#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 8.2.1 位置实参,实参传入注意与形参位置对应
def describe_pet(animal_type, pet_name):
    print("\n我有一只" + animal_type)
    print("名字叫" + pet_name)


describe_pet('猫', '皮特')

# 8.2.2 关键字实参,指定关键字后,实参位置可任意排列,形参实参名字必须对应
describe_pet(pet_name="杰瑞", animal_type="老鼠")

# 8.2.3 默认值,给形参设定默认值
'''P119
注意 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。
这让Python依然能够正确地解读位置实参。
'''


def describe_pet(animal_type, pet_name='joke'):
    print("\n我有一只" + animal_type)
    print("名字叫" + pet_name)


describe_pet('马')
