#!/usr/bin/env python
# coding=utf-8
import pretty_errors
import unittest

from name_function import get_formatted_name


# ctrl+shift+T 可以对指定方法生成测试文件
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):  # 测试方法必须以test开头
        formatted_name = get_formatted_name('janis', 'joplin')  # 运行结果保存入变量中
        self.assertEqual(formatted_name, 'Janis Joplin')  # 断言方法,比较结果和预期是否一致

    # 11.1.5 添加新测试
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('张', '三', '疯')
        self.assertEqual(formatted_name, '张 疯 三')
