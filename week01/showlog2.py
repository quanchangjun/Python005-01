#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:My
@file:showlog2.py
@time:2020/11/28
"""

import time


def showlog2():
    # 格式化日期
    log_time = time.strftime("%Y-%m-%d %X", time.localtime())
    var_date = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # print(log_time)
    # print(var_date)
    file_name = var_date+'.log'
    with open(file_name, 'a') as file:
        file.write(log_time+'\n')


if __name__ == '__main__':
    showlog2()
