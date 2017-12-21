# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 14:30
# @Author  : superman
# @FileName: setting.py
# @Software: PyCharm Community Edition
# @Blog    ：

"""
配置文件,配置交易费率字典,消费记录函数,以及日志的文件和等级等信息
"""

import sys,time,logging,datetime
sys.path.append('..')
from core import data_op,logger

date_time = time.strftime('%Y-%m-%d %H:%M:%S')

LOG_LEVEL = logging.DEBUG
LOG_TYPE = {'access':'access.log','trans':'trans.log','admin':'admin.log'}
