# 自定义异常, 当你写代码时, 需要一个报错

# 1. 使用raise, 自定义错误
# ZeroDivisionError: 除数不能为零

def chufa():
    a = int(input("除数: "))
    b = int(input("被除数: "))
    if a == 0:
        # raise ValueError("除数不能为0!")
        raise ZeroDivisionError("输入除数是0, 错误")
    return b / a

# print(chufa())
# 2. 断言, assert语句, 定义异常
def cf():
    a = int(input("除数: "))
    b = int(input("被除数: "))
    assert a!=0, "除数不能为0!"
    return b / a

# print(cf())

if __name__ == '__main__':
    try:
        res = cf()
    except AssertionError as a:
        print("断言错误: ", a)
    else:
        print(res)