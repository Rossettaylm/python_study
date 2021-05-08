# 列表详解

- list.append(x)
- list.extend(iterable)
- list.insert(index, x)
- list.remove(x)
- list.pop(i)
- list.clear()
- list.index(x, start, end)
- list.count(x)
- list.sort(\*, key=None, reverse=False)
- list.reverse()
- list.copy()

## 列表实现堆栈

```python
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)
    stack.pop()
```

## 列表实现队列

```python
    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    queue.popleft()
    queue.pop()
    print(queue)
```

## 列表推导式

`squares = [x**2 for x in range(10)]`

**将两个列表中不相等的元素结合起来**  
`[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]`

**等价于**

```python
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
```

**列表解析的嵌套**

```python
    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    a = [num for elem in vec for num in elem]
    print(a)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
