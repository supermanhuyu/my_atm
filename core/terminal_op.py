# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 16:50
# @Author  : superman
# @FileName: terminal_op.py
# @Software: PyCharm Community Edition
# @Blog    ：

from core import data_op
from core import pass_handler

tip = {'user_name': None,'login_state':False}

def freeze_count(user_name):
    user_data = data_op.load()
    user_data[user_name][0] = 0
    data_op.flush_db(user_data)

def login() :
    user_data = data_op.load()
    user_name = input('请输入用户名：')
    if user_data[user_name][0] == None :
        print('{}账户错误,请重新输入..'.format(user_name))
    elif user_data[user_name][0] == 0 :
        print('您的账户{}已被冻结,请联系管理员'.format(user_name))
        return False
    else :
        i = 0
        while i < 4 :
            if i == 3 :
                freeze_count(user_name)
                print('您的账户{}已被冻结,请联系管理员'.format(user_name))
                return False
            pwd_input= input('请输入{}的密码：'.format(user_name))
            pwd = pass_handler.md5_pwd(pwd_input)
            if pwd == user_data[user_name][1] :
                tip['user_name'] = user_name
                tip['login_state'] = True
                print('登录成功!')
                return  True
            else :
                print('密码输入有误,请重新输入.')
                i += 1

if __name__ == '__main__':
    login()
