# 🛡️ Local WPCTF (V1.0.1)

## 🎯 Overview

Local Web Page CTF is a modular **Web Application Security Assessment Framework** designed for black-box security analysis, attack surface modeling, and exploitability reasoning across modern web applications.

Unlike earlier WordPress-focused versions, V1.0 introduces a **framework-agnostic security engine** capable of analyzing diverse targets such as:

- 🧩 WordPress applications
- 🧪 DVWA
- 🍔 OWASP Juice Shop
- 📚 WebGoat
- 🌐 Generic PHP / web applications

The framework focuses on **structured security reasoning**, not signature-based scanning.

---

## 🧠 Core Design Philosophy (V1.0.1)

Local WPCTF V1.0.1 is built around a layered reasoning pipeline:

- 🔍 From discovery → modeling → reasoning → exploit path analysis
- 🧬 From isolated vulnerabilities → attack chains
- 🕸️ From static scanning → graph-based security intelligence

The goal is not just detection, but **security understanding through structure**.

---

## 🏗️ Architecture (V1.0.1)

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

├── main.py
├── config.json
├── requirements.txt
│
├── core/
│   ├── app_context.py
│   ├── app_classifier.py
│
├── scanners/
│   ├── auth_scan.py
│   ├── sql_scan.py
│   ├── xss_scan.py
│   ├── wordpress_scan.py (legacy plugin module)
│
├── workflow/
│   ├── function_discovery.py
│   ├── attack_surface.py
│   ├── attack_graph.py
│   ├── exploit_path_engine.py
│   ├── test_plan.py
│   ├── validation_execution.py
│   ├── pipeline_checker.py
│
├── analysis/
│   ├── coverage_analyzer.py
│   ├── posture_analyzer.py
│   ├── risk_analytics.py
│   ├── validation_analytics.py
│
├── reports/
│   ├── confidence_scoring.py
│   ├── dashboard_generator.py
│   ├── json_report.py
│   ├── owasp_mapper.py
│   ├── risk_engine.py
│
└── output/
    └── report.json
```

## 🚀 Key Features (V1.0.1)

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

### 🟢 Current Version: V1.0.1

- Schema-safe pipeline architecture
- Graph-based attack modeling system
- Unified security reasoning engine
- Stable cross-module contract enforcement

---

## 🚀 Future Direction (Planned)

### 🔵 V1.1 Enhancements

- 🧠 Exploit path chaining optimization
- 🕸️ Multi-surface correlation scoring
- 📊 Graph centrality risk weighting
- 🔍 Automatic OWASP refinement engine
- ⚙️ Schema contract registry system

---

## 🏁 Summary

Local WPCTF V1.0.1 represents a transition from:

> **tool-based scanning → structured security intelligence system**

It is designed to evolve into a full **security reasoning engine**, not just a scanner.