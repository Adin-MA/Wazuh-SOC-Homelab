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
See [`/Architecture`](./Architecture/README.md) folder for full system diagram.

Flow:
Endpoint (Ubuntu) → Wazuh Agent → Wazuh Server (Debian) → Alerts & Log Analysis

---

## Lab Components

| Component | OS | Description |
|------------|------------|------------|
| SIEM Server | Debian 13 | Wazuh Manager for log collection, analysis, and alerting |
| Agent Endpoint | Ubuntu Server 26.04 | Log source / target machine for attack simulation |
| Attack Simulation Host | Kali Linux 1.16 | Security testing and SSH brute-force simulation |
| Virtualization Platform | VirtualBox 7.2.4 | Virtual environment for lab deployment |

---

## Key Features
- Real-time log monitoring
- SSH brute-force detection
- Automated IP blocking (active response)
- Centralized log analysis

---

## Current Status
Current Version: v1.1 (SSH Detection + Active Response)

Implemented:
- Wazuh deployment
- Agent registration
- SSH brute-force detection
- Active response blocking
- Alert monitoring

In Progress:
- Root activity monitoring

---

## Roadmap

- [ ] OpenSearch integration
- [ ] Root activity detection
- [ ] Privilege escalation detection
- [ ] File integrity monitoring

---

## Detection Scenarios

| Scenario | Status |
|-----------|---------|
| SSH Brute Force | ✅ |
| Active Response | ✅ |
| Root Activity Monitoring | 🚧 |
| Privilege Escalation | 🚧 |
| File Integrity Monitoring | ⏳ |

Detailed available in [`/Demo`](./Demo/README.md).

---

## Notes
This is a personal cybersecurity learning project for SOC/SIEM practice.
