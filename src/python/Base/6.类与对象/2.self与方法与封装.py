# self
# self表示本类
# 类的实例方法,必须有self
class person:
    # 这是全局变量
    # 这里的变量无法直接修改
    name = "周晓"
    age = 18
    lanme = "别人"
    # 这是封装,私有,参考java,前面__用来修饰变量或者方法就为封装私有化
    __pwd = "pwd"

    # 这是魔术方法__init__,类似于构造函数
    def __init__(self, name, age, lname):
        self.name = name
        self.age = age
        self.lanme = lname
        print("这是__init__方法,自动执行")

    # #     这是魔术方法__new_,最先自动执行
    # def __new__(cls, *args, **kwargs):
    #     print("这是__new_方法,自动执行")

    # 这是魔术方法__str__类似于toString()方法
    def __str__(self):
        print("这是__str__方法,类似于toString()方法")
        print(f"name={self.name}, age ={self.age},lnaem={self.lanme}")

    # 这是实例无参方法
    def eat(self):
        print("eat")

    # 这是实例有参方法
    def myName(self, name):
        print(f"我的名字是{name}")

    # 我是类方法,可以直接通过类.方法名调用
    # 而且我不用self,我用cls
    @classmethod
    def classMyanme(cls):
        print(f"我是类方法,可以直接使用类.方法名调用,正常的调用也可以使用")
        print(f"我也可以使用类中的变量.但是静态方法不可以,我的名字是:{cls.name}")

    # 静态方法
    #  可以直接使用类.方法名调用,也可以使用普通方法调用
    #  而且我不需要cls
    @staticmethod
    def staticMym():
        print("我是静态方法,我不知道name这个参数")


zhouxiao = person("周晓", 21, "张维维")
zhouxiao.__str__()
zhouxiao.eat()
zhouxiao.myName("张三")
person.staticMym()
person.classMyanme()
pe