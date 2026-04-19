# Attacker Setup (Kali Linux VM)

## Setup

I used the Kali Linux VirtualBox image as the attacker machine. The Ubuntu install kept freezing, so switching to Kali made it easier to get a working environment quickly.

## Checking Network Connection

First, I made sure the VM had internet by running:

ping 8.8.8.8

This confirmed the VM was connected and working properly.

## Scapy

I checked if Scapy was installed and working:

python3 -c "import scapy.all as scapy; print('Scapy working')"

It was already installed on Kali though, so no extra setup was needed.

## ARP Scan

To see what devices were on the network, I ran:

sudo python3

Then inside Python:
import scapy.all as scapy
scapy.arping("10.0.2.0/24")

## Results

The scan returned a couple of devices:

* 10.0.2.2 (gateway)
* 10.0.2.3

So at this point, the attacker machine is set up and able to scan the network. This will be used next for the ARP spoofing attack.
