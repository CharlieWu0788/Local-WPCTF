# Local WPCTF

A lightweight local WordPress security testing framework that combines reconnaissance, attack surface modeling, test plan generation, and OWASP-based classification.

It is designed to identify and organize web attack surfaces including authentication endpoints, SQL injection points, XSS vectors, and WordPress-specific misconfigurations.

---

## ⚡ Features (v0.4.0)

### Scanner Layer

* WordPress detection
* Hybrid authentication surface discovery
  - Link-based discovery
  - Endpoint probing (e.g., /wp-login.php)
  - Form-based login detection
  - Validation-based confirmation
* Basic SQL injection reconnaissance (parameter-based)
* Basic reflected XSS detection (form-based)

---

### Workflow Layer

* Attack surface modeling
* Security test plan generation
* Authentication surface normalization
* Structured workflow output

---

### Security Classification Layer

* OWASP Top 10 mapping for generated test cases
* Structured vulnerability categorization
* Risk classification based on test intent
* Standardized security findings output

---

### Reporting Layer

* Standardized security assessment report generation
* Report metadata and scan information
* Summary statistics
* Persistent JSON report export
* Unified workflow output structure

---

### Reporting Layer

* Unified JSON output
* Structured security findings format
* OWASP-aligned result mapping

---

## 📊 Module Explanation

| Module         | Purpose |
| -------------- | --------|
| wordpress_scan | Detect WordPress installations through fingerprinting |
| auth_scan      | Hybrid authentication discovery engine |
| sql_scan       | Basic SQL injection reconnaissance |
| xss_scan       | Basic reflected XSS reconnaissance |
| attack_surface | Convert scan results into structured attack surfaces |
| test_plan      | Generate test cases from attack surfaces |
| owasp_mapper   | Map test cases to OWASP Top 10 categories |
| json_report    | Generate standardized security assessment reports |


---

## 🧠 Architecture

```text
Target URL
    ↓
Scanner Layer
    ↓
Attack Surface Modeling
    ↓
Test Plan Generation
    ↓
OWASP Top 10 Classification
    ↓
Standardized Reporting
    ↓
JSON Export
```

The framework now supports hybrid authentication discovery by combining link analysis, form-based detection, and endpoint probing to improve coverage of real-world login surfaces.

---

## 📁 Project Structure

```
Local WPCTF/

├── main.py
├── config.json
│
├── scanners/
│   ├── wordpress_scan.py
│   ├── auth_scan.py
│   ├── sql_scan.py
│   ├── xss_scan.py
│   └── __init__.py
│
├── workflow/
│   ├── attack_surface.py
│   ├── test_plan.py
│   └── __init__.py
│
├── reports/
│   ├── owasp_mapper.py
│   ├── json_report.py
│   └── __init__.py
│
└── README.md
```

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
* Basic workflow orchestration

### v0.3.0

* OWASP Top 10 classification
* Structured security findings

### v0.3.1 

* Hybrid authentication discovery engine
* Endpoint probing for login surfaces
* Form-based login detection
* Improved authentication validation logic

### v0.4.0

* Standardized report generation
* Security assessment metadata
* Summary statistics
* Persistent JSON export

---

### v0.5.0 (Planned)

* Function discovery
* Business functionality identification
* Enhanced attack surface enrichment
* Context-aware test planning

---

## 📌 Notes

This version significantly improves authentication surface coverage by combining multiple discovery strategies, reducing reliance on CMS-specific assumptions while maintaining compatibility with WordPress environments.
```