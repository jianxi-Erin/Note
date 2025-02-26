'''
1 运算符
1.1 赋值运算符  = += -= /= *=
1.2 算术运算符 + - * / % //(除法运算中，整数部分) **幂
        算数运算符只在数值型之间可以运算
1.3 比较运算符 == < > <= >= '
        同类型数据 相互可以比较大小  不同类型的数据 都 ！=
1.4 逻辑运算   and or not 与或非
1.5 成员运算符  in    not in
1.6 位运算  二进制 <<  >>  ,  |  ^  ~
'''
a=2
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
'''
    2.数据类型的转换
        int（value）
        float（value)
        bool(value）
'''
print(bool(0))
print(bool(1))
print(bool(1.9))
print(bool(""))
print(bool("0"))
print(bool("1"))
print(bool("1.9"))
print(bool(None))
print(bool(1+2j))
print(bool(2j))
print(bool(1+0j))

