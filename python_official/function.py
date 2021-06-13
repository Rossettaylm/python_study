def parrot(voltage, state='a stiff', action='voom'):
    """
    解包测试
    """
    print(voltage, state, action)


d = {'voltage': 1, 'state': 2, 'action': 3}
# 解包字典d，将其key：value传入parrot
parrot(**d)

#  def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#           |             |                  |
#           |        Positional or keyword   |
#           |                                - Keyword only
#           -- Positional only
