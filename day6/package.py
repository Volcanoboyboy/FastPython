"""
软件包
其本质是一个文件夹，包含一个__init__.py, eg: myutils
"""
# 导入语法与模块方式一样，多一级文件夹
import myutils.mysum
calc_sum = myutils.mysum.sum_numbers
print(calc_sum([1, 2, 4, 5, 6]))
print(myutils.__version__)
print(myutils.__author__)
print(myutils.__email__)

# from 导入跟路径有关系，跟模块导入有点区别
from myutils.mysum import sum_numbers
print(sum_numbers([1, 2, 3, 4]))