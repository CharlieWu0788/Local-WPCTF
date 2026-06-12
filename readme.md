# Local WPCTF

A lightweight local WordPress CTF reconnaissance framework for detecting attack surfaces including login endpoints, SQLi, XSS, and WordPress-specific misconfigurations.

---

## ⚡ Features (v0.1.0)

- WordPress detection
- Login page discovery (`/wp-login.php`, `/wp-admin`)
- Basic SQL injection reconnaissance (parameter-based)
- Basic reflected XSS detection (form-based)
- Unified JSON reporting
- Modular scanner architecture

---

## 📁 Project Structure
.gitignore
│  config.json
│  main.py
│  readme.md
│  requirements.txt
│  
├─reports
│      json_report.py
│      
└─scanners
    │  auth_scan.py
    │  sql_scan.py
    │  wordpress_scan.py
    │  xss_scan.py
    │  
    └─__pycache__


---

## 🚀 Usage

### 1. Configure target
//json
Edit 'Config.json':
{
  "url": "http://localhost:8081"
}

### 2. Run scanner
//bash
python main.py

### 3. Example output
//json
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

🧠 Architecture
main.py
   ↓
scanner modules
   ↓
structured results
   ↓
JSON output

Each scanner is independent and returns a standardized dictionary.

🧪 Tested Environment
Local Docker WordPress
Apache / Nginx WordPress installations
Default themes (Twenty series)