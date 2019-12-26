"""1、定义一个函数，以此来判断输入字符串的长度是否大于10
如果字符串大于10，显示“该字符串长度大于10”，并返回为True；否则显示“该字符串长度小于等于10”，并返回False"""
def long (i):
    if len(i)>10:
        print('“该字符串长度大于10”')
        return True
    else:
        print('“该字符串长度小于等于10”')
        return False
x=input("请输入字符串：")
long (x) 

"""2、定义一个i求解阶乘的函数，输入一个整数，即可得到n!=1x2x3…(n-1)xn
如传入参数5，得到结果为120（即1x2x3x4x5=120）"""
def f (n):
    m=1
    if n<=1:
        if n==0 or n==1:
            return 1
    else:
        for x in range(1,n+1):
            m *=x
    return m
a= int(input('请输入一个整数：'))
print(f(a))

