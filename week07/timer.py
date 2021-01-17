#!/usr/bin/python
# _*_ coding: UTF-8 -*_
"""
@author:quanchangjun
@file:timer.py.py
@time:2021/01/17
功能：实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""

import time


def timer(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        print(f'total {time.time() - start_time}')
        return ret

    return inner


@timer
def foo(n):
    # 休眠2秒，执行装饰器函数后，统计foo函数执行耗时
    time.sleep(n)


if __name__ == '__main__':
    foo(2)
