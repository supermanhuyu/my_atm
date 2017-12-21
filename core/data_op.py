# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 17:27
# @Author  : superman
# @FileName: data_op.py
# @Software: PyCharm Community Edition
# @Blog    ：数据操作模块

import json
# import chardet

def load():
    """
    读 atm 用户数据库   ,encoding="utf-8"
    """
    # with open("../db/atm_cart_db.json", "r") as f:
    #     print(f)
    user_data=json.load(open('../db/atm_cart_db.json','r'))
    return user_data

def flush_db(user_data) :
    """
    写入 ATM用户数据
    :param args:  新的用户数据
    :return:  True
    """
    json.dump(user_data,open("../db/atm_cart_db.json","w"),ensure_ascii=False,indent=1)
    return True
