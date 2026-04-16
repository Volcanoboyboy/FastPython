# __all__ 指定通用导入的模块, from md import *
__all__ = ["calc_data", "PI"]


def calc_data(data: list[int]) -> int:
    res = 0
    for i in data:
        res += i
    return  res

# 规范定义常量
PI = 3.14
NAME = "txz"

# __name__ 模块内置变量-> "__main__"
# 简写 main就会提示
if __name__ == "__main__":
    print("test") # 控制这个输出只在当前文件内部执行
