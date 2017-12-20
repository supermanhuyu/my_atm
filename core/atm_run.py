 # -*- coding: utf-8 -*-
# @Time    : 2017/12/20 14:46
# @Author  : superman
# @FileName: atm_run.py
# @Software: PyCharm Community Edition
# @Blog    ：

import sys
import prettytable
import time
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
        while True:
            print('welcome')
            choice = input('plz input your choice : ')
            if choice == "q" :
                logout()
            elif choice.isdigit() == True and int(choice) < 7  :
                menu[int(choice)](username)
            else :
                pass
    else :
        pass

if __name__ == '__main__' :
    main()


