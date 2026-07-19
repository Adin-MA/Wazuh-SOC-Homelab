# Basic Command Auditd
Basic Command for using Auditd

---

## Auditd Service
- Check Auditd Service Status
```bash
sudo systemctl status auditd 
```
- Restart Auditd Service
```bash
sudo systemctl restart auditd
```

---

## Auditd Configuration
- Audit Custom Rules
```bash
sudo nano /etc/audit/rules.d/audit.rules
```

---

## Auditd Rules Management

- List All Active Rules
```bash
sudo auditctl -l
```
- Delete All Active Rules
```bash
sudo auditctl -D
```

---

## Auditd Log Analysis
- Search Logs by Key
```bash
sudo ausearcj -k <audit_key> 
```
