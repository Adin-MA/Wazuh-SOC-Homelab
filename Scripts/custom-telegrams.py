import sys
import json
import requests
from datetime import datetime

alert_file = open(sys.argv[1])
hook_url = sys.argv[3]

alert_json = json.loads(alert_file.read())
alert_file.close()

alert_level = alert_json.get('rule', {}).get('level')
description = alert_json.get('rule', {}).get('description')
agent_name = alert_json.get('agent', {}).get('name')
rule_id= alert_json.get('rule', {}).get('id')

raw_time = alert_json.get('timestamp') or alert_json.get('@timestamp')
try: 
  dt = datetime.strptime(raw_time.split('.')[0], "%Y-%m-%dT%H:%M:%S") 
  time_str = dt.strftime("%Y-%m-%d %H:%M:%S") 
except:
  time_str = raw_time

src_ip = (
  alert_json.get('data', {}).get('srcip') 
  or alert_json.get('srcip') 
  or "Unknown"
)

msg = f"A Wazuh Alert (Level {alert_level})\n\n"
msg += f" Agent: (agent_name}\n"
msg += "IP: {}\n".format(src_ip) msg += f"+Time: {time_str}\n"
msg += f"Description: (description}\n"

if description == "SSH Brute Force detection": 
msg += "\n STATUS: IP BLOCKED BY IPTABLES"

chat_id = "YOUR_CHAT_ID_BOT"

payload = {
  "chat_id": chat_id,
  "text": msg,
  "parse_mode": "Markdown"
}

requests.post(hook_url, json=payload)
