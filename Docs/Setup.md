## Wazuh Basic Command 
- Check Wazuh Manager status (Debian)
```bash
sudo systemctl status wazuh-manager 
```
- Check Wazuh Agent status (Ubuntu)
```bash
sudo systemctl status wazuh-agent
```
- List connected agents (Debian)
```bash
sudo /var/ossec/bin/agent_control -l
```
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
