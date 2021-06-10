# 在一个非空的线性表里，存在着唯一一个首元素和唯一的一个尾元素。除首元素之外，表中的每个元素e
# 都仅有一个前驱元素；除尾元素之外，表中的每个元素都仅有一个后继元素。


# 自定义异常
class LinkedListUnderflow(ValueError):
    pass


# 定义一个单链表类
class LNode:
    def __init__(self, elem, next_=None) -> None:
        self.elem = elem
        self.next = next_

    def length(self, head):
        """求表的长度"""
        p, n = head, 0
        while p is not None:
            n += 1
            p = p.next
        return n


llist1 = LNode(1)
p = llist1
for i in range(2, 11):
    p.next = LNode(i)
    p = p.next

p = llist1
# while p:
while p is not None:
    print(p.elem)
    p = p.next


class LList:
    def __init__(self) -> None:
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
