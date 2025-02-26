# abc模块是所有抽象类的鸡肋
# 要使用抽象类必须导入这个模块
# 抽象类:比如求图形的面积,那么图形的面积就是抽象类.抽象类有方法名,但没有具体的方法体
# 抽象类:抽象类必须被继承
# 抽象类:必须指定元类metaclass=abc.ABCMeta
#   @abc.abstractmethod抽象方法
# @abstractclassmethod抽象类方法
# @abstractstrticmethod抽象静态方法
import abc


class animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def eat(self):
        """
        抽象方法:eat
        :return:
        """
        pass

    @abc.abstractmethod
    def drink(self):
        """
        抽象方法:drink
        :return:
        """
        pass

    @abc.abstractmethod
    def play(self):
        """
        抽象方法:play
        :return:
        """
        pass

    # 成员方法
    def last(self):
        print("动物很开心")


#         继承抽象类
class Dog(animal):
    def __init__(self) -> None:
        print("我是狗狗")

    # 重写抽象方法

    def eat(self):
        print("吃肉")

    def drink(self):
        print("喝水")
        pass

    def play(self):
        print("玩骨头")

    def last(self):
        super().last()


#         继承抽象类
class Cat(animal):
    def __init__(self) -> None:
        print("我是猫猫")

    # 重写抽象方法

    def eat(self):
        print("吃鱼")

    def drink(self):
        print("喝奶")
        pass

    def play(self):
        print("玩毛球")

    def last(self):
        super().last()


xiaohua = Cat()
xiaohua.eat()
xiaohua.drink()
xiaohua.play()
xiaohua.last()
print("=============")

xiaoyong=Dog()
xiaoyong.eat()
xiaoyong.drink()
xiaoyong.play()
xiaoyong.last()