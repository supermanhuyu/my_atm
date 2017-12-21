# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 17:27
# @Author  : superman
# @FileName: logger.py
# @Software: PyCharm Community Edition
# @Blog    ：日志记录模块

import sys
import logging
from conf.setting import *

def logger(log_type):
    """
    定义日志模块
    :param log_type: 日志的用户
    :return:
    """
    logger=logging.getLogger(log_type)
    logger.setLevel(LOG_LEVEL)

    ch=logging.StreamHandler()
    ch.setLevel(LOG_LEVEL)

    fh=logging.FileHandler('../log/{}'.format(LOG_TYPE[log_type]))
    fh.setLevel(LOG_LEVEL)

    formatter=logging.Formatter('%(asctime)s - %(name)s -'
                                ' %(levelname)s - %(message)s')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

#将日志实例化,防止进入循环后多次刷新日志
log_trans=logger('trans')
log_access=logger('access')
log_admin=logger('admin')