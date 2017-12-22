# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 14:30
# @Author  : superman
# @FileName: setting.py
# @Software: PyCharm Community Edition
# @Blog    ：

"""
配置文件,配置交易费率字典,消费记录函数,以及日志的文件和等级等信息
"""

import sys,time,logging
# import datetime
sys.path.append('..')
from core import data_op
# from core import logger

date_time = time.strftime('%Y-%m-%d %H:%M:%S')

def record(user_name,TransType,business,amounts):
    user_data=data_op.load()
    rates=trans_rate[TransType]*amounts
    user_data[user_name][4].append({date_time:[TransType,business,amounts,rates]})
    data_op.flush_db(user_data)
    return True

#利息计算
trans_rate={'提现':0.05,'转账':0.05,'还款':0,'支付':0,'收款':0}

LOG_LEVEL = logging.DEBUG
LOG_TYPE = {'access':'access.log','trans':'trans.log','admin':'admin.log'}
