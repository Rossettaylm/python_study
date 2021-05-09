<!-- TOC GFM -->

+ [标题](#标题)
+ [一级标题](#一级标题)
    * [二级标题](#二级标题)
+ [111](#111)
    * [222](#222)
        - [333](#333)
            + [444](#444)
                * [555](#555)
                    - [666](#666)
+ [换行](#换行)
+ [字体](#字体)
+ [分隔线](#分隔线)
+ [删除线](#删除线)
+ [下划线](#下划线)
+ [脚注](#脚注)
+ [无序列表](#无序列表)
+ [有序列表](#有序列表)
+ [列表嵌套](#列表嵌套)
+ [区块嵌套](#区块嵌套)
+ [区块中使用列表](#区块中使用列表)
+ [列表中使用区块](#列表中使用区块)
+ [代码表示](#代码表示)
+ [链接表示](#链接表示)
        - [高级链接](#高级链接)
+ [图片表示](#图片表示)
+ [表格表示](#表格表示)

<!-- /TOC -->

---

# 标题

# 一级标题

## 二级标题

# 111

## 222

### 333

#### 444

##### 555

###### 666

# 换行

两个空格换行  
空一行换行

# 字体

_斜体文本_  
_斜体文本_  
**粗体文本**  
**粗体文本**  
**_粗斜体文本_**  
**_粗斜体文本_**

# 分隔线

你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：

---

---

---

---

---

---

# 删除线

GOOGLE.COM  
~~BAIDU.COM~~  
google.com

# 下划线

<u>开始>>>结束</u>  
<u>带下划线文本</u>

# 脚注

This is a footnote.[^rossetta]  
[^rossetta]: thenameofme~

# 无序列表

使用\*、+、-来作为列表标记，标记后应添加空格

- first

* second

- last

# 有序列表

使用数字加上小数点

1. first
2. second
3. third

# 列表嵌套

在子列表的选项前添加四个空格

1. first
   - first[1]
   - first[2]
2. second
   - second[1]
   - second[2]

# 区块嵌套

> 最外层
>
> > 第一层嵌套
> >
> > > 第二层嵌套

# 区块中使用列表

> 区块中使用列表
>
> 1. 第一项
> 2. 第二项
>
> - 第一项
> - 第二项
>
> * 第三项
>
> - 第四项

# 列表中使用区块

- first
  > yangliaoming  
  > queshi
- second

# 代码表示

1. 用反引号表示

`print()`

2. 用三个反引号表示, 指定一种语言（可选）

```python
    for value in range(1,11):
        print(value)
```

# 链接表示

- [链接名称](链接地址)  
  [google](https://www.google.com)
- <链接地址>  
  <https://www.google.com>

### 高级链接

变量 1 为网址变量  
[Google][1]

# 图片表示

![photo](a photo address)  
![RUNOOB 图标](https://static.runoob.com/images/runoob-logo.png)  
<img src="https://static.runoob.com/images/runoob-logo.png" width="50%">

同高级链接，这个链接用 2 作为网址变量
然后在文档的结尾为变量赋值 （网址）  
[RUNOOB][2].

# 表格表示

用|来分隔不同的单元格， 用-----来分隔表头和其他行  
| title1 | title2 |
| ------ | ------ |
| cell1 | cell2 |
| cell11 | cell22 |

| 左对齐 | 右对齐 | 居中对齐 |
| :----- | -----: | :------: |
| cell   |   cell |   cell   |
| cell   |   cell |   cell   |
| cell   |   cell |   cell   |

[1]: https://www.google.com
[2]: https://static.runoob.com/images/runoob-logo.png
