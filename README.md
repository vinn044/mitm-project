# MITM Project

Simple ARP spoofing / MITM project made in Python using Scapy.  
Tested in a VM lab using Kali Linux and Ubuntu in VirtualBox.

The goal of the project was to understand how ARP poisoning works and how traffic can be redirected through another machine on a local network.

---

# Running the Script

Run the script with:

```bash
sudo python3 arpspoofer.py
```

Example output:

```bash
Packets sent...
Packets sent...
Packets sent...
```

Press `CTRL + C` to stop the attack and restore the ARP tables.

---

# What the Script Does

The script:

- Finds MAC addresses on the network
- Sends spoofed ARP replies to the victim
- Sends spoofed ARP replies to the router
- Redirects traffic through the attacker machine
- Restores the network when stopped

---

# Files

mitm-project/
├── arpspoofer.py
├── mitigation.md
├── attacker_setup.md
├── victim_setup.md
├── router_setup.md
└── README.md
