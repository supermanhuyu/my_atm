# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 17:25
# @Author  : superman
# @FileName: terminal_view_credit.py
# @Software: PyCharm Community Edition
# @Blog    ：查看消费记录模块

import sys
from core import data_op,format_num
sys.path.append('..')

def view_credit(user_name):
    """
    查看用户信息，加载数据，并将相关数据显示至屏幕
    :param user_name:
    :return:
    """
    user_data = data_op.load()
    if user_data[user_name][0] == None :
        print(" no such user !")
    else :
        # balance = user_data[username][3]
        balance = format_num.format_num(user_data[user_name][3])
        credit = format_num.format_num(user_data[user_name][2])
        print('你的信用额度为:\033[31;1m{}\033[0m,'
              '目前可用额度为:\033[31;1m{}\033[0m'.format(credit,balance))
