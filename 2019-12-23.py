'''用循环语句和列表生成式两种方法，将[3,4,2,5]和[6,8,4,2,9,1,5]中各个元素相乘后，存到列表中，再对列表求均值
L1 = [3,4,2,5]
L2 = [6,8,4,2,9,1,5]
2019-12-24未明学院作业
'''
#① 列表生成式方法
L1 = [3,4,2,5]
L2 = [6,8,4,2,9,1,5]
s =[i*j for i in L1 for j in L2]
print(s)
import numpy as np
m=np.mean(s)
print("平均值为：%d" % m)
#② 循环语句方法

L1 = [3,4,2,5]
L2 = [6,8,4,2,9,1,5]
L3=[]
for a in L1:
    for b in L2:
        L3.append(a*b)
print(L3)
import numpy as np
m=np.mean(L3)
print("平均值为：%d" % m)
sdjajjhakjhsadlkh
