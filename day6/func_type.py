"""类型注解"""

name: str | int = "nihao"

dic: dict[str, int] = {"name": 10,} # 这里的类型是 键：str，值：int

# 函数类型注解
def calc_data(scores: list[int])-> int:
    calc_sum = 0
    for score in scores:
        calc_sum += score
    return calc_sum

print(calc_data([13, 435, 5465465]), end="$")