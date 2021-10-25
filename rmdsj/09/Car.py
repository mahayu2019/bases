#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 9.2.1 Car类
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.oldmeter = 0  # 9.2.2添加默认属性,行驶里程

    # 返回整洁的描述信息
    def get_descriptive_name(self):
        long_name = str(self.year) + '年产 ' + self.make + '-' + self.model
        return long_name.title()

    def read_oldmeter(self):
        print('已行驶里程' + str(self.oldmeter) + '公里')

    # 9.2.3-2通过方法修改属性值,必须自定义形参,不可使用self
    def update_oldmeter(self, mil):
        self.oldmeter = mil


mycar = Car('奥迪', 'A8', '2020')
print(mycar.get_descriptive_name())
mycar.read_oldmeter()

# 9.2.3 修改属性的值
# 1.直接修改
mycar.oldmeter = 23
mycar.read_oldmeter()

# 2.看上面
mycar.update_oldmeter(90)
mycar.read_oldmeter()
