# 定义一个单链表类

```python
class LNode:
    def __init__(self, elem, next_=None) -> None:
        self.elem = elem
        self.next = next_

    def length(self, head):
        p, n = head, 0
        while p is not None:
            n += 1
            p = p.next
       	return n
```

## 1.添加节点

- 从头添加节点

```python
q = LNode(13)
q.next = head.next
head = q
```

- 一般位置添加节点

  ```python
  q = LNode(13)
  q.next = pre.next
  pre.next = q
  ```

## 2.删除节点

- 从头删除节点

  ```python
  head = head.next
  ```

- 一般位置删除节点

  ```python
  pre.next = pre.next.next
  ```

## 3.扫描和遍历

```python
p = head
while p is not None and i > 0:
	i -= 1
	p = p.next
```

​ p 为扫描指针，每次遍历前需要检查其是否为 None

```python
p = head
while p is not None and not pred(p.elem):
    p = p.next
```

​ **遍历**

```python
p = head
while p is not None:
    print(p.elem)
    p = p.next
```
