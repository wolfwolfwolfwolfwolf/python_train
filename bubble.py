# -*- coding:utf-8 -*-

#冒泡排序。

num = list(map(int,input("please input three number: ").split()))
temp = 0
for i in range(len(num)-1):
    for j in range(len(num)-1):
        if(num[j]>num[j+1]):
            temp = num[j+1]
            num[j+1] = num[j]
            num[j] = temp
print(num)


