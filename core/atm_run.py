 # -*- coding: utf-8 -*-
# @Time    : 2017/12/20 14:46
# @Author  : superman
# @FileName: atm_run.py
# @Software: PyCharm Community Edition
# @Blog    ：

import sys
import prettytable
import time
sys.path.append('..')
from core import terminal_op
from core import terminal_repay,terminal_show_record,terminal_transfers,terminal_view_credit,\
    terminal_withdraw,terminal_discover_bills,terminal_bill_rate

def logout():
    exit('系统推出')

menu = [terminal_view_credit.view_credit,
        terminal_show_record.show_record,
        terminal_repay.repay,
        terminal_withdraw.withdraw,
        terminal_transfers.transfers,
        terminal_discover_bills.inqure_bills,
        terminal_bill_rate.inqure_rates,
        logout]



def main():
    """
    先登录，返回true的时候进入主菜单
    :return:
    """
    username = "superman"
    result = terminal_op.login()
    if result :
        row = prettytable.PrettyTable()
        row.field_names = ['查看可用额度','查看消费记录','还款','提现','转账','查询本月账单','还款逾期查询','退出']
        row.add_row([0,1,2,3,4,5,6,'q&quit'])
        print('\033[31;1m欢迎来到superman支行\033[0m'.center(93, '*'))
        while True:
            # print("\n")
            print(row)
            choice = input('请选择对应的操作序号：')
            if choice == "q" :
                logout()
            elif choice.isdigit() == True and int(choice) < 7  :
                menu[int(choice)](username)
            else :
                print('\033[31;1m您的输入有误，请重新输入\033[0m')
    else :
        pass

if __name__ == '__main__' :
    main()


