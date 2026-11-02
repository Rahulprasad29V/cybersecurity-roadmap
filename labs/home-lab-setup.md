# Home Lab Setup

## Goal
Create a small, isolated environment for learning operating systems, networking, monitoring and application security.

## Planning
1. Check hardware capacity, disk space and host OS compatibility.
2. Select a reputable hypervisor and read its documentation.
3. Create an isolated virtual network; do not expose vulnerable VMs to the internet.
4. Install a general-purpose Linux VM.
5. Add a Windows evaluation/lab VM only where licensing permits.
6. Add an intentionally vulnerable training application such as OWASP Juice Shop.
7. Snapshot clean installations before experiments.

## Operational safety
- Update the host and hypervisor.
- Use unique lab-only passwords; never reuse work or personal credentials.
- Disable shared folders and clipboard integration when unnecessary.
- Take snapshots and revert after experiments.
- Never upload sensitive host data into a lab.
- Keep vulnerable services private and isolated.

## Lab record
Record date, VM name, purpose, network mode, snapshot name and cleanup steps. Do not publish serial numbers, license keys or private network details.
