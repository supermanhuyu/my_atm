# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 16:39
# @Author  : superman
# @FileName: format_num.py
# @Software: PyCharm Community Edition
# @Blog    ：

def format_num(value) :
    """
    将金额转化为人民币模式，带逗号分隔，保留小数点两位，四舍五入
    :param value:
    :return:
    """
    return '{:,.2f}'.format(value)
