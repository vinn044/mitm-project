victim vm setup guide

what you'll need:
virtualbox 7.2 installed
ubuntu 24.04.2 live server ARM64 ISO (based on personal device)

part 1:
open virtualbox and click "new"

name: victim-ubuntu
ISO image: ubuntu-24.04.2-live-server-arm64.iso
type: linux
version: ubuntu(64 bit)

uncheck "procceed with unattended installation", click next

virtual hardware setup:
base memory: 2048 MB
number of CPUs: 2
disk size: 20 GB

click next and finish

display setup:
go to settings -> display
set video memory to 128 MB
click ok

newtwork adapter setup:
we use NAT during installation and package setup so the vm has access to the internet, 
then we switch back to Internal Network for the actual demo.
go to setttings
click the expert tab
scroll to network -> adapter 1
see attached to: NAT
click ok

part 2: 
start the vm (double-click vitctim-ubuntu)
it will boot into a text-based installer

if you see "no bootable option found", 
press any key to enter the UEFI boot manager -> boot manager -> select CD-ROM entry
also go back to virtualbox manager and check settings -> system -> motherboard
make sure 'Hard Disk' is checked and at the top of boot order

installation type:
back to the text-based installer (black screen, orange header bar)
you'll see that ubuntu server is already selected, press enter

network configuration: 
when on NAT, the network auto-configures, press enter on done

proxy configuration: 
leave blank. done -> enter

mirror configuration:
the mirror test may fail or be slow...
press enter on done and if a "mirror check failes" popup appears -> select continue
the popup may appear several times, always select continue

guided storage configuration:
storage with the 20 GB disk is already selected. done -> enter twice

a "confirm destructive action" popup appears -> select continue

profile configuration:
your name: Victim User
your servers name: victim-vm
pick a username: victim
choose a password: victim123
confirm your password: victim123

done -> enter

skip ubuntu pro setup for now -> continue 

ssh configuration:
leave 'install openssh server' unchecked
done -> enter

.....wait for installation, 5-10 min.....
....when done the header says "installation complete"
select reboot now -> enter

when prompted "please remove the installation medium, then press enter" just press enter

part 3:
after reboot youll see the GRUB bootloader window with Ubuntu highlighted press Enter
or wait for it to auto-boot

at the login prompt, enter username: victim, password: victim123

you then should see: victim@victim-vm:~$

part 4:
install required packages, this is where the vm must be on NAT to work
install packages one at a time:
sudo apt install -y python3
sudo apt install -y curl

then install scapy (adding --no-install-recommends avoids pulling 400+ MB dependencies):
sudo apt install -y python3-scapy --no-install-recommends
(if this stall or shows 404 errors retry 3 attempts or try: sudo apt-get install -y python3-scapy --fix-missing)

verify everything is installed:
python3 --version
python3 -c "import scapy; print('scapy ok')"
curl --version

expected output:
Python 3.12.3
scapy ok
curl 8.5.0 ...

part 5: (still on NAT)
clone repo. 

if git clone fails ("could not resolve host"), restart the network interface:
sudo ip link set enp0s8 down
sudo ip link set enp0s8 up
sudo dhcpcd enp0s8

wait till you see -> enp0s8: offered 10.0.2.15 -> then clone:
cd ~
git clone https://github.com/vinn044/mitm-project.git

part 6:
switch back to internal network:
settings -> expert tab -> network -> adapter 1
set attatched to: internal network
set name: labnet
click ok

set the static ip inside the vm: 
sudo nano /etc/netplan/50-cloud-init.yaml

replace the contents with:
network:
  version: 2
  ethernets:
    enp0s8:
      addresses:
        - 192.168.56.101/24
      routes:
        - to: default
          via: 192.168.56.1
      nameservers:
        addresses: [8.8.8.8]

save ctrl+X -> Y -> enter, then apply:
sudo netplan apply

verify:
ip addr show
you should see inet 192.168.56.101/24 under enp0s8







