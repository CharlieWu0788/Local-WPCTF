import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def scan_sql_injection(url):
    """
    Basic SQL Injection reconnaissance scanner.

    Detection methods:
    - Baseline response comparison
    - SQL error message detection
    - Response length differences
    - HTTP status code changes

    Returns:
        {
            "sql_injection_detected": bool,
            "evidence": list,
            "tested_payloads": list
        }
    """

    PAYLOADS = [
        "'",
        '"',
        "' AND 1=1--",
        "' AND 1=2--",
        '" AND 1=1--',
        '" AND 1=2--',
    ]

    ERROR_MESSAGES = [
        "sql syntax",
        "mysql",
        "mariadb",
        "postgresql",
        "sqlite",
        "odbc",
        "oracle",
        "unclosed quotation mark",
        "database error",
        "syntax error",
        "warning: mysql",
        "pg_query",
    ]

    evidence = []
    detected = False

    try:
        baseline = requests.get(url, timeout=5)

        baseline_status = baseline.status_code
        baseline_length = len(baseline.text)

    except requests.RequestException as e:
        return {
            "sql_injection_detected": False,
            "evidence": [f"Request failed: {str(e)}"],
            "tested_payloads": PAYLOADS
        }

    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    if not params:
        return {
            "sql_injection_detected": False,
            "evidence": [
                "No URL parameters found for SQL injection testing"
            ],
            "tested_payloads": PAYLOADS
        }

    for param in params:

        original_value = params[param][0]

        for payload in PAYLOADS:

            test_params = params.copy()
            test_params[param] = [original_value + payload]

            test_query = urlencode(test_params, doseq=True)

            test_url = urlunparse(
                (
                    parsed.scheme,
                    parsed.netloc,
                    parsed.path,
                    parsed.params,
                    test_query,
                    parsed.fragment,
                )
            )

            try:
                response = requests.get(test_url, timeout=5)

                response_text = response.text.lower()

                for error in ERROR_MESSAGES:
                    if error in response_text:
                        detected = True
                        evidence.append(
                            f"Possible SQL error detected on parameter '{param}' using payload '{payload}'"
                        )
                        break

                if response.status_code >= 500:
                    detected = True
                    evidence.append(
                        f"Server returned HTTP {response.status_code} on parameter '{param}' using payload '{payload}'"
                    )

                length_diff = abs(
                    len(response.text) - baseline_length
                )

                if baseline_length > 0:
                    diff_percent = (
                        length_diff / baseline_length
                    ) * 100

                    if diff_percent > 30:
                        evidence.append(
                            f"Response length changed by {diff_percent:.1f}% on parameter '{param}' using payload '{payload}'"
                        )

                if response.status_code != baseline_status:
                    evidence.append(
                        f"Status code changed from {baseline_status} to {response.status_code} on parameter '{param}' using payload '{payload}'"
                    )

            except requests.RequestException:
                continue

    return {
        "sql_injection_detected": detected,
        "evidence": list(set(evidence)),
        "tested_payloads": PAYLOADS,
    }