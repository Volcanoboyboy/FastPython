"""
面向对象

"""

class Person:
    # 类属性 -- 链式访问
    hair = "long"
    color = "yellow"
    # 魔法方法__init__，魔法方法会由类自调用
    def __init__(self, name, age):
        # 实例属性 -- 优先访问
        self.name = name
        self.age = age
    def display(self): # 实例方法
        print(self.name)
        print(self.age)
    def speak(self):
        """
        自我介绍
        :return: 名字和年龄
        """
        print(f"my name is {self.name} and my age is {self.age}")

    # 魔法方法 __init__ __str__ __eq__ __lt__ __le__ __gt__ __ge__
    def __str__(self):
        return f"my name is {self.name} and my age is {self.age}"
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    def __lt__(self, other):
        return  self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
    def __le__(self, other):
        return self.name <= other.name and self.age <= other.age
    def __ge__(self, other):
        return self.name >= other.name and self.age >= other.age
    def __add__(self, other):
        return self.name + other.name



xiaoming = Person("xiaoming", 18)
print(xiaoming) # 默认输出的是对象地址
# 如果添加了__str__魔法方法，对象会默认输出__str__的返回内容

print(xiaoming.name)
print(xiaoming.age)




























