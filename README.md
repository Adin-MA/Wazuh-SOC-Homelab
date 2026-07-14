# SIEM Lab Setup With Wazuh
A hands-on SIEM lab built with Wazuh for log monitoring, threat detection, attack simulation, and automated incident response.

---

## Objective
To build a hands-on SIEM lab environment for:
- Log collection and centralized monitoring
- Custom security event detection
- Active response automation
- Attack simulation and analysis
- Linux auditing with Auditd
- Risk-based event correlation

---

## Architecture
This project follows a centralized SIEM architecture using Wazuh for log collection, detection, and automated response.

Full technical diagram and flow: [`/Architecture`](./Architecture/ARCHITECTURE.md)

---

## Repository Structure
| Directory | Purpose |
|------------|------------|
| [`/Architecture`](./Architecture/ARCHITECTURE.md) | SIEM Architecture diagrams and technical flow |
| [`/Assets`](./Assets) | Images and screenshots used in documentation |
| [`/Config`](./Config) | Wazuh rules and configuration files |
| [`/Demo`](./Demo) | Attack simulation and detection demonstrations |
| [`/Docs`](./Docs/DOCS.md) | Frequently used commands for setup, monitoring, testing, and troubleshooting  |
| [`/Scripts`](./Scripts/custom-telegram.py) | Telegram integration and automation scripts |

---

## Security Response Flow
``` bash
🚨 Attack Simulation (Kali Linux)
→ Endpoint (Ubuntu Server)
→ Wazuh Agent
→ Wazuh Manager (Debian)
→ Detection Engine (Rule + Threshold)
→ Alert Generation
→ Active Response (IP Blocking)
→ Telegram Notification
```

---

## Lab Components
| Component | OS | Description |
|------------|------------|------------|
| SIEM Server | Debian 13 | Wazuh Manager for log collection, analysis, and alerting |
| Agent Endpoint | Ubuntu Server 26.04 | Log source / target machine for attack simulation |
| Attack Simulation Host | Kali Linux 2025.4 | Security testing and SSH brute-force simulation |
| Virtualization Platform | VirtualBox 7.2.4 | Virtual environment for lab deployment |

---

## Key Capabilities
- 📡 Real-time log ingestion from endpoint machines
- 🧠 Threshold-based SSH brute-force detection (event correlation over time window to reduce false positives)
- ⚡ Automated incident response via Active Response (IP blocking)
- 📊 Centralized security event monitoring and analysis
- 📩 Telegram-based security alert notifications
  
---

## Project Overview
| Item | Count |
|------|-------|
| Custom Rules Wazuh | 6 |
| Log Sources | 2 |
| Detection Scenarios | 2 |
| Active Response Workflow | 1 |
| Notification Integration | 1 (Telegram) |

---

## Current Status
Current Version: **v2.4** (Repository Restructure & Documentation Improvements) 🚀

---

## What's New in v2.4
- Reorganized the repository structure for improved readability and maintainability.
- Split demonstration documentation into separate files for each detection scenario.
- Restructured the Config directory by separating Manager, Agent, and Auditd configurations.
- Added an Auditd configuration directory for upcoming Linux auditing integration.
- Improved repository navigation and documentation consistency.

---

## Implemented:
- Wazuh deployment and configuration
- Agent registration
- SSH brute-force detection
- Active response (automatic IP blocking)
- Real-time alert monitoring
- Telegram alert integration
- Custom root activity detection for privileged shell execution
- Custom Wazuh rule development and testing

---

## In Progress
- Risk-based privilege escalation detection
- SQLite-based risk scoring engine
- Auditd integration for Linux auditing
- Context-aware event correlation
- Risk-based automated response
  
---

## Future Improvements
- Log visualization with OpenSearch Dashboards
- File Integrity Monitoring (FIM)
- Detection coverage expansion for additional attack techniques
- MITRE ATT&CK mapping for custom detection rules
- Enhanced threat hunting capabilities
  
---

## Detection Scenarios
| Scenario | Status | Demo |
|-----------|---------|---------|
| SSH Brute Force | ✅ | [`/SSH_DEMO.md`](/Demo/SSH_DEMO.md) |
| Root Activity Monitoring | ✅ | [`/ROOT_ACTIVITY_MONITORING.md`](/Demo/ROOT_ACTIVITY_MONITORING.md) |
| Privilege Escalation | 🚧 | Coming Soon |
| File Integrity Monitoring | ⏳ | Coming Soon |

---

## Notes
This is a personal cybersecurity learning project focused on SIEM engineering, detection engineering, and SOC analyst practices using Wazuh.
