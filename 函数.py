__author__ = 'yumyu'

#绝对值函数
print(abs(-20))

a=max(2,3,1,6)
print(a)

#数据类型转换,init()把其他类型的数据转换为整数
b=int(12.34)
print(b)

#如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-41))

#函数的参数,默认参数的设置默认参数降低了函数调用的难度,默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#可变参数/*args是可变参数，args接收的是一个tuple；**kw是关键字参数，kw接收的是一个dict。可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)