# yay.com-dns-update
DNS Update Script for yay.com

This script checks your current external IP address and if there is a change since it updates either an A or CNAME entry from yay.com
It runs every minute and it creates a file to write the last updated IP to.

If you want to use my script you need to install some packages.

Requirements:

UBUNTU/DEBIAN

sudo apt install curl tail python3 python3-pip

After that run

sudo pip install requests

Not finished
