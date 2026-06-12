# Local WPCTF

A lightweight local WordPress CTF reconnaissance framework for detecting attack surfaces including login endpoints, SQLi, XSS, and WordPress-specific misconfigurations.

---

## ⚡ Features (v0.1.1)

- WordPress detection
- Generic authentication page discovery
- Login endpoint identification through link analysis and keyword matching
- Basic SQL injection reconnaissance (parameter-based)
- Basic reflected XSS detection (form-based)
- Unified JSON reporting
- Modular scanner architecture

---

## 📊 Module Explaination
| Module         | Purpose                                                                        |
|----------------|--------------------------------------------------------------------------------|
| wordpress_scan | Detect WordPress installations through common fingerprints                     |
| auth_scan      | Discover authentication surfaces using link analysis and login-page heuristics |
| sql_scan       | Perform basic SQL injection reconnaissance                                     |
| xss_scan       | Perform basic reflected XSS reconnaissance                                     |

---

## 📁 Project Structure
| Directory | Description |
|------------|------------|
| main.py | Entry point |
| config.json | Target configuration |
| reports/json_report.py | JSON reporting module |
| scanners/wordpress_scan.py | WordPress detection |
| scanners/auth_scan.py | Authentication discovery |
| scanners/sql_scan.py | SQL injection reconnaissance |
| scanners/xss_scan.py | XSS reconnaissance |

---

## 🚀 Usage

### 1. Configure target

Edit 'Config.json':

```json
{
  "url": "http://localhost:8081"
}
```

### 2. Run scanner

```bash
python main.py
```

### 3. Example output

```json
{
  "wordpress": {
    "wordpress_detected": true,
    "evidence": [
      "wp-content found",
      "wp-includes found",
      "generator tag found"
    ]
  },
  "auth": {
    "login_page_found": true,
    "login_url": "http://localhost:8081/wp-login.php",
    "status_code": 200,
    "evidence": [
      "WordPress login page detected"
    ],
    "error": null
  },
  "sql": {
    "sql_injection_detected": false,
    "evidence": [
      "No URL parameters found for SQL injection testing"
    ],
    "tested_payloads": ["'","\""]
  },
  "xss": {
    "xss_detected": false,
    "evidence": [
      "No forms discovered"
    ],
    "tested_payloads": ["<script>alert(1)</script>"]
  }
}
```

## 🧠 Architecture

```text
config.json
     ↓
main.py
     ↓
scanner modules
     ↓
structured results
     ↓
JSON output
```

Each scanner is independent and returns a standardized dictionary.

🧪 Tested Environment
```text
Local Docker WordPress
Apache / Nginx WordPress installations
Default themes (Twenty series)
```