import sys
import json
import requests
from datetime import datetime

alert_file = open(sys.argv[1])
hook_url = sys.argv[3]

alert_json = json.loads(alert_file.read())
alert_file.close()

alert_level = alert_json.get('rule', {}).get('level', 'Unknown')
description = alert_json.get('rule', {}).get('description', 'Unknown')
agent_name = alert_json.get('agent', {}).get('name', 'Unknown')
rule_id = alert_json.get('rule', {}).get('id', 'Unknown')
groups = alert_json.get('rule', {}).get('groups', [])

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
        or 'Unknown'
    )

    msg = f"*SSH Wazuh Alert (Level {alert_level})*\n\n"
    msg += f"*Source IP  :* {src_ip}\n"
    chat_id = "YOUR_GROUP_SSH_CHAT_ID_BOT"

elif "monitoring" in groups:
    msg = f"Root Activity Wazuh Alert (Level {alert_level})\n\n"

    if "root" in groups:
        command = (
            alert_json.get('data', {}).get('command')
            or alert_json.get('command')
            or 'Unknown'
        )

        tty = (
            alert_json.get('data', {}).get('tty')
            or alert_json.get('tty')
            or 'Unknown'
        )

        pwd = (
            alert_json.get('data', {}).get('pwd')
            or alert_json.get('pwd')
            or 'Unknown'
       )

        msg += f"*Command :* {command}\n"
        msg += f"*TTY            :* {tty}\n"
        msg += f"*PWD           :* {pwd}\n"

    elif "audit" in groups:
        command = (
            alert_json.get('data', {}).get('audit', {}).get('command')
            or alert_json.get('data', {}).get('command')
            or alert_json.get('command')
            or 'Unknown'
        )

        if rule_id in ["100301", "100302", "100303", "100304"] and command in ["useradd", "userdel", "adduser"]:
            sys.exit(0)

        auid = (
            alert_json.get('data', {}).get('audit', {}).get('auid')
            or alert_json.get('data', {}).get('auid')
            or alert_json.get('auid')
            or 'Unknown'
        )

        tty = (
           alert_json.get('data', {}).get('audit', {}).get('tty')
           or alert_json.get('data', {}).get('tty')
           or alert_json.get('tty')
           or 'Unknown'
        )
        syscall = alert_json.get('data', {}).get('audit', {}).get('syscall')
        msg += f"*SYSCALL: {syscall}*"
        msg += f"*AUID          :* {auid}\n"
        msg += f"*Command :* {command}\n"
        msg += f"*TTY            :* {tty}\n"

    else:
        sys.exit(0)

    chat_id = "YOUR_GROUP_ROOT_ACTIVITY_CHAT_ID_BOT"

else:
    sys.exit(0)

msg += f"*Agent         :* {agent_name}\n"
msg += f"*Rule ID       :* {rule_id}\n"
msg += f"*Time           :* {time_str}\n\n"
msg += f"*Description:*\n{description}\n"

if "L1" in description:
    msg += "\n*STATUS:*\nIP BLOCKED 1 MINUTES BY IPTABLES"
elif "L2" in description:
    msg += "\n*STATUS:*\nIP BLOCKED 1 HOUR BY IPTABLES"
elif "L3" in description:
    msg += "\n*STATUS:*\nIP BLOCKED PERMANENT BY IPTABLES"

payload = {
           "chat_id": chat_id,
           "text": msg,
           "parse_mode": "Markdown"
}

requests.post(hook_url, json=payload, timeout=5)
