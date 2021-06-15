from random import randint

import single_link_list as sl  # type: ignore
from single_link_list import LinkedListUnderflow  # type: ignore

LList = sl.LList
LNode = sl.LNode


class LList1(LList):
    """链表头不仅有head也有rear，指向表尾"""

    def __init__(self) -> None:
        super().__init__()
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:  # 空表
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:  # 只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:  # 循环直到倒数第二个
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


if __name__ == "__main__":
    mlist1 = LList1()
    mlist1.prepend(99)
    for i in range(11, 20):
        mlist1.append(randint(1, 20))

    for x in mlist1.filter(lambda y: y % 2 == 0):  # 遍历mlist1中的偶数
        print(x)
