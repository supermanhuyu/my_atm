# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 17:24
# @Author  : superman
# @FileName: terminal_transfers.py
# @Software: PyCharm Community Edition
# @Blog    ：转账模块




import sys
sys.path.append('..')
from core import data_op,format_num,verification_code
from conf.setting import *
from core.logger import *

def transfers(username) :
    """
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
    print('您的可用转账额度为:{}'.format(format_num.format_num(able_wd_amount)))
    t_user_name = input('请输入您要转入的账户名称:')
    if user_data.get(t_user_name)==None:
        print('本银行无此账户信息,请核实信息后再进行转账...')
    else:
        # 转账操作
        for i in range(4) :
            if i == 3 :
                print('输入错误格式超过三次，退出！')
                break
            amount_inp = input('请输入转账额度：')
            if amount_inp.isdigit() :
                amount = int(amount_inp)
                if amount > able_wd_amount :
                    print('最高转账额度为{},已超支,'
                          '退出操作!'.format(format_num.format_num(able_wd_amount)))
                    log_trans.info('{}转账操作失败'.format(username))
                    break
                else :
                    # 如不超支,转账,先验证码验证
                    res = verification_code.check_veri()
                    if res :
                        user_data[username][3] -= amount
                        user_data[username][3] -= amount * trans_rate['转账']
                        user_data[t_user_name][3] += amount
                        data_op.flush_db(user_data)
                        print('现可消费额度为:'
                              '{}'.format(format_num.format_num(user_data[username][3])))
                        # record(args, '转账', '终端机', amount)
                        # record(t_user_name, '收款', args, amount)
                        log_trans.info('{}向{}成功转账{}'.format(username, t_user_name, amount))
                        break
                    else:
                        print('验证失败!转账操作失败!!')
                        log_trans.info('{}向{}转账失败'.format(username,t_user_name))
                        break
            else:
                i+=1
                print('输入格式错误,还有{}次机会'.format(3 - i))