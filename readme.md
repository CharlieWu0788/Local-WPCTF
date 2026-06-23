# Local WPCTF

A lightweight local WordPress security testing framework that combines reconnaissance, attack surface modeling, function discovery, OWASP-based classification, risk ranking, workflow validation, security analytics, and standardized reporting.

It is designed to identify and organize web attack surfaces including authentication endpoints, SQL injection points, XSS vectors, and WordPress-specific misconfigurations.

Version 0.6.0 extends the framework beyond attack-surface generation by introducing analytical capabilities such as coverage assessment, risk distribution analysis, security posture evaluation, and dashboard-oriented reporting.

---

## ⚡ Features (v0.6.0)

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

### Analytics Layer

* Attack surface coverage analysis
* Risk distribution analysis
* Security posture evaluation
* Workflow outcome analytics
* Security assessment summarization

---

### Dashboard Layer

* Coverage overview generation
* Risk overview generation
* Security posture summaries
* Executive dashboard reporting
* Aggregated assessment metrics

---

### Reporting Layer

* Standardized security assessment report generation
* Report metadata and scan information
* Summary statistics
* Persistent JSON report export
* Unified workflow output structure

---

## 📊 Module Explanation

| Module              | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| wordpress_scan      | Detect WordPress installations through fingerprinting        |
| auth_scan           | Hybrid authentication discovery engine                       |
| sql_scan            | Basic SQL injection reconnaissance                           |
| xss_scan            | Basic reflected XSS reconnaissance                           |
| function_discovery  | Discover security-relevant application functions             |
| attack_surface      | Convert discovered functions into structured attack surfaces |
| test_plan           | Generate security test cases from attack surfaces            |
| confidence_scoring  | Calculate attack surface confidence values                   |
| risk_assessor       | Assess potential security impact                             |
| risk_engine         | Rank attack surfaces based on confidence and risk            |
| pipeline_checker    | Validate workflow integrity and semantic consistency         |
| owasp_mapper        | Map generated test cases to OWASP Top 10 categories          |
| coverage_analyzer   | Measure attack-surface coverage and workflow completeness    |
| risk_analytics      | Analyze overall risk distribution across attack surfaces     |
| posture_analyzer    | Evaluate overall security posture                            |
| dashboard_generator | Generate summarized assessment dashboards                    |
| json_report         | Generate standardized security assessment reports            |

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
Coverage Analysis
    ↓
Risk Distribution Analysis
    ↓
Security Posture Evaluation
    ↓
Dashboard Generation
    ↓
Standardized Reporting
    ↓
JSON Export
```

The framework uses an attack-surface-driven workflow that transforms reconnaissance results into structured security testing plans, OWASP-aligned classifications, risk-prioritized findings, and analytical security assessments.

---

## 📁 Project Structure

```text
Local WPCTF/

├── main.py
├── config.json
├── requirements.txt
├── README.md
│
├── .vscode/
│   └── launch.json
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
├── analytics/
│   ├── coverage_analyzer.py
│   ├── risk_analytics.py
│   ├── posture_analyzer.py
│   └── __init__.py
│
└── reports/
    ├── confidence_scoring.py
    ├── risk_assessor.py
    ├── risk_engine.py
    ├── owasp_mapper.py
    ├── dashboard_generator.py
    ├── json_report.py
    └── __init__.py
```

---

## 📄 Report Structure

```json
{
  "metadata": {
    "framework": "Local WPCTF",
    "version": "v0.6.0",
    "target": "http://localhost:8081",
    "timestamp": "..."
  },

  "summary": {
    "attack_surface_count": 0,
    "test_count": 0,
    "finding_count": 0
  },

  "attack_surface": [],

  "test_plan": [],

  "owasp": [],

  "analytics": {
    "coverage": {
      "surface_count": 0,
      "covered_count": 0,
      "uncovered_count": 0,
      "coverage_score": 0
    },

    "risk_distribution": {
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0,
      "total": 0
    },

    "security_posture": {
      "security_posture": "Good"
    },

    "dashboard": {
      "coverage_score": 0,
      "overall_risk": {},
      "security_posture": "Good"
    }
  }
}
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

### v0.5.6

* Function discovery
* Attack surface enrichment
* Context-aware test planning
* Confidence scoring framework
* Risk assessment workflow
* Risk-based attack surface ranking
* OWASP classification integration improvements
* Pipeline validation checker
* Semantic workflow validation
* Workflow integrity verification
* End-to-end pipeline consistency checks

### v0.6.0

* Security analytics framework
* Attack surface coverage analysis
* Risk distribution analysis
* Security posture evaluation
* Dashboard generation
* Executive assessment summaries
* Coverage metrics reporting
* Aggregated security analytics
* Workflow outcome analytics

---

## 📌 Notes

Version 0.5.6 completed the attack-surface-driven security testing pipeline by integrating reconnaissance, function discovery, attack surface construction, OWASP classification, risk ranking, workflow validation, and standardized reporting.

Version 0.6.0 extends Local WPCTF into a security analytics platform. In addition to generating security testing data, the framework now analyzes workflow outcomes through coverage measurement, risk distribution analysis, security posture evaluation, and dashboard-oriented reporting.

The v0.6.x series represents the transition from generating security data to analyzing security data while preserving the modular workflow architecture established in previous versions.
