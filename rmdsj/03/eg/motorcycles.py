#!/usr/bin/env python
# coding=utf-8
import pretty_errors

# 3.2.1 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print("打印列表:")
print(motorcycles)

motorcycles[0] = 'ducati'
print("\n修改第一个元素,然后输出")
print(motorcycles)

# 3.2.2 在列表结尾添加元素
motorcycles.append('hongqi')
print("\nappend--在列表结尾添加元素")
print(motorcycles)

motorcycles = []
motorcycles.append('长安')
motorcycles.append('大奔')
motorcycles.append('奥迪')
motorcycles.append('大众')
print("\n在空列表中加入元素")
print(motorcycles)

# 插入元素 insert,必须指定元素索引和值
motorcycles.insert(2, 'mazida')
print("\n插入元素--insert")
print(motorcycles)

# 3.2.3 删除元素,必须指定元素索引值
del motorcycles[1]
print("\n删除指定索引的元素")
print(motorcycles)

# 使用pop弹出元素(从结尾开始弹出)
motorcycles.pop()
print("\n从结尾弹出元素--pop")
print(motorcycles)

# 弹出指定位置的元素
fk = motorcycles.pop(1)  # 弹出并赋值
print("\n弹出指定位置的元素pop(元素下标)")
print('他开的是' + fk)

# 根据值删除元素
print("\n根据值删除元素--remove(元素名称)")
print(motorcycles)
motorcycles.remove('长安')
print(motorcycles)
