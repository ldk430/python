import json

f = open("郑州天气.json", "r", encoding="utf-8")
json_data = f.read()    # json字符串
print(type(json_data))
# 1. 反序列化, loads(json字符串)将json数据转换为python数据
python_data = json.loads(json_data)     # json转python, 字典形式
print(type(python_data))
# print(python_data)
# 取出城市的信息
city_info = python_data["cityInfo"]
print(city_info)
city_name = city_info["city"]
sheng = city_info["parent"]
print(sheng, city_name)
# 取data数据, 主要数据
data = python_data["data"]
forecast = data["forecast"]
for f in forecast:
    print(f)
# 2. 序列化, dumps(python数据)将python数据转化json数据
import datetime
news = {
    "message": "感谢CCTV, 让我们报道这次事件",
    "status": 200,
    "time": datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
    "data": [
        {"new1": "神州13发射成功!"},
        {"new2": "台湾回归祖国, 完成国家统一, 见证这个历史时刻吧!"}
    ]
}
# ensure_ascii: 默认为True, 指定使用ASCII编码, False不使用
# indent=4: 格式化结果
j = json.dumps(news, ensure_ascii=False, indent=4)
with open("智能2班媒体.json", "w", encoding="utf-8") as  js:
    js.write(j)

"""
    练习: 将json数据中的   时间, 最高温, 最低温度, 天气状况
"""

