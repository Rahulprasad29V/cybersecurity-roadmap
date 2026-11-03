# Labs and Practice Platforms

Practise in intentionally vulnerable applications, CTFs, local VMs and platform-provided targets. Read each platform's rules before interacting with any target.

## Recommended environments
| Platform | Good for | Official link |
|---|---|---|
| OverTheWire | Linux and command-line fundamentals | https://overthewire.org/wargames/ |
| TryHackMe | Guided cybersecurity learning | https://tryhackme.com/ |
| Hack The Box | Hands-on labs and CTF practice | https://www.hackthebox.com/ |
| PortSwigger Web Security Academy | Web application security | https://portswigger.net/web-security |
| OWASP Juice Shop | Local intentionally vulnerable web app | https://owasp.org/www-project-juice-shop/ |
| picoCTF | Beginner CTF challenges | https://picoctf.org/ |
| CyberDefenders | Blue-team and DFIR practice | https://cyberdefenders.org/ |
| Blue Team Labs Online | Defensive security scenarios | https://blueteamlabs.online/ |

Availability, pricing, features and rules can change. Confirm details on the official site.

## Lab safety checklist
- [ ] I own the environment or have explicit authorization.
- [ ] The target and activity are within written scope.
- [ ] The lab is isolated from sensitive or production systems.
- [ ] A VM snapshot or backup exists.
- [ ] No real credentials or personal data are used.
- [ ] I understand the activity's potential impact.
- [ ] I will stop if scope or safety is uncertain.

## Suggested home lab
Use a supported hypervisor, one general-purpose Linux VM, an optional Windows evaluation/lab VM where licensing permits, an isolated virtual network, an intentionally vulnerable local training app, and snapshots. Do not bridge vulnerable targets onto a network you do not control. Keep lab-only passwords unique and never reuse work or personal credentials.


## Guided exercises
The detailed [lab catalog](catalog.md) links to guided exercises for:
- [Packet review](exercises/packet-review.md)
- [Synthetic log triage](exercises/log-triage.md)
- [File integrity verification](exercises/file-integrity.md)
- [Local web security review](exercises/web-security-review.md)
- [Cloud configuration review](exercises/cloud-review.md)

Use the reusable [lab exercise template](lab-exercise-template.md) when proposing a new activity.
