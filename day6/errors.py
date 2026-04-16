"""异常"""

def hello():
    goodbye()
    print("hello")
def goodbye():
    print("goodbye")

if __name__ == "__main__":
    try:
        hello()
    except Exception as e:
        print(e)
    finally:
        print(f"看看这个错误最终处理了没啊", end="$")



