"""1、处理如下字符串列表，在列表中所有人名前面都加上name_，如name_alex
name=['alex','eva','cathy']"""

name=['alex','eva','cathy']
a=list(map(lambda x:"name_"+x,name))
print (a)


"""2、有如下字典数据，请使用filter及定义函数的方式，得到股票价格大于20的股票名称
Tips：filter函数可针对字典数据进行操作，使用方法类同于列表操作（第一参数传入匿名函数，可使用类似shares[x]操作，第二参数为字典数据）
shares={'IBM':36.6,'Lenovo':23.2,'AAAP':21.2,'ADM':10.2}
① filter函数
② 定义函数"""
#① filter函数
shares={'IBM':36.6,'Lenovo':23.2,'AAAP':21.2,'ADM':10.2}
b=list(filter(lambda y:shares[y]>20,shares))
print(b)
#② 定义函数???
shares={'IBM':36.6,'Lenovo':23.2,'AAAP':21.2,'ADM':10.2}
filter(lambda y:shares[y]>20,shares)
