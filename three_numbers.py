# -*- coding:utf-8 -*-

#输入三个整数x,y,z，请把这三个数由小到大输出。

raw = []

for i in range(3):
    x = int(input('int%d: ' %(i)))
    raw.append(x)
print(sorted(raw))