# 双向链表支持两端的高效操作，但每个结点都需增加一个链接域
# 结点: prev | elem | next
# 头指针：head | rear
from random import randint
from single_linked_list import LinkedListUnderflow, LList1, LNode


class DLNode(LNode): # 双链表结点类
    def __init__(self, elem, prev=None, next_=None) -> None:
        LNode.__init__(self, elem, next_)
        self.prev = prev


class DLList(LList1): # 双链表类
    """双链表类
    继承了单链表类的find, filter, printall方法
    """
    def __init__(self) -> None:
        LList1.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head) # 头结点的prev是None, next指向原先的头结点
        if self._head is None: # 空表
            self._rear = p
        else:
            p.next.prev = p # p.next即头结点prev指向新建结点p
        self._head = p # head指向新建结点p

    def append(self, elem):
        p = DLNode(elem, self._rear, None) # 尾结点的next是None, prev指向原先的尾结点
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e = self._head.elem
        self._head = self._head.next # 删除表头元素
        if self._head is not None: # head为空时不需要做任何事
            self._head.prev = None # 将第一个元素的prev设为None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of DLList")
        e = self._rear.elem
        self._rear = self._rear.prev # 删除表尾元素
        if self._rear is None: # 删除后rear为空，证明原表中只有一个结点
            self._head = None # 设为空表
        else:
            self._rear.next = None # 如果表中结点大于1，将最后一个结点的next引用域设为None
        return e

    def length(self):
        len = 0
        p = self._head
        if p is None:
            return len
        len += 1
        while p.next is not None:
            p = p.next
            len += 1
        return len

    def reverse(self):
        i, j = 0, self.length() - 1
        p, q = self._head, self._rear
        while i < j:
            p.elem, q.elem = q.elem, p.elem
            p, q = p.next, q.prev
            i, j = i + 1, j - 1


list1 = DLList()
for value in range(10):
    list1.append(value)

list1.printall()
print(list1.length())
list1.reverse()
list1.printall()
