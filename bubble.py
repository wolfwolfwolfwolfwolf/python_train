# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
#输入三个整数x,y,z，请把这三个数由小到大输出。

num = list(map(int,input("please input three number: ").split()))
temp = 0
for i in range(len(num)-1):
    for j in range(len(num)-1):
        if(num[j]>num[j+1]):
            temp = num[j+1]
            num[j+1] = num[j]
            num[j] = temp
print(num)


