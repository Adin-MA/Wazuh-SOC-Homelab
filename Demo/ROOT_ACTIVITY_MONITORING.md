# Root Activity Monitoring

## 📌 Scenario
A privileged shell execution was simulated on the monitored Ubuntu agent using `sudo` commands.

## 🎯 Attack Method
The following commands were executed to simulate root-level activity:

```bash
sudo su
sudo sh
sudo bash
```

<p align="left">
 <img src="../Assets/Demo/Root-Activity/Commands/Root-Commands.png" width="600"/>
</p>

## 🛡️ Detection
A custom Wazuh rule monitors successful `sudo` executions and detects privileged shell commands.
Detected commands include:
- `sudo su`
- `sudo sh`
- `sudo bash`

## ⚡ Response
- Custom Wazuh rule triggered
- High-severity alert generated
- Alert forwarded to Telegram
- Command execution details included in the notification

## 📸 Evidence

### 1. Root activity detected in Wazuh (`alerts.log`)
Detection generated after executing privileged shell commands.

<p align="left">
 <img src="../Assets/Demo/Root-Activity/Wazuh-Alert/Wazuh-Su-Alert.png" width="600"/>
</p>
<p align="left">
 <img src="../Assets/Demo/Root-Activity/Wazuh-Alert/Wazuh-Sh-Alert.png" width="600"/>
</p>
<p align="left">
 <img src="../Assets/Demo/Root-Activity/Wazuh-Alert/Wazuh-Bash-Alert.png" width="600"/>
</p>

### 2. Telegram Alert Notification
Telegram notification generated after privileged shell execution was detected by the custom Wazuh rule.

<p align="left">
 <img src="../Assets/Demo/Root-Activity/Telegram-Alert/Telegram-Su-Alert.png" width="300"/>
 <img src="../Assets/Demo/Root-Activity/Telegram-Alert/Telegram-Sh-Alert.png" width="300"/>
 <img src="../Assets/Demo/Root-Activity/Telegram-Alert/Telegram-Bash-Alert.png" width="300"/>
</p>
