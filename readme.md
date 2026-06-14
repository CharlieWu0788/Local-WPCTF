# Local WPCTF

A lightweight local WordPress security testing framework that combines reconnaissance, attack surface modeling, and test plan generation. For detecting attack surfaces including login endpoints, SQLi, XSS, and WordPress-specific misconfigurations.

---

## ⚡ Features (v0.2.0)

### Scanner Layer

* WordPress detection
* Generic authentication page discovery
* Login endpoint identification through link analysis and keyword matching
* Basic SQL injection reconnaissance (parameter-based)
* Basic reflected XSS detection (form-based)

### Workflow Layer

* Attack surface modeling
* Security test plan generation
* Authentication surface normalization
* Structured workflow output

### Reporting

* Unified JSON reporting
* Standardized result structure

---

## 📊 Module Explanation

| Module         | Purpose                                                                        |
| -------------- | ------------------------------------------------------------------------------ |
| wordpress_scan | Detect WordPress installations through common fingerprints                     |
| auth_scan      | Discover authentication surfaces using link analysis and login-page heuristics |
| sql_scan       | Perform basic SQL injection reconnaissance                                     |
| xss_scan       | Perform basic reflected XSS reconnaissance                                     |
| attack_surface | Convert scanner outputs into attack surface entries                            |
| test_plan      | Generate testing tasks from identified attack surfaces                         |

---

## 📁 Project Structure

| Directory                  | Description                   |
| -------------------------- | ----------------------------- |
| main.py                    | Entry point                   |
| config.json                | Target configuration          |
| scanners/wordpress_scan.py | WordPress detection           |
| scanners/auth_scan.py      | Authentication discovery      |
| scanners/sql_scan.py       | SQL injection reconnaissance  |
| scanners/xss_scan.py       | XSS reconnaissance            |
| workflow/attack_surface.py | Attack surface modeling       |
| workflow/test_plan.py      | Security test plan generation |

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
structured results
     ↓
JSON output
```

The framework now separates vulnerability discovery from workflow generation, allowing identified assets and entry points to be transformed into structured security testing tasks.

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

### Planned (v0.3.0)

* OWASP vulnerability classification
* Risk assessment
* Evidence collection

### Planned (Future)

* Attack chain analysis
* Remediation guidance
* Automated retesting
