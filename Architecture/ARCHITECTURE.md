# Architecture Overview

This SIEM lab uses Wazuh as the main security monitoring platform.

## Architecture Diagram

The following diagram illustrates the current SIEM lab architecture and communication flow between components.

![Wazuh Architecture](../Assets/Architecture/Architecture.png)

## Components

- Wazuh Manager (Debian): log collection, analysis, alerting, and active response
- Wazuh Agent (Ubuntu Server): monitored endpoint and log source
- Kali Linux: attack simulation host used for security testing

## Future Expansion

- OpenSearch (planned)
- OpenSearch Dashboards (planned)

## Flow

```bash
Attack Simulation (Kali Linux)
→ Ubuntu Endpoint
→ Wazuh Agent
→ Wazuh Manager
→ Detection & Correlation
→ Active Response (IP Blocking)
→ Telegram Notification
```
