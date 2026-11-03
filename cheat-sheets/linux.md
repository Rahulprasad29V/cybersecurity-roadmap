# Linux Quick Reference

Use a disposable VM while learning. Exact commands and output vary by distribution.

| Task | Common command |
|---|---|
| Current directory | `pwd` |
| List files | `ls -la` |
| Show file text | `cat file.txt` |
| Search text | `grep -n "pattern" file.txt` |
| Find files | `find ./lab -type f` |
| Disk space | `df -h` |
| Memory summary | `free -h` |
| Current processes | `ps aux` |
| Service status (systemd) | `systemctl status SERVICE` |
| Recent journal entries | `journalctl -n 50` |
| File permissions | `stat file.txt` |
| SHA-256 digest | `sha256sum file.txt` |

## Permission reminder
- Read: inspect file contents or list a directory.
- Write: modify a file or directory entries.
- Execute: run a file or traverse a directory, subject to other controls.
- Prefer least privilege. Avoid running unknown scripts or commands as root.
- Do not copy commands blindly; read the relevant manual page first.
