from random import randint

#!/home/rossetta/miniconda3/envs/dl/bin/python
# 在一个非空的线性表里，存在着唯一一个首元素和唯一的一个尾元素。除首元素之外，表中的每个元素e
# 都仅有一个前驱元素；除尾元素之外，表中的每个元素都仅有一个后继元素。

# 自定义异常


class LinkedListUnderflow(ValueError):
    pass


class LNode:
    """定义一个节点类"""

    def __init__(self, elem, next_=None) -> None:
        self.elem = elem
        self.next = next_


#  if __name__ == "__main__":
#  llist1 = LNode(1)
#  p = llist1
#  for i in range(2, 11):
#  p.next = LNode(i)
#  p = p.next

#  p = llist1
#  # while p:
#  while p is not None:
#  print(p.elem)
#  p = p.next


class LList:
    """定义一个单链表类"""

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

    def find(self, pred):  # 穿入的pred为函数，可用lambda表示
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

    def rev(self):
        """将链表的首端结点取下加入一个新链表，最后通过head指向它
        """
        p = None
        while self._head is not None:  # 当链表非空时
            q = self._head     # 取首结点赋给q
            self._head = q.next  # head指向第二结点
            q.next = p  # 新取下来的结点加在新链表的前面, 最末的结点next为None
            p = q       # 将p设为前端待插入的结点
        self._head = p  # 最终令head指向p，即首结点


def list_sort(lst):
    """插入排序
    """
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = x


#  if __name__ == "__main__":
#  mlist1 = LList()
#  for i in range(10):
#  mlist1.append(i)
#  #  mlist1.printall()

#  #  mlist1.for_each(print)

#  #  # 使用迭代器遍历链表
#  #  for x in mlist1.elements():
#  #  print(x)
#  for value in mlist1.filter(lambda y: y % 2 == 0):
#  print(value)

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
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


#  if __name__ == "__main__":
#  mlist1 = LList1()
#  mlist1.prepend(99)
#  for i in range(11, 20):
#  mlist1.append(randint(1, 20))

#  for x in mlist1.filter(lambda y: y % 2 == 0): # 遍历mlist1中的偶数
#  print(x)

# 单链表的常见变形为循环单链表，其中最后一个节点的next域
# 不用None，而是指向表的第一个节点。

# 当只有rear指向表尾时，循环单链表支持O(1)的表头/表尾插入和
# O(1)的表头删除


class LCList:
    """循环单链表类"""

    def __init__(self) -> None:
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p  # 建立一个节点的循环
            self._rear = p
        else:
            p.next = self._rear.next  # 将p指向头结点
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next  # p指向第一个节点
        if self._rear is p:  # 只有一个节点时
            self._rear = None
        else:
            self._rear.next = p.next  # 删除第一个节点
        return p.elem

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop_last of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
            return p.elem
        else:
            while p.next is not self._rear:
                p = p.next
            e = p.next.elem
            p.next = self._rear.next
            self._rear = p
            return e

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            if p is not self._rear:
                print(p.elem, end=', ')
            else:
                print(p.elem)
                break
            p = p.next


# if __name__ == "__main__":
    #circlist = LCList()
    # for value in range(10):
        #circlist.append(randint(1, 10))

    # circlist.printall()
    #print('The first elements:' + str(circlist.pop()))
    # circlist.printall()
    #print('The last elements:' + str(circlist.pop_last()))
    # circlist.printall()
