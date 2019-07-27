# A Simple Python Scipt Get Linux's IP Changes Noticed With ServerChan
# 一个简单的检测linux服务器IP地址更改并告知管理员的脚本

Thanks to powerdown and PPPoE redial caused IP change, sometimes your remote linux server may not reachable anymore. Though hundreds of solutions could be found via the Internet, as a admin in team R.E.W. it's much more fun to write tools myself. And after severval months I finally realized, it may be a better way to decorate my github homepage and, show my code skill in job interview in the near future.

To use getIpWithServerChan.py, you need:
- a [ServerChan](http://sc.ftqq.com/) SCKEY bind with Wechat account
- sudo chmod a+x getIpWithServerChan.py
- modify it with your servers' env such as hardware addr
- make sure that it can autorun after a few hours by using crontab in linux
- create .ip.conf in the same folder

Now your servers could jump out and shout out to you once their IP addr has changed.