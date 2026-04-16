"""
模块化
import md
import md as newmd
from md import mdi
from md import mdi as newmdi
from md import * 导入所有子模块
"""

# 自定义模块, 每一个py文件都是一个模块
#导入的模块会执行一遍，是在执行之后执行的
import mymodule

mysum = mymodule.calc_data([1, 2, 3, 4, 5])
print("--------")
print(mymodule.PI)
print(mymodule.__name__) #
print(mysum)
print("--------")