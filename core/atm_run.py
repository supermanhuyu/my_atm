 # -*- coding: utf-8 -*-
# @Time    : 2017/12/20 14:46
# @Author  : superman
# @FileName: atm_run.py
# @Software: PyCharm Community Edition
# @Blog    ：

import sys
import prettytable
import time
from core import terminal_op

def main():
    """
    先登录，返回true的时候进入主菜单
    :return:
    """

    result = terminal_op.login()
    if result :
        while True:
            print('welcome')
            choice = input('plz input your choice : ')

    else :
        pass

if __name__ == '__main__' :
    main()


