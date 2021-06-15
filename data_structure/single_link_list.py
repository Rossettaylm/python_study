#!/home/rossetta/miniconda3/envs/dl/bin/python
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


if __name__ == "__main__":
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

    def pop_last(self):
        if self._head == None:  # 空表
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next == None:  # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    def for_each(self, proc):
        """链表的遍历
        """
        p = self._head
        while p is not None:
            proc(p.elem)  # proc应该是可以作用于表元素的操作函数，它将被作用于每个表元素。
            p = p.next

    def elements(self):
        """定义一个生成器，遍历功能
        """
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self, pred):
        """通过yield定义一个生成器，返回所有
        符合条件的值
        """
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next


if __name__ == "__main__":
    mlist1 = LList()
    for i in range(10):
        mlist1.append(i)
    #  mlist1.printall()

    #  mlist1.for_each(print)

    #  # 使用迭代器遍历链表
    #  for x in mlist1.elements():
    #  print(x)
    for value in mlist1.filter(lambda y: y % 2 == 0):
        print(value)

