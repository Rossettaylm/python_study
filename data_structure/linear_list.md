# ADT of LIST

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
