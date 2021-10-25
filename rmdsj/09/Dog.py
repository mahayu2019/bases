#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 9.1.1 创建类
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


# 9.1.2 根据类创建实例
my_dog = Dog("马特", 6)
print("狗狗名字:" + my_dog.name.title() + ".")
print(str(my_dog.age) + "岁了")
my_dog.sit()
my_dog.roll_over()
you_dog = Dog("史蒂芬", 3)
print("狗狗名字:" + you_dog.name.title() + ".")
print(str(you_dog.age) + "岁了")
you_dog.sit()
you_dog.roll_over()
