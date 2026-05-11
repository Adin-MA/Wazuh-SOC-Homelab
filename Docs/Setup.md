# Wazuh Basic Command 

## Wazuh Service Status
- Check Wazuh Manager status (Manager)
```bash
sudo systemctl status wazuh-manager 
```
- Check Wazuh Agent status (Agent)
```bash
sudo systemctl status wazuh-agent
```

---

## Wazuh Service Restart <br>

<sub>Manager (Debian)</sub>  
```bash
sudo systemctl restart wazuh-manager
```
   <sub>Agent (Ubuntu)</sub>  
```bash
sudo systemctl restart wazuh-agent
```

---

## Wazuh Agent Management
- Add New Agent (Manager)
```bash
sudo /var/ossec/bin/manage_agents
```
- Import Key Agent (Agent)
```bash
  sudo /var/ossec/bin/manage_agents
```
- List connected agents (Manager)
```bash
sudo /var/ossec/bin/agent_control -l
```
<sub>Expected Output</sub>
```bash
Active ubuntu-agent
```

---

## Wazuh Monitoring and Logs
- View real-time alerts (MOST IMPORTANT)
```bash
sudo tail -f /var/ossec/logs/alerts/alerts.log
```
- View Manager Logs
```bash
sudo tail -f /var/ossec/logs/ossec.log
```

---

## Wazuh Configuration

- Wazuh Configuration
```bash
sudo nano /var/ossec/etc/ossec.conf
```
- Wazuh Custom Rules
```bash
sudo nano /var/ossec/etc/rules/local_rules.xml
```
 
  
