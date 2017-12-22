# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 17:22
# @Author  : superman
# @FileName: terminal_repay.py
# @Software: PyCharm Community Edition
# @Blog    ：还款操作模块

import sys
sys.path.append('..')
from core import data_op,format_num
from conf.setting import *
from core.logger import *

def repay(username):
    """
    还款函数
    :param username:
    :return:
    """

    user_data = data_op.load()
    #如果还款额度大于等于信用额度，提示无需还款
    if user_data[username][3] >= user_data[username][2] :
        print('没有消费，就不用还款 ^_^ !!!')
    else :
        #计算还款额度
        need_repay = user_data[username][2] - user_data[username][3]
        print('你所需还款金额为：\033[31;1m{}\033[m'.format(format_num.format_num(need_repay)))
        while True :
            input_num = input('请输入还款金额：')
            if input_num.isdigit() :
                amount = int(input_num)
                # 判断如果大于需还款金额,用户选择
                if amount > need_repay :
                    inp = input('有钱人，你的还款大于所需还款金额，是否继续？'
                          '\033[32;1m 回车 或 Y 继续，back 或 b 为返回 \033[m:')
                    if len(inp) == 0 or inp.lower() == 'y' :
                        # 修改用户账户信息
                        user_data[username][3] += amount
                        data_op.flush_db(user_data)
                        print('有钱人还多了...还款完成!,目前可用信用金额为'
                              '\033[31;1m{}\033[m'.format(format_num.format_num(user_data[username][3])))
                        # record(username, '还款', '终端机', amount)
                        # log_trans.info('{}成功还款{}'.format(username, amount))
                        break
                    else :
                        break
                else :
                    # 修改用户账户信息
                    user_data[username][3] += amount
                    data_op.flush_db(user_data)
                    print('还款完成!,目前可用信用金额为'
                          '\033[31;1m{}\033[m'.format(format_num.format_num(user_data[username][3])))
                    # record(username, '还款', '终端机', amount)
                    # log_trans.info('{}成功还款{}'.format(username, amount))
                    break
            else :
                print('输入有误,请重新输入.')









