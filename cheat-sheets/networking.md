# Networking Quick Reference

## Common protocols
| Protocol | Common port | Purpose |
|---|---:|---|
| DNS | 53 TCP/UDP | Domain name system queries |
| DHCP | 67/68 UDP | Dynamic IPv4 configuration |
| HTTP | 80 TCP | Web traffic without transport encryption |
| HTTPS | 443 TCP (commonly) | HTTP protected by TLS |
| SSH | 22 TCP | Secure remote administration |
| SMTP | 25 TCP | Mail transfer between servers |
| NTP | 123 UDP | Time synchronization |
| RDP | 3389 TCP/UDP | Remote Desktop |

Ports are conventions, not proof of which service is running. Services can use non-default ports.

## Address concepts
- IPv4 loopback: `127.0.0.1`
- IPv6 loopback: `::1`
- IPv4 private ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`
- Link-local IPv4: `169.254.0.0/16`
- Default gateway: next hop used when no more specific route applies.

## Troubleshooting sequence
1. Check local interface configuration.
2. Check route and gateway.
3. Check name resolution.
4. Check service reachability only for systems you are authorized to access.
5. Compare expected and observed behavior; record timestamps and errors.

## Key distinctions
- TCP provides a reliable ordered byte stream.
- UDP provides datagrams without TCP's delivery guarantees.
- DNS resolves names and stores multiple record types.
- TLS protects data in transit but does not make endpoints trustworthy.
