#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 9.3 继承
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.oldmeter = 0  # 9.2.2添加默认属性,行驶里程

    def get_descriptive_name(self):
        long_name = str(self.year) + '年产 ' + self.make + '-' + self.model
        return long_name.title()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


mytesla = ElectricCar('吉安特', '自行车', '1998')
print(mytesla.get_descriptive_name())
