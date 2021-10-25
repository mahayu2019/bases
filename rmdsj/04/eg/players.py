#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 4.4.1 切片  object[start_index:end_index:step]
'''
一个完整的切片表达式包含两个“:”，用于分隔三个参数(start_index、end_index、step)。
只有一个“:”时，默认第三个参数step=1；当一个“:”也没有时，start_index=end_index，
表示切取start_index指定的那个元素。

step：正负数均可，其绝对值大小决定了切取数据时的‘‘步长”，而正负号决定了“切取方向”，
正表示“从左往右”取值，负表示“从右往左”取值。当step省略时，默认为1，即从左往右以步长1取值。
“切取方向非常重要！”“切取方向非常重要！”“切取方向非常重要！”，重要的事情说三遍！

start_index：表示起始索引（包含该索引对应值）；该参数省略时，表示从对象“端点”开始取值，
至于是从“起点”还是从“终点”开始，则由step参数的正负决定，step为正从“起点”开始，为负从“终点”开始。

end_index：表示终止索引（不包含该索引对应值）；该参数省略时，表示一直取到数据“端点”，
至于是到“起点”还是到“终点”，同样由step参数的正负决定，step为正时直到“终点”，为负时直到“起点”。


链接：https://www.jianshu.com/p/15715d6f4dad

'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('完整序列:' + players.__str__())
print("用切片生成列表的子集")
print(players[0:3])  # 指定起始索引为0,终止为索引为3
print(players[1:4])

# 不指定起始,默认从头开始
print("\n从头开始切片")
print(players[:4])

# 不指定终止索引
print("\n从第三个元素开始到结尾")
print(players[2:])

# 尾部两个
print("\n从结尾开始取两个元素")
print(players[-2:])

#DIY,拓展
print("\n去掉结尾指定个数的元素")
print(players[:-2])

# 4.4.2 for循环遍历切片
print("\n用循环遍历输出前三个元素")
for p in players[:3]:  # 遍历前三个
    print(p.title())



