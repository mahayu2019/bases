#!/usr/bin/env python
# coding=utf-8

'''
初识线程
'''

import time
import threading


def work_one():
    print('1号工人')


def work_two():
    print('2号工人')


if __name__ == '__main__':
    t = threading.Thread(target=work_one())
    t.start()
