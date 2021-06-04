def fib(n):
    f0, f1 = 1, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f0


print(fib(10))
