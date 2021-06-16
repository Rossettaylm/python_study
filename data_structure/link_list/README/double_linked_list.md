# double linked list - 双链表

双链表增加一个引用域，可以直接访问前后结点

结点: | prev| elem | next | 

指针：| head | rear |

![double_linked_list](/home/rossetta/python_works/data_structure/link_list/pictures/double_linked_list.png)

## 1.结点操作

删除结点：

```python
p.prev.next = p.next  # 上一结点的next指向下一结点
p.next.prev = p.prev  # 下一结点的prev指向上一结点
```

## 2.双链表类

可以通过独立定义或者在LNode类的基础上派生生成

```python 
class DLNode(LNode):	# 双链表结点类
    def __init__(self, elem,  prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev
```

可以继承LList类的find、filter、printall方法，他们执行中只用next方向的引用，可以在双链表上使用。

```python
class DLList(LList1):  # 双链表类
    """双链表类
    继承了单链表类的find, filter, printall方法
    """

    def __init__(self) -> None:
        LList1.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)  # 头结点的prev是None, next指向原先的头结点
        if self._head is None:  # 空表
            self._rear = p
        else:
            p.next.prev = p  # p.next即头结点prev指向新建结点p
        self._head = p  # head指向新建结点p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)  # 尾结点的next是None, prev指向原先的尾结点
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e = self._head.elem
        self._head = self._head.next    # 删除表头元素
        if self._head is not None:      # head为空时不需要做任何事
            self._head.prev = None      # 将第一个元素的prev设为None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of DLList")
        e = self._rear.elem
        self._rear = self._rear.prev  # 删除表尾元素
        if self._rear is None:  # 删除后rear为空，证明原表中只有一个结点
            self._head = None   # 设为空表
        else:
            self._rear.next = None  # 如果表中结点大于1，将最后一个结点的next引用域设为None
        return e
```

