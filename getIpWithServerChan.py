#!/home/rinabell/anaconda3/bin/python
# -*- coding: utf-8 -*-
# by rinabell @190419

import os
import requests
from datetime import datetime
import socket, struct, fcntl
key = ' '	# INPUT YOUR SCKEY HERE

# get last boot up days
day1 = datetime(2019, 4, 19)	# input your date, BE NOTICE here applies form  
	# of YYYY-MM-DD bcz its chinese tradition
day2 = datetime.now()
interval = day2 - day1
title = "%s days ipaddr report"%(interval.days)
url = "https://sc.ftqq.com/%s.send"%(key)	# server-chan web address

# get ip address now
def getIp(ipAd):
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, \
		 struct.pack('256s', bytes(ipAd[:15], 'utf-8')))[20:24])
newIp = getIp('ppp0')	
# ATTENTION HERE INPUT YOUR OWN HARDWARE ADDRESS SUCH AS 'etho0/lo/pp0'
# find it by 'ifconfig' in terminal

# save ip address to compare in case of poweroff
with open('.ip.conf','r+') as f:
	oldIp = f.read(15).strip()	# notice that len(oldIp) may be 14 or 15
	if oldIp != newIp:
		f.truncate(0)
		f.write(newIp)
		ip = "now ipaddr is %s"%(newIp)
		# talk with server-chan
		payload = {'text': title, 'desp': ip}
		requests.post(url, params = payload)




