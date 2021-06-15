# data structure

It's a data-structure note.

---

**ADT （抽象数据类型)**

## ADT of LIST

| method                | # 一个表抽象数据类型                                |
| :-------------------- | :-------------------------------------------------- |
| List(self)            | # 表构造操作，创建一个新表                          |
| is_empty(self)        | # 判断 self 是否为一个空列表                        |
| len(self)             | # 获得 self 的长度                                  |
| prepend(self, elem)   | # 将元素 elem 加入表中作为第一个元素                |
| append(self, elem)    | # 将元素 elem 加入表中作为最后一个元素              |
| insert(self, elem, i) | # 将 elem 加入表中作为第 i 个元素，其他元素顺序不变 |
| del_first(self)       | # 删除表中的首元素                                  |
| del_last(self)        | # 删除表中的尾元素                                  |
| del(self, i)          | # 删除表中的第 i 个元素                             |
| search(self, elem)    | # 查找元素 elem 在表中出现的位置                    |
| forall(self, op)      | # 对表中的每个元素执行操作 op                       |

## 通过时间复杂度和空间复杂度来进行算法分析

### O(g(n))表示法

**当 n 趋向于无穷大时从小到大依次为**  
O(log(n)), O(n), O(nlog(n)), O(n^2), O(n^3), O(2^n)

---

> 1. 基本操作：认为其时间复杂度为 O(1)，如果是函数调用，则  
>    将其时间复杂度带入整体计算
> 2. 加法规则：如果算法是两个部分的顺序复合，其复杂度是这  
>    两部分的复杂性之和

        O(T1(n)) + O(T2(n)) = O(max(T1(n), T2(n)))

> 3. 乘法规则：如果算法是一个循环，循环体执行 T1(n)次，且  
>    每次执行需要 T2(n)的时间，那么：

        O(T1(n) * O(T2(n))) = O(T1(n) * T2(n))

> 4. 取最大规则：如果算法是条件分支，两个分支的时间复杂性  
>    分别为 T1(n)和 T2(n),则有：  
>    当 n 趋向于无穷大时

        T(n) = O(max(T1(n), T2(n)))
