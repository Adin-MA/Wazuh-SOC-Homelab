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
groups = alert_json.get('rule', {}).get('groups')
rule_id= alert_json.get('rule', {}).get('id')

raw_time = alert_json.get('timestamp') or alert_json.get('@timestamp')
try: 
  dt = datetime.strptime(raw_time.split('.')[0], "%Y-%m-%dT%H:%M:%S") 
  time_str = dt.strftime("%Y-%m-%d %H:%M:%S") 
except:
  time_str = raw_time

if "bruteforce" in groups:
  src_ip = (
    alert_json.get('data', {}).get('srcip') 
    or alert_json.get('srcip') 
    or "Unknown"
  )
  
  msg = f"SSH Alert (Level {alert_level})\n\n"
  msg += f"Source IP  : {src_ip}\n"
  chat_id = "YOUR_GROUP_SSH_CHAT_ID_BOT"

elif "root" in groups:
  command = (
    alert_json.get('data', {}).get('command')
    or alert_json.get('command')
    or 'Unknown'
  )
  
  msg = f"Root Activity Alert (Level {alert_level})\n\n"
  msg += f"Command  : {command}\n"
  chat_id = "YOUR_GROUP_Root_Activity_CHAT_ID_BOT"

else:
  chat_id=""

msg += f"Agent        : {agent_name}\n"
msg += f"Rule ID      : {rule_id}\n"
msg += f"Time         : {time_str}\n"
msg += f"Description:\n{description}\n"

if rule_id == "100100": 
  msg += "\n STATUS: IP BLOCKED 1 MINUTES BY IPTABLES"
elif rule_id == "100101": 
  msg += "\n STATUS: IP BLOCKED 1 HOUR BY IPTABLES"
elif rule_id == "100102": 
  msg += "\n STATUS: IP BLOCKED PERMANENT BY IPTABLES"

payload = {
  "chat_id": chat_id,
  "text": msg,
  "parse_mode": "Markdown"
}

requests.post(hook_url, json=payload)
