# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 17:23
# @Author  : superman
# @FileName: terminal_show_record.py
# @Software: PyCharm Community Edition
# @Blog    ：查看消费记录
import prettytable,sys
from core import data_op

def show_record(user_name):
    """
    user_data = data_op.load()
    :param user_name:
    :return:
    """
    user_data = data_op.load()
    records = user_data[user_name][4]
    if len(records) == 0:
        print(" no record !")
    else:
        row = prettytable.PrettyTable()
        row.field_names = ['时间','交易','商家','交易金额','利息']
        for item in records :
            for record in item :
                row.add_row([record,item[record][0],item[record][1],
                             item[record][2],item[record][3]])
        print(row)
    # print("show_record"+"_"+username)
