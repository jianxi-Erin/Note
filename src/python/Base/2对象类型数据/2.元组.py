'''
1 元组的定义
  t=( , , )
        ()里面可以存放任何数据类型，‘，’隔开个元素的序列,其中每一个元素的数据类型没有限制

'''
t=(1,'a',None,True,1.3)
print(t)
print(type(t))
t1=(1,'a',None,True,1.3,t)
print(t1)
print(type(t1))
t2=()
print(t2)

'''2.元组的长度（len）,,不管这个元素有多复杂，他都只是一个元素'''
print(len(t))
print(len(t1))
'''3 元世祖中的元素的访问
    索引
        正序
        逆序
        切片
'''
print(t1)
print(t1[5])
print(t1[::-1])

'''
    4.元组的拼接
    4.1'+'
        t+t1  把前后两个数组里的元素按顺序取出，组成新的元素
    4.2 “*”
    t*n  把元组里面的元素取出来放入新的元组，重复n次
'''

t2=t+t1
print(t2)

'''
    5 元组一经定义，其中元素不可更新，只读    
'''
# t[1]=2  TypeError: 'tuple' object does not support item assignment

'''6.内置函数 
        len(s)
'''
'''123'''
print(tuple(t)) #tuple(data) 构造函数

'''7.元组转换位字符串'''
