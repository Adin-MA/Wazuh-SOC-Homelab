# SIEM Lab Setup With Wazuh

This project is a home lab SIEM setup using Wazuh for security monitoring and log analysis.

---

## Objective
To build a basic SIEM environment for:
- Log collection and monitoring
- Security event detection
- Simulating attack scenarios (future updates)

---

## Tools Used
- Wazuh (SIEM platform)
- Wazuh Agent (endpoint monitoring)
- Wazuh Server / Manager
- Agent Endpoint
- Virtual Lab Environment

---

## Architecture
See `/architecture` folder for full system diagram.

Flow:
Endpoint (Ubuntu) → Wazuh Agent → Wazuh Server (Debian) → Alerts & Log Analysis

---

## Wazuh Basic Command 
- Check Wazuh Manager status (Debian)
<pre>```bash
sudo systemctl status wazuh-manager 
```</pre>
- Check Wazuh Agent status (Ubuntu)
```bash
sudo systemctl status wazuh-agent
```
- List connected agents (Debian)
bash sudo /var/ossec/bin/agent_control -l
<sub>Expected Output</sub>
```bash
Active ubuntu-agent
```
- View real-time alerts (MOST IMPORTANT)
```bash
sudo tail -f /var/ossec/logs/alerts/alerts.log
```
- View Manager Logs
```bash
sudo tail -f /var/ossec/logs/ossec.log
```

- Restart Service <br>

<sub>Manager (Debian)</sub>  
```bash
sudo systemctl restart wazuh-manager
```
   <sub>Agent (Ubuntu)</sub>  
```bash
sudo systemctl restart wazuh-agent
```

---

## Current Status
🚧 Setup completed (Basic lab environment running).

Last updated: 27 April 2026

---

## Testing Simulator
Generate test events on Ubuntu:
```bash
sudo ls root
```
or failed SSH login simulation:
```bash
ssh fakeuser@localhost
```
Check alerts on debian: 
```bash
sudo tail -f /var/ossec/logs/alerts/alerts.log
```

---

## Future Improvements
- Add Elasticsearch / OpenSearch integration
- Improve visualization dashboard
- Add more detection rules

---

## Screenshots
(To be added)

---

## Notes
This is a personal cybersecurity learning project for SOC/SIEM practice.
