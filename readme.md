# Local WPCTF

## 🎯 Overview

Local WPCTF is a modular black-box security assessment framework focused on WordPress-based targets.

The project is designed for controlled security testing, attack surface discovery, validation-driven analysis, and security posture assessment.

The framework follows a staged workflow that progressively:

* Discovers attack surfaces
* Generates security test plans
* Maps findings to OWASP Top 10
* Validates discovered attack surfaces
* Assesses exploitability
* Produces standardized reports

---

## 🏗️ Architecture

```text
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
OWASP Classification
    ↓
Attack Surface Ranking
    ↓
Validation Execution
    ↓
Validation Analytics
    ↓
Exploitability Analysis
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
```

---

## 📁 Project Structure

```text
Local WPCTF/

├── main.py
├── config.json
├── requirements.txt
│
├── scanners/
│   ├── wordpress_scan.py
│   ├── auth_scan.py
│   ├── sql_scan.py
│   ├── xss_scan.py
│
├── workflow/
│   ├── function_discovery.py
│   ├── attack_surface.py
│   ├── test_plan.py
│   ├── validation_execution.py
│   ├── exploit_simulation.py
│   └── pipeline_checker.py
│
├── executors/
│   ├── auth_executor.py
│   ├── sql_executor.py
│   ├── xss_executor.py
│
├── analysis/
│   ├── coverage_analyzer.py
│   ├── posture_analyzer.py
│   ├── risk_analytics.py
│   ├── validation_analytics.py
│   └── exploitability_engine.py
│
├── reports/
│   ├── confidence_scoring.py
│   ├── dashboard_generator.py
│   ├── json_report.py
│   ├── owasp_mapper.py
│   ├── risk_assessor.py
│   └── risk_engine.py
│
└── output/
    └── report.json
```

---

## 🚀 Features

### 🔍 Discovery

* WordPress Detection
* Authentication Discovery
* Function Discovery
* Attack Surface Modeling

### 🧪 Assessment

* SQL Reconnaissance
* XSS Reconnaissance
* OWASP Classification
* Risk Ranking

### ✅ Validation

* Authentication Validation
* SQL Interaction Validation
* XSS Interaction Validation
* Validation Evidence Collection

### 🎯 Exploitability

* Validation-Based Scoring
* Exploitability Assessment
* Risk Classification
* Confidence-Oriented Analysis

### 📊 Analytics

* Coverage Analysis
* Risk Distribution Analysis
* Security Posture Evaluation
* Dashboard Generation

### 📝 Reporting

* Standardized JSON Reporting
* Validation Results
* Validation Summary
* Exploitability Results

---

## 📦 Version History

### 🟢 v0.1.1

* Initial WordPress Detection
* Basic Scanning Workflow

### 🔵 v0.2.0

* Authentication Discovery
* SQL Reconnaissance
* XSS Reconnaissance

### 🟣 v0.3.1

* Function Discovery
* Attack Surface Modeling

### 🟠 v0.4.0

* Test Plan Generation
* OWASP Mapping

### 🔴v0.5.6 — Generate Security Data

* Attack Surface Ranking
* Confidence Scoring
* Pipeline Validation
* Standardized Reporting
* Risk Engine Integration

### 🟡 v0.6.x — Analyze Security Data

* Coverage Analysis
* Risk Distribution Analytics
* Security Posture Evaluation
* Executive Dashboard Generation


### 🟢 v0.7.0 — Validate Security Data
* Validation Execution Layer
* Authentication Validation
* SQL Validation
* XSS Validation
* Validation Evidence Collection
* Validation Analytics
* Validation Scoring
* Exploitability Assessment
* Login Endpoint Verification
* Enhanced Function Discovery
* Extended Dashboard Metrics
* Extended Report Schema

---

## 📄 Report Output

Generated report includes:

* Attack Surface Inventory
* Test Plan
* OWASP Mapping
* Validation Results
* Validation Summary
* Exploitability Results
* Coverage Analytics
* Risk Distribution
* Security Posture
* Executive Dashboard

Output:

```text
output/report.json
```

---

## ⚠️ Safety Model

Local WPCTF is designed for:

* Local laboratory environments
* Educational security testing
* Controlled WordPress targets
* Defensive security validation

The framework does not perform:

* Credential brute forcing
* Database dumping
* Destructive exploitation
* Unauthorized target testing