# Mitigation

There are a few ways to reduce or prevent ARP spoofing attacks on a network.

## Static ARP Entries

One method is using static ARP entries instead of dynamic ones.

Normally, devices automatically accept ARP replies and update their ARP tables. Static entries manually bind an IP address to a specific MAC address so fake ARP replies are ignored.

Example:

```bash
arp -s 10.0.2.2 00:11:22:33:44:55
```

This helps prevent a victim machine from accepting a spoofed gateway MAC address.

The downside is that static entries are harder to manage on large networks.

## HTTPS

HTTPS encrypts traffic between the client and the server.

Even if an attacker successfully redirects traffic through their machine, encrypted HTTPS traffic is much harder to read or modify.

Without HTTPS, sensitive information like usernames and passwords could potentially be captured in plain text.

## VPNs

VPNs add another layer of encryption to network traffic.

With a VPN enabled, intercepted traffic is usually unreadable because the data is encrypted before leaving the machine.

This does not stop ARP spoofing itself, but it makes the captured traffic much less useful to an attacker.

## Dynamic ARP Inspection

Some managed switches support Dynamic ARP Inspection (DAI).

DAI checks ARP packets on the network and blocks fake or suspicious ARP replies before they reach other devices.

This is commonly used in enterprise environments to help prevent MITM attacks.

## Network Segmentation

ARP spoofing normally only works on devices connected to the same local network.

Separating systems into different VLANs or subnetworks can reduce exposure by limiting which devices can communicate directly.

## Monitoring Tools

Network monitoring tools can help detect suspicious ARP activity.

Some commonly used tools include:

- Wireshark
- arpwatch
- IDS/IPS systems

Signs of ARP spoofing can include:

- Unexpected MAC address changes
- Duplicate ARP replies
- High amounts of ARP traffic

## Restoring the Network

The script restores the original ARP mappings when stopped with `CTRL + C`.

This helps return communication between the victim and gateway back to normal after the test finishes.