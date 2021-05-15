###############################################################
# File Name: function.py
# =============================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-
##############################################################

def parrot(voltage, state='a stiff', action='voom'):
    """
    解包测试
    """
    print(voltage, state, action)


d = {'voltage': 1, 'state': 2, 'action': 3}
# 解包字典d，将其key：value传入parrot
parrot(**d)
