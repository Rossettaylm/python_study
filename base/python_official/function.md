# funtion
## 实参列表位置  
```python
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
        .............
```

## 任意实参列表  
```python
    def concat(*args, sep="/"):
        return sep.join(args)
```

---------------
## 解包实参列表  
函数调用要求独立的位置参数，但实参在列表或元组里时，要执行相反的操作。例如，内置的 range() 函数要求独立的 start 和 stop 实参。如果这些参数不是独立的，则要在调用函数时，用 * 操作符把实参从列表或元组解包出来：  
```python 
    >>> list(range(3, 6))            # normal call with separate arguments
    [3, 4, 5]
    >>> args = [3, 6]
    >>> list(range(*args))            # call with arguments unpacked from a list
    [3, 4, 5]
```
同样的， 字典可以用**操作符传递关键字操作数    
```python  
    def parrot(voltage, state='a stiff', action='voom'):
        print(voltage, state, action)

    # 解包字典d，将其key：value传入parrot
    d = {'voltage': 1, 'state': 2, 'action': 3}
    parrot(**d)
```

--------------
## Lambda表达式  
lambda 关键字用于创建小巧的匿名函数。lambda a, b: a+b 函数返回两个参数的和。Lambda 函数可用于任何需要函数对象的地方。在语法上，匿名函数只能是单个表达式。在语义上，它只是常规函数定义的语法糖。与嵌套函数定义一样，lambda 函数可以引用包含作用域中的变量：  
```python  
>>>  def make_incrementor(n):
        return lambda x: x + n  

>>>  f = make_incrementor(42)  
>>> f(0)  
42  
>>> f(1)
43  
```

## 函数注解  
标注以字典的形式存放在函数的 __annotations__ 属性中，并且不会影响函数的任何其他部分。 形参标注的定义方式是在形参名后加冒号，后面跟一个表达式，该表达式会被作为值为标注的值。 返回值标注的定义方式是加组合符号 ->，后面跟一个表达式，该标注位于形参列表和表示 def 语句结束的冒号之间。 下面的示例有一个必须的参数，一个可选的关键字参数以及返回值都带有相应的标注:   
```python 
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```
