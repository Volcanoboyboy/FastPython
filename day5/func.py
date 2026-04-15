"""
函数
def fun_name(name):
    print(name)
"""

def fun_name(name):
    print(name)
    return name

fun_name("python")  # 没有作用域提升，得先定义s

# 类型
print(type(fun_name))  # <class 'function'>

# 参数 返回值 默认返回 None, 可以返回多个值，以，隔开，返回类型是tuple
# help(test) 可以通过help查看函数说明

def test(num):
    """
    函数返回多个值
    :param num: 入参
    :return: 返回的是tuple
    """
    return num * 3.14, round(2 * num * 3.14, 2)

print(type(test(10))) # <class 'tuple'>


# 区分全局变量和局部变量， 全局变量一般定义在顶部

# 如果需调用全局变量，可以使用 global

name = "txz"
def fun_1():
    global name
    name = "xhs" # 已将全局变量修改，如不使用global则会在局部生成一个临时变量

    print(name)

fun_1()

print(name)


# 参数：传参方式，默认参数，不定长参数

# 位置传参数
def fun_3(a, b, c):
    print(a, b, c)
fun_3(1, 2, 3)

# 关键字传参
def fun_4(a, b, c):
    print(a, b, c)
fun_4(b = 1, c = 3, a = 2)
print(fun_4)

# 同时还可以混合使用
def fun_5(a, b, c):
    print(a, b, c)
fun_5(1, c = 3, b = 2) # 注意位置参数前置


# 默认参数
def fun_6(a, b, c = 3):
    print(a, b, c)
fun_6(1, 2)

# 不定长参数
def fun_7(*args, **kwargs): # arguments keywordarguments
    print(args, kwargs)

fun_7(1, 3, 4, {'a': 5, 'b': 6}, name = 'z')

# 函数本身也是变量，可以传递

# lamda 匿名函数

nums = [1, 2, 3, 4, 5, 6, 7, 8]

fun_l = lambda x: x % 2 == 0
even_nums = list(filter(fun_l, nums))
print(even_nums)

strs = ["23213", "fdsfs", "df", 'fdsafsda']



strs.sort(key=lambda item: len(item), reverse=False)
print(strs)


# 递归调用
def funSteps(n):
    if n > 1:
        return  n * funSteps(n -1)
    else:
        return n
print(funSteps(-10))







