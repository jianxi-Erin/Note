'''
字符串的定义 必须在一对引号里
引号可以是单双三都可以 '',"",''' ''',""" """
使用”+“做字符串拼接
两个字符串都要有引号 ” “+” “
'''
s1='1'
s2='a'
s3='1.0'
s4="1"
s5="""1"""
print(s4,type(s4))
print(s5,type(s5))
print(s1,type(s1))
s11='aaaabbbccc'
s12="aaaabbbccc"
s13='''aaaabbbccc'''
s14='aaa' \
    'bbb' \
    'bbb'
s15="aaaa" \
    "bbb" \
    "ccc"
s16='''aaa
        bbb
        ccc'''
print(s11)
print(s12)
print(s13)
print(s14)
print(s15)
print(s16)

'''
    2.字符串的拼接
        2.1 使用’+‘拼接
        2.2 字符串挨着
        2.3 字符串只能个和字符串拼接，不能和数值类型拼接
        2.4 使用’‘*n  字符串重复n次拼接字符串

'''
s1='hello'+'world'
s2='hello''world'
print(s1)
print(s2)

#定义一个字符串’**********‘10个星号
print('*'*10)
'''
    3 转义字符   \各语言通用
       \特殊字符 \n（换行）  \\（一个\） 
       要求输出 I’m Zhangsan
 '''
print( 'I\'m Zhangsan')

'''
    4.字符串长度 len(str)
'''
print(len('I\'m ZhangSan'))
print(len("I'm ZhangSan"))

'''
    5.字符串中字符元素的访问
        索引
        5.1正序索引
            从左边开始 0向右 依次递增 1
        5.2逆序索引
            从右边开始 -1向左 依次递减1
'''
s='hello world'
print(s[0])
print(s[10])
print(s[-11])

'''
    问题
        1.需要指定字符串中前五个字符
        2.需要指定字符串中后五个字符
        3.需要指定字符串中前2-7位置范围内的字符
        4.需要指定字符串中第六个字符
6.切片:按某个规格切
  str[start:stop:step]
  参数 
    start 从第几个元素开始切
            如果从最左边开始切片，及start是0，则start可省
    stop  切到第几个元素
            最后一个元素，len-1，则stop可省
    step  切片的步长值，默认为1
        正数：从做到右
        负数：从右到左
'''
s11="hello world"
print(s11[6:9])
print(s11[6:])
# 切出偶数位置的整数
print(s11[::2])
print(s11[2:-2])
#逆序输出
print(s11[::-1])

'''
    格式化
        字符串中间的占位符;
        %s:整数 %10s
        %d:字符串  %3d
        %f:浮点   %.2f
        
        {}{}  format（）
        {}{}  format（）
        {:>3}{:10>}{:.2f}  format（）
        {:<3}{:10<}{:.2f}  format（）
        
        f  {}  {}  {} 
        f/F 的作用是把其后面的字符串作为格式字符串
'''
no=1
name='ZhangSan'
height=171.5
#我是1号考生，我的姓名是ZhangSan，身高171.5
print("我是%d号考生，我的姓名是%s，身高%f。" % (no, name, height))
#171.5取出整数部分 给了%d，丢失小数部分
print("我是%d号考生，我的姓名是%s，身高%f。"%(height,name,height))
print("我是{}号考生，我的姓名是{}，身高{}。".format(height,name,height))
print(f"我是{no}号考生，我的姓名是{name}，身高{height}。")

'''
7 字符串处理常用函数
7.1 字符处理
7.2 字符查找
        str.find(sub,start=0,end=len(str))
            参数;sub：要在原始字符串str中查找的子串
                start 从原始字符串str的start位置处开始往后查找
                end 查找到原始字符串str的end位置前，结束
        返回值：
        sub在str中第一次出现的首字符位置
        找不到sub 则返回-1
    str.rfind（）
    
    str.index（）
    
    str.count（）
7.3 字符判断
7.4 字符替换
'''
s='hello WORLD'
print(s)
s1=s.capitalize()
print(s1)
print(s.upper())
print(s.lower())
print(s.swapcase());   '''交替'''
#7.2 字符查找
s='hello world world world'
result=s.find('w')
print(result)
print(s[6])
result=s.find('wor')
print(result)
result=s.find('wwr')
print(result)
result=s.find('wor',10)
print(result)
result=s.find('wor',10,20)
print(result)
#7.3 字符串判断
print(s.isalpha())
print(s.islower())
print('123'.isdigit())
print('abc'.isalpha())

#7.4 字符串替换
s='hello world hello world'
print( s.replace(' ','\n')) #把空格替换为换行
print(s.replace(' ','\n',2)) #把空格替换为换行2次
s1='hello world hello world'
print(s1.strip())
print(s1.lstrip())
print(s1.rsplit())
print(s1.strip('he'))


str='aAbBcC'
s=str.swapcase()
print(s);

str='aAbBcC'
print(str[-1]+str[:-1])


str='aAbBcC'
print(str[::-1])

