# SIEM Lab Setup With Wazuh
A hands-on SIEM laboratory built with Wazuh for centralized log monitoring, custom threat detection, Linux auditing, attack simulation, and automated incident response.

---

## Objective
To build a hands-on SIEM lab environment for:
- Log collection and centralized monitoring
- Custom security event detection
- Active response automation
- Attack simulation and analysis
- Linux auditing with Auditd

---

## Architecture
This project follows a centralized SIEM architecture where Wazuh collects logs from monitored Linux endpoints, analyzes security events using built-in and custom detection rules, executes automated active responses, and sends real-time alerts through Telegram for incident monitoring.

![Wazuh Architecture](Assets/Architecture/Architecture.png)

---

## Security Response Flow
``` bash
Attack Simulation
→ Endpoint
→ Wazuh Agent
→ Wazuh Manager
→ Detection Engine
→ Alert Generation
→ Active Response
→ Telegram Notification
```

---

## Lab Environment
| Component | Platform | Description |
|-----------|----------|-------------|
| SIEM Server | Debian 13 + Wazuh | Centralized log collection, analysis, and alerting |
| Agent Endpoint | Ubuntu Server 26.04 | Monitored endpoint for log collection and attack simulation |
| Attack Host | Kali Linux 2025.4 | Security testing and attack simulation |
| Virtualization | VirtualBox 7.2.4 | Virtual lab environment |

---

## Detection Scenarios
| Scenario | Status | Demo |
|-----------|---------|---------|
| SSH Brute Force | ✅ | [`SSH Brute Force Demo`](/Demo/SSH_DEMO.md) |
| Root Activity | ✅ | [`Root Activity Demo`](/Demo/ROOT_ACTIVITY.md) |
| Privilege Escalation | ✅ | [`Privilege Escalation Demo`](/Demo/PRIVILEGE_ESCALATION.md) |
| File Integrity Monitoring | 🚧 | Coming Soon |

---

## Detection Features
| Feature | Status | Description |
|---------|:------:|-------------|
| Threshold-based Detection | ✅ | Detect repeated security events within a defined time window |
| Custom Wazuh Rules | ✅ | Custom detection logic for Linux security events |
| Active Response | ✅ | Automatic IP blocking using Wazuh |
| Telegram Notifications | ✅ | Real-time alert delivery |
| Auditd Integration | ✅ | Linux auditing for privileged activity |
| Event Correlation | ⏳ | Correlate multiple security events into a single incident |
| Threat Scoring Engine | ⏳ | Assign risk scores to detected activities |
| Risk-Based Response | ⏳ | Automated response based on accumulated threat score |

---

## Project Overview
| Item | Value | Description |
|------|------:|-------------|
| Custom Wazuh Rules | 13 | Custom detection rules developed for the lab |
| Log Sources | 3 | Journald, `/var/log/auth.log`, and Auditd logs |
| Detection Scenarios | 3 | SSH brute-force, root activity, and privilege escalation detection |
| Active Response | IP Blocking | Automatic IP blocking using Wazuh Active Response |
| Automation | Python | Custom integration and automation scripts |
| Threat Scoring Database | SQLite (Planned) | Threat scoring and event tracking |


---

## Repository Structure
| Directory | Purpose |
|------------|------------|
| [`/Assets`](./Assets) | Images and screenshots used in documentation |
| [`/Config`](./Config) | Wazuh rules and configuration files |
| [`/Demo`](./Demo) | Attack simulation and detection demonstrations |
| [`/Docs`](./Docs/DOCS.md) | Frequently used commands for setup, monitoring, testing, and troubleshooting  |
| [`/Scripts`](./Scripts/custom-telegram.py) | Custom automation and integration scripts |

---

## Current Status
Current Version: **v3.0** (Privilege Escalation Detection & Auditd Integration)

**Highlights**
- Privilege Escalation Detection
- Auditd Integration
- 13 Custom Wazuh Rules

---

## What's New in v3.0
- Added privilege escalation detection using custom Wazuh rules.
- Integrated Auditd as an additional Linux audit log source.
- Expanded detection scenarios to include privileged activity monitoring.
- Improved detection logic for Linux security events.
- Reorganized the repository structure and documentation.

---

## In Progress
- Auditd event filtering and noise reduction
- SQLite-based risk scoring engine
- Context-aware event correlation
- Risk-based automated response

---

## Future Improvements
- MITRE ATT&CK mapping for custom detection rules
- File Integrity Monitoring (FIM)
- Log visualization with OpenSearch Dashboards
- Detection coverage expansion for additional attack techniques
- Enhanced threat hunting capabilities
  
---

## Project Roadmap
| Version | Focus | Status |
|---------|-------|:------:|
| v1.x | Wazuh deployment, basic monitoring, SSH brute-force detection, and Active Response | ✅ |
| v2.x | Telegram notification integration and Root Activity monitoring | ✅ |
| v3.0 | Privilege Escalation detection and Auditd integration | ✅ |
| v3.1 | Auditd event filtering and Threat Scoring Engine | 🚧 |
| v3.2 | Context-aware Event Correlation and Risk-Based Response | ⏳ |
| v4.0 | File Integrity Monitoring (FIM) and MITRE ATT&CK mapping | ⏳ |

---

## Notes
This is a personal cybersecurity learning project focused on SIEM engineering, detection engineering, and SOC analyst practices using Wazuh.
