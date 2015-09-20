__author__ = 'yumyu'
# 构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现：
L = []
n = 1
while n <= 99:
    L.append(n)
    n += 2

# list tuple 字符串切片操作 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:2])
print((0, 1, 2, 3, 4, 5)[:3])
print('ABCDEFG'[:3])

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
    # 如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

for ch in 'ABC':
    print(ch)

    #下标循环迭代
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)