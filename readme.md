# Local WPCTF

A lightweight local WordPress security testing framework that combines reconnaissance, attack surface modeling, function discovery, OWASP-based classification, risk ranking, workflow validation, and standardized reporting.

It is designed to identify and organize web attack surfaces including authentication endpoints, SQL injection points, XSS vectors, and WordPress-specific misconfigurations.

---

## ⚡ Features (v0.5.6)

### Scanner Layer

* WordPress detection
* Hybrid authentication surface discovery

  * Link-based discovery
  * Endpoint probing (e.g., `/wp-login.php`)
  * Form-based login detection
  * Validation-based confirmation
* Basic SQL injection reconnaissance (parameter-based)
* Basic reflected XSS detection (form-based)

---

### Workflow Layer

* Function discovery
* Attack surface modeling
* Attack surface enrichment
* Security test plan generation
* Authentication surface normalization
* Structured workflow orchestration

---

### Security Classification Layer

* OWASP Top 10 mapping for generated test cases
* Structured vulnerability categorization
* Risk-based attack surface ranking
* Confidence-based attack surface scoring
* Standardized security findings output

---

### Validation Layer

* Pipeline validation checker
* Workflow consistency verification
* Attack surface integrity validation
* OWASP mapping verification
* Semantic workflow validation

---

### Reporting Layer

* Standardized security assessment report generation
* Report metadata and scan information
* Summary statistics
* Persistent JSON report export
* Unified workflow output structure

---

## 📊 Module Explanation

| Module             | Purpose                                                      |
| ------------------ | ------------------------------------------------------------ |
| wordpress_scan     | Detect WordPress installations through fingerprinting        |
| auth_scan          | Hybrid authentication discovery engine                       |
| sql_scan           | Basic SQL injection reconnaissance                           |
| xss_scan           | Basic reflected XSS reconnaissance                           |
| function_discovery | Discover security-relevant application functions             |
| attack_surface     | Convert discovered functions into structured attack surfaces |
| test_plan          | Generate security test cases from attack surfaces            |
| confidence_scoring | Calculate attack surface confidence values                   |
| risk_assessor      | Assess potential security impact                             |
| risk_engine        | Rank attack surfaces based on confidence and risk            |
| pipeline_checker   | Validate workflow integrity and semantic consistency         |
| owasp_mapper       | Map generated test cases to OWASP Top 10 categories          |
| json_report        | Generate standardized security assessment reports            |

---

## 🧠 Architecture

```text
Target URL
    ↓
WordPress Detection
    ↓
Authentication Scan
    ↓
SQL Reconnaissance
    ↓
XSS Reconnaissance
    ↓
Function Discovery
    ↓
Attack Surface Modeling
    ↓
Test Plan Generation
    ↓
OWASP Top 10 Classification
    ↓
Attack Surface Ranking
    ↓
Pipeline Validation
    ↓
Standardized Reporting
    ↓
JSON Export
```

The framework uses an attack-surface-driven workflow that transforms reconnaissance results into structured security testing plans, OWASP-aligned classifications, and risk-prioritized findings.

---

## 📁 Project Structure

```text
Local WPCTF/

├── main.py
├── config.json
├── requirements.txt
│
├── output/
│   └── report.json
│
├── scanners/
│   ├── wordpress_scan.py
│   ├── auth_scan.py
│   ├── sql_scan.py
│   ├── xss_scan.py
│   └── __init__.py
│
├── workflow/
│   ├── function_discovery.py
│   ├── attack_surface.py
│   ├── test_plan.py
│   ├── pipeline_checker.py
│   └── __init__.py
│
├── reports/
│   ├── confidence_scoring.py
│   ├── risk_assessor.py
│   ├── risk_engine.py
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

### v0.3.1

* OWASP Top 10 classification
* Structured security findings
* Hybrid authentication discovery engine
* Endpoint probing for login surfaces
* Form-based login detection
* Improved authentication validation logic

### v0.4.0

* Standardized report generation
* Security assessment metadata
* Summary statistics
* Persistent JSON export

### v0.5.0

* Function discovery
* Attack surface enrichment
* Context-aware test planning

### v0.5.1

* Confidence scoring framework

### v0.5.2

* Risk assessment workflow

### v0.5.3

* Risk-based attack surface ranking

### v0.5.4

* OWASP classification integration improvements

### v0.5.5

* Pipeline validation checker

### v0.5.6

* Semantic workflow validation
* Workflow integrity verification
* End-to-end pipeline consistency checks

---

## 📌 Notes

Version 0.5.6 represents the stable completion of the Local WPCTF attack-surface pipeline. The framework now supports reconnaissance, function discovery, attack surface construction, OWASP classification, risk prioritization, and workflow integrity validation through a unified security testing workflow.

This version serves as the foundation for future analytical and intelligence-driven capabilities planned for the v0.6.x series.
