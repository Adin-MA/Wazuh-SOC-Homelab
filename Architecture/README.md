# Architecture Overview

This SIEM lab uses Wazuh as the main security monitoring platform.

![Wazuh Architecture](Architecture-SIEM.png)

## Components
- Wazuh Server: log collection, analysis, and alerting
- Wazuh Agent: installed on monitored machine(s)

## Optional / Future Expansion
- Elasticsearch (planned)
- Kibana (planned)

## Flow
Logs from target machine → Wazuh agent → Wazuh server → detection & alerting
