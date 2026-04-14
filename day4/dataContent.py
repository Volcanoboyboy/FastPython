"""随机数"""
# import random
#
# random_num = random.randint(1, 100)
# print(random_num)
#
# while True:
#     user_name = int(input('please input your num: '))
#     if user_name == random_num:
#         print("It is right")
#         break


"""data content"""

"""
list, 列表一次性存储多个元素
可以储存不懂类型的元素
元素有序可重复，可以修改
正向索引从0开始，反向索引从-1开始
"""

list1 = [1, True, "hello", 4, 5]
# print(type(list1) == "<class 'list'>")
# print(list1[0])
# print(list1[-1])

list1[0] = 2 # 修改
del list1[0] # 删除

for item in list1: # 遍历
    print(item)

# 切片 list[start:end:step] start 开始索引，默认为0，end索引不包含，step跳过部长

print(list1[:3]) # start默认为0，step默认为1

"""列表常用方法"""
# append() insert() remove() pop() sort() reverse()
# remove 是移除第一个匹配到的元素

"""数据常用方法"""

# sum max min len

"""
判断元素是否包含： 
if item in list => bool
if item not in list => bool

解包：
new_list = [*list1, *list2]

组包：
new_list = list1 + list2

列表推导式
[i for i in list1]
"""

# 列表推导式

list3 = [i ** 2 for i in range(1, 11)]

list4 = [i ** 2 for i in range(1, 21) if i % 2 == 0] # 可以加条件




"""
str字符串
字符串不可替换： 不可变性，有序性，可迭代性
find() count() upper() lower() split() strip() replace() starswith()
不可变，原始字符串不可变

"""

s = "hello python"
print(s[-1:-len(s):-1])# 可以从后往前截取，类似于反转，nohtyp olleh
print(s.count("h") or "p" in s) # in运算符也可判断是否包含


"""
tuple
不可变，只能查询，区别list
t1 = ()
t2 = tuple()
count(): 统计 index()：第一次出现的索引

！定义单元组元素，要加逗号 t = (1,), 不然()默认为通用括号，不是元组
"""

# 定义
t1 = (1, 2, 34, 5, 6)
print(f"{9.8:.2f}") # .2是精读， f是表示这个数是浮点

students = (
("liming", 1, 2, 3, 4),
("hallo", 1, 2, 3, 4),
)

for a, b, c, d, e in students:
    print(f"{a}")


"""
set 集合: 自动去重，无序，不可重复，可修改的数据容器
add() remove() pop() clear() difference() union() intersection()

"""

# 只有这两种定义方式
s1 = {1, 2, 3, 4, 5, 3, 2, 2, 1}
s2 = set() # 注意这里不是{}
s3 = {1, 3, 5}
s1.difference(s2) # s1中包含，s2中没有的
s2.difference(s1) # 差集
s1.union(s2) # 并集
s1.intersection(s2) # 交集
allset = s1 | s2 | s3

print(s1)

# 集合推导式 {要添加的元素或表达式 for s in set if 条件} 和列表推导式类似


"""
dict: 字典，键值对

"""
# 定义
dict0 = {}
dict01 = dict()
dict1 = {"a": 1, "b": 2, "c": 3} # 键不能重复
dict2 = dict({"a": 1, "b": 2, "c": 3}) # key只能是不可变类型，不能是list set dict

# 获取值
res = dict1["a"]
dict_type = type(dict1)

# 添加/修改值
dict1["a"] = 5
dict1["b"] = 6
dict1["c"] = 7

# 删除
del dict1["a"]
dict1.pop("b")

# 查询
dict1.get("c")
dict1.values()  # values
dict1.keys()    # keys
dict1.items()   # key: value, 其中item是元组

for item in dict1.items():
    print(f"{item[0]}: {item[1]}")

for key, value in dict1.items():
    print(f"{key}: {value}")


# eg: shopping_cat = { "apple": {"price": 10, "nums": 10}}
shopping_list = {}
# 制作菜单



























