# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 10:27
# @Author  : superman
# @FileName: pass_handler.py
# @Software: PyCharm Community Edition
# @Blog    ： 加密+加盐

import hashlib

def md5_pwd(pwd):
    """
    为了防止解密,hashlib.md5时加入自己的字段
    将密码转化为 md5形式
    :param pwd: 密码明文
    :return: 加密后的密码
    """
    hash = hashlib.md5(bytes('odlboy',encoding='utf8'))
    hash.update(bytes(pwd,encoding='utf8'))
    return hash.hexdigest()
    # result = hash.hexdigest()
    # return result






