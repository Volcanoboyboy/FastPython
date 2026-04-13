# input 函数 获取键盘输入数据： s = input(“提示信息”)
# 输入是同步执行的，一个输入会阻塞下一个
name = input("please input your name: ")
age = input("please input your age: ") # 所有键盘录入的数据都是字符串 ”18“
print(f"your name is {name}, age is {age}? right!")

# int类型只能和int类型计算，可通过int()函数转化字符串
# int() str() float() bool()
# float能兼容int但是int不能兼容float

# 运算符
# + - * / 除法 // 整除 % 摩 ** 幂指数
print(3 / 2)
print(3 // 2)

# 优先级
#  ** ｜ * / // % ｜ + -

# python 也具有精度问题，损失
print(0.5 - 0.4) # 0.0999999999998
