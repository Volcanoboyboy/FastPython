s1 = "hello" "world" ", vocal!"

msg1 = 'hello'
msg2 = 'world'

print(msg1 + msg2)

#+号只能拼接字符串类型, 可以利用str()转字符

s2 = 'txz'
s3 = 18
print("下午好，我是:" + s2 + ",今年" + str(s3) + "岁。")

# 字符串格式化，语意化更好，写法更简洁

s4 = 'xiaoming'
print("python world, I`m %s" %s4)
print("hello world %s %s" % (s2, s4)) # 按顺序替换，占位符都是%s

# f"内容{变量/表达式}", 实际使用一般用这种，
print(f"I`m {s4 + s2}")