# ARP Spoofing

## Overview

For this part of the project, I implemented a basic ARP spoofing attack using Python and Scapy. The goal was to simulate how an attacker can position themselves between a victim and a gateway by sending fake ARP responses.

## How it works

ARP does not verify who sends replies, so a machine can send false information and other devices will trust it. The script takes advantage of this by repeatedly sending ARP packets to both the target and the gateway.

This makes each side believe that the attacker’s machine is the other device.

## Implementation

The script:

* gets the MAC address of a target IP
* sends spoofed ARP replies
* continuously repeats this to maintain the attack
* restores the network when stopped

## Testing

The script was run in a Kali Linux virtual machine. Since the network was using NAT (10.0.2.x), only virtual devices were visible.

Even though a full man-in-the-middle attack could not be demonstrated yet, the script successfully sent spoofed ARP packets continuously.

## Results

The script ran without errors and printed "Packets sent..." repeatedly, confirming that ARP spoofing packets were being transmitted. (I added a screenshot named "packetssent.png" for reference)

## Next Steps

To fully demonstrate the attack, a second virtual machine (victim) will be added and the network will be switched to a bridged adapter. This will allow actual traffic interception to be observed.
