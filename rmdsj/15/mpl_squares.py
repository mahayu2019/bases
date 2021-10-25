#!/usr/bin/env python
# coding=utf-8
import pretty_errors
import matplotlib.pyplot as plt

# 15.2 绘制简单的折线图
squares = [1, 4, 9, 16, 25]
plt.plot(squares)

# 15.2.1 修改标签文字和线条粗细
plt.title("折线图", fontproperties='SimHei', fontsize=24)  # 需要注明字体,否则中文无法显示
plt.xlabel("值", fontproperties='SimHei', fontsize=14)
plt.ylabel("参数", fontproperties='SimHei', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
