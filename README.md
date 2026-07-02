# SIEM Lab Setup With Wazuh

A hands-on SIEM lab built with Wazuh for log monitoring, threat detection, attack simulation, and automated incident response.

---

## Objective

To build a SIEM lab environment for:
- Log collection and monitoring
- Security event detection
- Active response automation
- Attack simulation and analysis

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
| [`/Demo`](./Demo/DEMO.md) | Attack simulation and detection demonstrations |
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

## Current Status

Current Version: **v2.3** (SSH Detection + Active Response + Root Activity Monitoring + Telegram Improvements) 🚀

---

## What's New in v2.3
- Added custom root activity detection rules for (`sudo su`, `sudo sh`. and `sudo bash`)
- Improved custom Wazuh rule logic for privileged command monitoring.
- Enhanced Telegram alert integration with structured notifications for root activity events.
- Added command context to alerts, including executed command, TTY, agent information, rule ID, and timestamp.
- Reduced unrelated Telegram notifications by refining rule filtering.
- Validated custom detection rules using wazuh-logtest and real attack simulations.
- Improved root activity monitoring reliability through custom rule tuning and event validation.

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

## In Progress:

- Privilege escalation detection using custom Wazuh rules
- Severity classification based on privileged command execution
- Context-aware alert classification to reduce false positives
- Detection coverage expansion for additional post-exploitation techniques
  
---

## Future Improvements

- Log visualization with OpenSearch Dashboards
- File Integrity Monitoring (FIM)
- Expanded privilege escalation detection
- MITRE ATT&CK mapping for custom detection rules
  
---

## Detection Scenarios

| Scenario | Status |
|-----------|---------|
| SSH Brute Force | ✅ |
| Active Response | ✅ |
| Root Activity Monitoring | ✅ |
| Privilege Escalation | 🚧 |
| File Integrity Monitoring | ⏳ |

Each scenario includes detection logic, alert behavior, and response actions. Full details available in [`/Demo`](./Demo/DEMO.md).

---

## Notes
This is a personal cybersecurity learning project for SOC/SIEM practice.
