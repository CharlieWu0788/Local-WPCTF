# 🛡️ Local WPCTF (V1.1.2)

## 🎯 Overview

Local WPCTF is a modular **Web Application Security Assessment Framework** designed for structured security assessment, attack surface modeling, validation, and security analytics.

Rather than acting as an automated exploitation tool, Local WPCTF focuses on building a reusable security reasoning framework capable of understanding modern web applications through a clean, extensible architecture.

Current supported and planned targets include:

- 🧩 WordPress
- 🧪 DVWA
- 🍔 OWASP Juice Shop
- 📚 WebGoat
- 🕷️ Mutillidae
- 🌐 Generic Web Applications

---

# 🧠 Design Philosophy

Local WPCTF follows several core principles:

- Clean Architecture
- Single Responsibility Principle
- Modular Design
- Framework Agnostic
- Security Reasoning over Signature Detection

The project is designed as a long-term security framework rather than a collection of individual scanners.

Every component has a clearly defined responsibility, allowing new targets and assessment modules to be added without affecting existing functionality.

---

# 🏗️ Layer Architecture

```text
                    Local WPCTF

        ┌─────────────────────────────┐
        │            Core             │
        │ Context • Classification    │
        │ Schema                      │
        └──────────────┬──────────────┘
                       │
        ┌──────────────▼──────────────┐
        │          Scanner            │
        │ Discovery • Enumeration     │
        │ Technology Detection        │
        └──────────────┬──────────────┘
                       │
        ┌──────────────▼──────────────┐
        │         Workflow            │
        │ Attack Surface              │
        │ Attack Graph                │
        │ Test Plan                   │
        │ Validation Planning         │
        └──────────────┬──────────────┘
                       │
        ┌──────────────▼──────────────┐
        │          Attack             │
        │ Attack Engines              │
        │ Validators                  │
        │ Wordlists                   │
        └──────────────┬──────────────┘
                       │
        ┌──────────────▼──────────────┐
        │         Executors           │
        │ Security Validation         │
        └──────────────┬──────────────┘
                       │
        ┌──────────────▼──────────────┐
        │         Analysis            │
        │ Risk                        │
        │ Coverage                    │
        │ Validation                  │
        │ Security Posture            │
        └──────────────┬──────────────┘
                       │
        ┌──────────────▼──────────────┐
        │          Reports            │
        │ Dashboard                   │
        │ JSON                        │
        │ OWASP Mapping               │
        └─────────────────────────────┘
```

---

# 🔄 Framework Pipeline

The execution pipeline is intentionally simple.

Business logic is isolated inside dedicated modules while `main.py` serves only as the pipeline orchestrator.

```text
Configuration
      │
      ▼
Scanner Pipeline
      │
      ▼
Application Context
      │
      ▼
Application Classification
      │
      ▼
Attack Surface Construction
      │
      ▼
Attack Graph Generation
      │
      ▼
Test Plan Generation
      │
      ▼
Validation Execution
      │
      ▼
Security Analytics
      │
      ▼
Report Generation
```

---

# 📁 Project Structure

```text
Local WPCTF/

├── analysis/
│   ├── Coverage Analytics
│   ├── Risk Analytics
│   ├── Validation Analytics
│   └── Security Posture
│
├── attack/
│   ├── Attack Engines
│   ├── Validators
│   └── Wordlist Loader
│
├── core/
│   ├── App Context
│   ├── App Classification
│   └── Schema Layer
│
├── executors/
│   └── Security Validation Executors
│
├── reports/
│   ├── Dashboard
│   ├── JSON Report
│   └── OWASP Mapping
│
├── resources/
│   ├── Payloads
│   └── Wordlists
│
├── scanners/
│   └── Discovery Modules
│
├── scripts/
│   └── Development Utilities
│
├── workflow/
│   ├── Attack Surface
│   ├── Attack Graph
│   ├── Test Plan
│   ├── Validation Execution
│   └── Execution Workflow
│
└── main.py
```

---

# 🚀 Core Capabilities

## 🔍 Security Discovery

- Authentication discovery
- SQL injection discovery
- XSS discovery
- Upload surface discovery
- Cookie inspection
- HTTP header inspection
- Directory enumeration
- API discovery
- WordPress reconnaissance

---

## 🧠 Application Intelligence

- Application context generation
- Framework classification
- Schema-based data normalization
- Unified scanner output

---

## 🕸️ Attack Surface Modeling

- Scan-result driven attack surface construction
- Graph-ready security modeling
- Structured security asset representation

---

## 🧩 Workflow Intelligence

- Attack graph generation
- Validation planning
- Execution workflow
- Security assessment pipeline

---

## 🧪 Security Validation

Current validation modules include:

- Authentication validation
- SQL validation
- XSS validation
- Brute-force testing
- Validation execution engine

---

## 📊 Security Analytics

- Risk analytics
- Coverage analytics
- Validation analytics
- Security posture evaluation

---

## 📄 Reporting

- JSON reports
- Executive dashboard
- OWASP Top 10 mapping
- Standardized reporting pipeline

---

# 🧱 Clean Architecture Principles

Local WPCTF enforces strict responsibility separation.

## Core

Responsible for:

- Context
- Classification
- Schema

---

## Scanner

Responsible only for discovering security information.

No business logic.

---

## Workflow

Responsible for:

- Attack Surface
- Attack Graph
- Test Plan
- Validation Planning

No scanning.

No reporting.

---

## Attack

Responsible for:

- Attack engines
- Validators
- Payload resources
- Wordlists

---

## Executors

Responsible only for executing specific security validations.

---

## Analysis

Responsible only for analytics.

- Risk
- Coverage
- Validation
- Security Posture

---

## Reports

Responsible only for rendering outputs.

- Dashboard
- JSON
- OWASP Mapping

---

# 📦 Version History

## 🟢 v0.x — WordPress Prototype

- WordPress-focused scanner
- Static vulnerability discovery
- Initial reporting pipeline

---

## 🔵 v1.0.0 — Framework Foundation

- Framework abstraction
- Multi-target architecture
- Attack graph modeling
- Workflow engine
- Security reasoning pipeline

---

## 🟣 v1.1.0 — Generic Scanner Preparation

- Generic scanner architecture
- Modular project organization
- Future multi-target foundation

---

## 🔵 v1.1.1 — Unified Scanner Schema

- Unified scanner schema
- Common scanner contract
- Cross-module compatibility

---

## 🟢 v1.1.2 — Clean Architecture Refactoring

Major architectural refactoring focused on maintainability and extensibility.

Highlights include:

- AppContext pipeline introduced
- Application classifier refactored
- Dedicated schema layer established
- Analysis decoupled from reporting
- JSON reporting redesigned
- Attack surface consumes scan results directly
- Legacy function discovery removed
- Main pipeline simplified into a pure orchestrator
- Improved modularity for future framework expansion

---

# 📄 Output

Generated reports are stored in:

```text
output/report.json
```

The report includes:

- Attack Surface
- Attack Graph
- Validation Results
- Risk Analytics
- Coverage Analytics
- Security Posture
- OWASP Mapping
- Executive Dashboard Data

---

# 🛡️ Safety

Local WPCTF is intended only for:

- Local laboratories
- Educational environments
- Authorized security testing
- Defensive security research

The framework is **not designed for unauthorized exploitation**.

---

# 🚀 Roadmap

## V1.1.3

- Generic Scanner Engine

## V1.1.4

- Generic Discovery Framework
- Target-independent scanner modules

## V1.1.5

- Workflow expansion
- Additional validation modules
- Improved attack graph reasoning

## V1.2

- AI Security Agent foundation
- Intelligent assessment planning
- Autonomous workflow generation

---

# 🎯 Project Vision

Local WPCTF is evolving from a collection of web security scanners into a **modular security reasoning framework**.

The long-term vision is to provide a reusable architecture capable of supporting diverse web applications, advanced security analytics, graph-based attack modeling, and future AI-assisted security assessment.

> **From vulnerability scanning to structured security intelligence.**