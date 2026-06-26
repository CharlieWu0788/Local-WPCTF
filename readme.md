# 🛡️ Local WPCTF (V1.1.1)

## 🎯 Overview

Local Web Page CTF is a modular **Web Application Security Assessment Framework** designed for black-box security analysis, attack surface modeling, and exploitability reasoning across modern web applications.

Unlike earlier WordPress-focused versions, V1.1 introduces a **framework-agnostic security engine** capable of analyzing diverse targets such as:

- 🧩 WordPress applications
- 🧪 DVWA
- 🍔 OWASP Juice Shop
- 📚 WebGoat
- 🌐 Generic PHP / web applications

The framework focuses on **structured security reasoning**, not signature-based scanning.

---

## 🧠 Core Design Philosophy (V1.1.0)

Local WPCTF V1.1.0 is built around a layered reasoning pipeline:

- 🔍 From discovery → modeling → reasoning → exploit path analysis
- 🧬 From isolated vulnerabilities → attack chains
- 🕸️ From static scanning → graph-based security intelligence

The goal is not just detection, but **security understanding through structure**.

---

## 🏗️ Architecture (V1.1.0)

```text
🎯 Target Application
    ↓
🧠 Application Classification
    ↓
🔐 Authentication & Surface Scanning
    ↓
🔎 Function Discovery
    ↓
🕸️ Attack Surface Modeling (Graph-Based)
    ↓
🔥 Exploit Path Engine
    ↓
🧪 Test Plan Generation
    ↓
📌 OWASP Classification
    ↓
✅ Validation Execution
    ↓
⚠️ Exploitability Analysis
    ↓
📊 Risk & Coverage Analytics
    ↓
🧭 Security Posture Evaluation
    ↓
📈 Dashboard Generation
    ↓
📄 Standardized Reporting
```

## 📁 Project Structure

```text
Local WPCTF/
├── .vscode
│   └── launch.json
├── analysis
│   ├── __init__.py
│   ├── coverage_analyzer.py
│   ├── exploitability_engine.py
│   ├── posture_analyzer.py
│   ├── risk_analytics.py
│   └── validation_analytics.py
├── config.json
├── core
│   ├── app_classifier.py
│   ├── app_context.py
│   └── schema
│       ├── __init__.py
│       ├── graph_schema.py
│       ├── safe_wrap.py
│       └── scanner_schema.py
├── executors
│   ├── __init__.py
│   ├── auth_executor.py
│   ├── sql_executor.py
│   └── xss_executor.py
├── main.py
├── output
│   └── report.json
├── readme.md
├── reports
│   ├── __init__.py
│   ├── confidence_scoring.py
│   ├── dashboard_generator.py
│   ├── json_report.py
│   ├── owasp_mapper.py
│   ├── risk_assessor.py
│   ├── risk_engine.py
│   └── security_graph_dashboard.py
├── requirements.txt
├── scanners
│   ├── __init__.py
│   ├── api_scan.py
│   ├── auth_scan.py
│   ├── cookie_scan.py
│   ├── directory_scan.py
│   ├── header_scan.py
│   ├── sql_scan.py
│   ├── upload_scan.py
│   ├── wordpress_scan.py (legacy plugin module)
│   └── xss_scan.py
├── tools
│   └── tree_view.py
└── workflow
    ├── __init__.py
    ├── attack_graph.py
    ├── attack_surface.py
    ├── exploit_path_engine.py
    ├── exploit_simulation.py
    ├── function_discovery.py
    ├── pipeline_checker.py
    ├── test_plan.py
    └── validation_execution.py
```

## 🚀 Key Features (V1.1.0)

### 🔍 Application Intelligence

- 🧠 Multi-framework application classification
- 🌐 Technology-agnostic target understanding
- 🧩 Dynamic application context modeling

---

### 🕸️ Attack Surface Intelligence

- 🔎 Function-based surface extraction
- 🧠 Semantic attack surface classification
- 📊 Confidence-based prioritization

---

### 🧬 Graph-Based Security Modeling

- 🕸️ Attack surface graph construction
- 🔗 Node-edge security relationship modeling
- 🧭 Multi-step attack path representation

---

### 🔥 Exploit Path Engine

- ⚡ Automatic attack chain discovery
- 🧠 Multi-step exploitation path analysis
- 📉 Risk-ranked exploit path generation

---

### 🧪 Security Assessment

- 💉 SQL injection surface detection
- 🧷 XSS reflection analysis
- 🔐 Authentication surface discovery
- 🧩 Business logic surface modeling

---

### 📊 Security Analytics

- 📉 Risk distribution analysis
- 📡 Coverage evaluation
- 🧭 Security posture scoring
- 🧪 Validation analytics

---

### 📄 Reporting & Visualization

- 📄 Structured JSON reporting
- 📌 OWASP Top 10 mapping
- 📊 Executive dashboard generation
- ⚠️ Exploitability scoring integration

---

## 📦 Version History

### 🟢 v0.x — WordPress Era

- 🧱 WordPress-specific scanning engine
- 🔍 Static vulnerability detection
- ➡️ Linear workflow pipeline
- 📌 Basic OWASP mapping

---

### 🔵 v1.0 — Web Application Security Intelligence Engine

- 🌐 Full framework abstraction layer
- 🧠 Application classification system
- 🕸️ Graph-based attack surface modeling
- 🔥 Exploit path engine (multi-step attack chains)
- 🧪 Multi-target support (DVWA, Juice Shop, WebGoat)
- 🧬 Security reasoning pipeline architecture
- 🔄 Backward compatibility preserved for WordPress modules

---

### 🟣 v1.1.0 — Generic Scanner Expansion

- 🏗️ Prepared generic scanner project structure
- 🔌 Introduced placeholder modules for future discovery scanners
- 📦 Established foundation for framework-agnostic scanner expansion

---

### 🔵 v1.1.1

- 🧩 Introduced a unified generic scanner schema
- 🔄 Preserved backward compatibility with V1.0.x scanners
- 🛡️ Established a common contract for future discovery scanners

## 📄 Output

Generated standardized report is stored at:

```text 
output/report.json
```

### 📊 Report includes:

- 🕸️ Attack Surface Graph
- 🔥 Exploit Paths (attack chains)
- ⚠️ Risk Scoring
- 📌 OWASP Mapping
- ✅ Validation Results
- 🧭 Security Posture Metrics
- 📡 Coverage Analytics
- 📈 Executive Dashboard Data

---

## ⚠️ Safety Model

### 🧪 Local WPCTF is designed for:

- 🏠 Local laboratory environments
- 🎓 Educational security testing
- 🔐 Controlled and authorized applications
- 🛡️ Defensive security validation

---

### 🚫 The framework does NOT perform:

- ❌ Unauthorized external scanning
- ❌ Credential brute forcing
- ❌ Destructive exploitation
- ❌ Data exfiltration attacks

---

## 🧭 Project Status

### 🟢 Current Version: V1.1.1

- Generic scanner schema introduced
- Schema-safe pipeline architecture
- Graph-based attack modeling system
- Unified security reasoning engine
- Stable cross-module contract enforcement

---

## 🚀 Future Direction (Planned)

### 🔵 Upcoming V1.1 Releases

#### V1.1.2
- Safe wrapper upgrade

#### V1.1.3
- Generic scanner implementation

#### V1.1.4
- Scanner integration

#### V1.1.5
- Attack surface expansion

---

## 🏁 Summary

Local WPCTF V1.1.0 continues the transition from:

> **tool-based scanning → structured security intelligence system**

V1.1 establishes the foundation for a generic, framework-agnostic scanner architecture that enables future attack surface expansion across diverse web applications.

It is designed to evolve into a full **security reasoning engine**, not just a scanner.