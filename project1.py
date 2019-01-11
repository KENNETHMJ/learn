#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime

#时间相关函数

T = '2018-12-25'
def time_control():
    time1 = datetime.datetime.now().strftime('%Y-%m-%d')
    time2 = T
    d1 = datetime.datetime.strptime(time1,'%Y-%m-%d')
    d2 = datetime.datetime.strptime(time2,'%Y-%m-%d')
    delta = d1 - d2
    if delta.days < 3 or delta.days > 7:
        return 'no %s days' % delta.days
    else:
        return 'yes %s days' %delta.days


a = time_control()
print(a)