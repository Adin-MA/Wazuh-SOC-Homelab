# SIEM Lab Setup With Wazuh

A hands-on SIEM lab built with Wazuh for log monitoring, threat detection, attack simulation, and automated incident response..

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
| Attack Simulation Host | Kali Linux 1.16 | Security testing and SSH brute-force simulation |
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
Current Version: v2.0 (SSH Detection + Active Response + Telegram Alerts) 🚀

Implemented:
- Wazuh deployment
- Agent registration
- SSH brute-force detection
- Active response blocking
- Alert monitoring

In Progress:
- Root activity monitoring

---

## Future Improvements

- Log visualization layer (OpenSearch / OpenSearch Dashboards)
- Root access monitoring (sudo / privileged command abuse detection)
- Privilege escalation detection (unauthorized permission or role changes)
- File Integrity Monitoring (critical system file change tracking)
- MITRE ATT&CK mapping for detection rules and alerts
  
---

## Detection Scenarios

| Scenario | Status |
|-----------|---------|
| SSH Brute Force | ✅ |
| Active Response | ✅ |
| Root Activity Monitoring | 🚧 |
| Privilege Escalation | 🚧 |
| File Integrity Monitoring | ⏳ |

Each scenario includes detection logic, alert behavior, and response actions. Full details available in [`/Demo`](./Demo/DEMO.md).

---

## Notes
This is a personal cybersecurity learning project for SOC/SIEM practice.
