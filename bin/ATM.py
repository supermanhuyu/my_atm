# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 10:25
# @Author  : superman
# @FileName: ATM.py
# @Software: PyCharm Community Edition
# @Blog    ：


import sys
sys.path.append("..")
from core import atm_run

if len(sys.argv) == 2 and sys.argv[1] == "start" :
    atm_run.main()
else:
    print(r"python atm.py start to start up programe")







