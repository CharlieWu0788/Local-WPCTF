# Local WPCTF

A lightweight local WordPress security testing framework that combines reconnaissance, attack surface modeling, test plan generation, and OWASP-based classification.

It is designed to detect and organize web attack surfaces including authentication endpoints, SQL injection points, XSS vectors, and WordPress-specific misconfigurations.

---

## ⚡ Features (v0.3.0)

### Scanner Layer

* WordPress detection
* Generic authentication page discovery
* Login endpoint identification through link analysis and keyword matching
* Basic SQL injection reconnaissance (parameter-based)
* Basic reflected XSS detection (form-based)

---

### Workflow Layer

* Attack surface modeling
* Security test plan generation
* Authentication surface normalization
* Structured workflow output

---

### Security Classification Layer (NEW)

* OWASP Top 10 mapping for generated test cases
* Structured vulnerability categorization
* Risk classification based on test intent
* Standardized security findings output

---

### Reporting Layer

* Unified JSON reporting
* OWASP-aligned structured output format

---

## 📊 Module Explanation

| Module         | Purpose |
| -------------- | --------|
| wordpress_scan | Detect WordPress installations through common fingerprints |
| auth_scan      | Discover authentication surfaces using link analysis and login-page heuristics |
| sql_scan       | Perform basic SQL injection reconnaissance |
| xss_scan       | Perform basic reflected XSS reconnaissance |
| attack_surface | Convert scanner outputs into attack surface entries |
| test_plan      | Generate testing tasks from identified attack surfaces |
| owasp_mapper   | Map generated test cases to OWASP Top 10 categories |

---

## 📁 Project Structure

| Directory                  | Description |
| -------------------------- | ----------- |
| main.py                    | Entry point |
| config.json                | Target configuration |
| scanners/wordpress_scan.py | WordPress detection |
| scanners/auth_scan.py      | Authentication discovery |
| scanners/sql_scan.py       | SQL injection reconnaissance |
| scanners/xss_scan.py       | XSS reconnaissance |
| workflow/attack_surface.py | Attack surface modeling |
| workflow/test_plan.py      | Security test plan generation |
| reports/owasp_mapper.py    | OWASP classification mapping |

---

## 🧠 Architecture

```text
config.json
     ↓
scanner modules
     ↓
attack surface modeling
     ↓
test plan generation
     ↓
OWASP Top 10 classification
     ↓
structured security findings
     ↓
JSON output
```

The framework now extends beyond reconnaissance and test generation, introducing a classification layer that maps security tests to OWASP Top 10 categories for structured vulnerability analysis.

---

## 🚧 Roadmap

### v0.1.x

* WordPress detection
* Authentication discovery
* SQL reconnaissance
* XSS reconnaissance

### v0.2.0

* Attack surface modeling
* Test plan generation
* Authentication surface normalization

### v0.3.0 (CURRENT)

* OWASP Top 10 classification
* Security test categorization
* Structured vulnerability reporting

### v0.3.1 (Planned)

* Improved authentication discovery
* Generic login form detection
* Reduced CMS-specific heuristics

### Future

* Attack chain analysis
* Remediation guidance
* Automated retesting