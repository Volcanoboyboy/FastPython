# 单行注释
"""多行注释"""

# 条件判断 if  python 代码归属通过空格对其来表示， 一般是四个空格， 这个流程范围代码也称为代码块
# if 100 == '100':  # 条件不需要括号， 且后见需要英文冒号， 且缩紧要对齐，不然也是错误语法
#     print("true, 100 == '100'")
#     print('hhhh, 是对的！')
# else:
#     print("false, 100 != '100'")
#     print("hhh，是错的！")
#
#
# num = int(input("请输入正整数"))
# if num == '1':
#     print(f"num is {num}")
# elif num == '2':
#     print(f"num is {num}")
# else:
#     print(f"num is {num}")

"""三角形判断"""

# a = int(input('请输入第一条边'))
# b = int(input('请输入第二条边'))
# c = int(input('请输入第三条边'))
#
# if a + b < c or b + c < a or a + c < b:
#     pass  # 这是空语句，类似TODO
#     print('这三条边不能组成三角形！！')
# else:
#     print('这三条边能组成三角形')
#     if a == b and b == c:
#         print("并且是等边")
#     elif a == b or b == c or c == a:
#         print("并且是等边三角形")
#     else:
#         print("就是普通三角形")

"""模式匹配 match...case, 通过模板匹配数据结构和内容"""

# day = input("请输入今天周几")
# match day:
#     case "1":
#         print("周一")
#     case "2":
#         print("周三")
#     case "3":
#         print("周三")
#     case "4":
#         print("周三")
#     case "5":
#         print("周三")
#     case "6" | "7" if day == "6" or day == "7": # 条件差成功才匹配case条件
#         print("周三")
#     case _:
#         print("错误输入")

"""循环"""
# while
# i = 0
# while i < 10:
#     print("人生苦短我学python")
#     i += 1
# else: #跳出循环触发
#     print("打印完了，十遍可以了")

# 0-100，偶数和

# total = 0
# i = 0
# while i <= 100:
#     if i % 2 == 0:
#         total += i
#     i += 1
# else:
#     print(total)

"""for循环，是轮询机制， 类似js中的for...in循环"""
# forName = "hello world"
# for i in forName:
#     print(i)
# else:
#     print(f"{forName}遍历完成")

"""利用range(start, stop, step), 不包括stop, 只写stop是从0开始"""

# 计算1-100之间所有奇数集
# nums = range(0, 101, 2)
# for i in nums:
#     if i % 2 == 1: # 实际不用再判断了
#         print(i)
# else:
#     print(f"{nums}奇数项打印完毕")

# 获取 100-500 之间能被3整除的数
# nums2 = range(100, 501)
# for i in nums2:
#     if i % 3 == 0:
#         print(i)
# else:
#     print(f"{nums2}中能被3整除的数已经打印完毕")

"""嵌套循环， print自带换行效果"""

# m1 = int(input("长度"))
# n1 = int(input("高度"))

# for n in range(n1):
#     for m in range(m1):
#         print("*", end=" ")
#     print()

# 输出99乘法表
for n in range(1, 10):
    for m in range(1, n + 1):
        print(f"{m} * {n} = {m * n}", end="\t")
    print()


"""循环关键字： break, continue"""

while True:
    username = input("username: ")
    password = input("password: ")
    if username == "" or password == "":
        print("用户名或密码不能为空， 请重新输入")
        continue #结束当前循环，进入下一次循环，避免浪费
    elif username == "admin" and  password == "123":
        print("登录成功！")
        break



















