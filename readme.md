RPi IP Emailer
===============
This Python script gets your device's IP address and emails it to you. This is perfect for when you boot up the Pi on a network and are not sure how to connect to it initially.

Installation
------------
Download sendip.py to your Raspberry Pi and place it in your home directory. Open your rc.local file for editing:

````sh
sudo nano /etc/rc.local
````

Add python /home/pi/sendip.py as below:

````
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
  python /home/pi/sendip.py
fi
````