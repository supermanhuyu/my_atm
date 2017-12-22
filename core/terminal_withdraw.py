# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 17:26
# @Author  : superman
# @FileName: terminal_withdraw.py
# @Software: PyCharm Community Edition
# @Blog    ：终端取现模块


import sys
sys.path.append('..')
from core import data_op,format_num
from conf.setting import *
from core.logger import *

def withdraw(username) :
    """
    提现函数，与转账模块基本一致，但无需验证目标用户，金额有所变动
    :param username:
    :return:
    """

    user_data = data_op.load()
    #剩余可用额度
    able_amount = user_data[username][3]
    # 标准可转账额度 = 标准可用额度 / 2
    max_amount = user_data[username][2]/2
    if able_amount >= max_amount :
        able_wd_amount = max_amount
    else:
        able_wd_amount = able_amount
    print('您的可用提现额度为:{}'.format(format_num.format_num(able_wd_amount)))
    for i in range(4) :
        if i == 3 :
            print('输入错误格式超过三次，退出！')
            break
        amount_inp = input('请输入提现额度：')
        if amount_inp.isdigit() :
            amount = int(amount_inp)
            if amount > able_wd_amount :
                print('最高取现额度为{},已超支,'
                      '退出操作!'.format(format_num.format_num(able_wd_amount)))
                log_trans.info('{}提现操作失败'.format(username))
                break
            else :
                user_data[username][3] -= amount
                user_data[username][3] -= amount * trans_rate['提现']
                data_op.flush_db(user_data)
                print('现可消费额度为:'
                      '{}'.format(format_num.format_num(user_data[username][3])))
                # record(args, '提现', '终端机', amount)
                log_trans.info('{}提现成功'.format(username))
                break
        else:
            i+=1
            print('输入格式错误,还有{}次机会'.format(3 - i))