#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/25 14:06
# Author  :ZhengChengBin
# File    :emailTest.py

from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import ConfigParser
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


cp = ConfigParser.SafeConfigParser()
cp.read('myapp.conf')
from_add = cp.get('email', '163user')
from_pwd = cp.get('email', '163pwd')
to_add = cp.get('email', 'qquser')
hostname = cp.get('email', '163SMTP')

# 必要信息必须填99%,否则会报错554
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_add)
msg['To'] = _format_addr(u'管理员 <%s>' % to_add)

server = smtplib.SMTP_SSL(hostname)
server.set_debuglevel(1)
server.login(from_add, from_pwd)  # 密码必须是特别授权的密码，不是原来的密码
server.sendmail(from_add, [to_add], msg.as_string())
server.quit()

print 'success'


