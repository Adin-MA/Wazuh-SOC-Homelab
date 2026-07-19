# Basic Command Wazuh and IP Tables
Basic Command for using Wazuh and IP Tables

---

## Wazuh Service Status
- Check Wazuh Manager status
```bash
sudo systemctl status wazuh-manager 
```
- Check Wazuh Agent status 
```bash
sudo systemctl status wazuh-agent
```

---

## Wazuh Service Restart <br>

- Restart Wazuh Manager   
```bash
sudo systemctl restart wazuh-manager
```
- Restart Wazuh Agent  
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
- List Connected Agents (Manager)
```bash
sudo /var/ossec/bin/agent_control -l
```
<sub>Expected Output</sub>
```bash
Active ubuntu-agent
```

---

## Wazuh Monitoring and Logs
- View Real-time Alerts

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

- Wazuh Integration Telegram

```bash
sudo nano /var/ossec/integrations/custom-telegrams
```

---

## Wazuh Validation & Testing

- Validate Wazuh configuration and rule syntax

```bash
sudo /var/ossec/bin/wazuh-analysisd -t
```

- Test log decoding and rule matching

```bash
sudo /var/ossec/bin/wazuh-logtest
```

---

## IP Tables Basic Command

### - Check IP Blocked by IP Tables

```bash
sudo iptables -L -n
```
