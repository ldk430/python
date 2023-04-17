"""
语法错误: 缩进错误, 变量写错, 大小写错误, 缺少符号, 中英文错误... 直接导致程序爆红, 直接终止程序
逻辑错误: 写的代码得到的结果与预期不一致, 代码能运行
"""
# NameError: 访问一个没有声明的变量
# print(age)
# IndexError: 超出索引范围
# list1 = [1, 2, 3]
# print(list1[5])
# TypeError: 类型错误
# print(len(123))
# KeyError: 获取一个字典不存在的键发生错误
# d = {"name": "张三"}
# print(d["age"])
# FileNotFoundError: 文件找不到, 或不存在
# f = open("a.txt", "r")
# print(f.read())
# AttributeError: 当一个对象所有调用属性, 或方法不存在
# print("abc".time())
# -----------------抓取错误-----------------------
# 1. try ... except...语句
try:    # try下边的代码块跟预计有错误的代码块
    print(name)
except NameError:   # 预期的错误, 提前抓取到
    # 当遇到这个错误, 下边处理的手段
    print("这个变量没有定义!")
    name = "张三"

print("程序继续执行...")
print(name)
# 2. try ... except ... else...结构
ls = [1, 2, 3]
try:
    print(ls[1])
except IndexError:
    # 报错处理代码块
    print("已经超出列表的索引范围!")
else:
    # 不报错处理代码块
    print("try上边的代码不报错, 则执行else下边代码块")
# 3. try ... except ... finally... 结构
string = "541863389"
try:
    string.date
except Exception as e:  # Exception: 就是指的上边报那个错误, 泛指
    print("抓取到错误: ", e)
finally:
    # 无论是否报错, 都执行下边代码块
    print("一定执行的代码块!")
