class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def work(self):
        print(f'{self.name}在工作')

# 测试代码
print("---5.1---")
p = Person('简希', 35, '男')
p.work()

class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def work(self):
        print(f'{self.name}在工作')

class Teacher(People):
    def __init__(self, name, age, gender, salary, tel):
        super().__init__(name, age, gender)
        self.salary = salary
        self.tel = tel

    def work(self):
        print(f'{self.name}在授课')

    def play(self, sport):
        print(f'{self.name}正在进行{sport}')

# 测试代码
print("---5.2---")
t = Teacher('简希', 30, '男', 8000, '123456789')
t.work()
t.play('游戏')