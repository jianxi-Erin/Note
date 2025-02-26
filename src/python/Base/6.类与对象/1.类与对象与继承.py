# class Person:
#     height = 160
#     weight = 80
#
#     # #
#     def __init__(self, height, weight):
#         """
#         构造函数
#         :param height:
#         :param weight:
#         """
#         self.height = height
#         self.weight = weight
#
#     def __del__(self):
#         print("我要被干掉了")
#
#     def eat(self, eat):
#         print("吃东西:", eat)
#
#     def play(self, play):
#         print("玩", play)
#
#
# xiaoming = Person(180, 90)
# print(xiaoming.height)
# print(xiaoming.weight)
# xiaoming.eat("香蕉")
# xiaoming.__del__()
#
#
# # 单继承
# class ordPerson(Person):
#     def sleep(self):
#         print("睡觉")
#
#
# laoming = ordPerson()
# laoming.sleep()
# laoming.eat("dongxi")
#
#
# # 多重继承,先在本类找,然后再在第一个父类调用,找不到的话,在第二个父类找,找不到报错
# # 方法重写,在子类如果定义与父类相同的方法名字,则会重写(覆盖)父类的原方法
# # 方法重载,同一个类,相同名字不同方法名将会被重载,根据传入参数的个数来决定调用哪个方法
#
# class no(ordPerson, Person):
#     def play(self):
#         print("不许玩")
#
#     pass
#
#
# n = no()
# n.play()
# n.sleep()
# n.eat()
#
