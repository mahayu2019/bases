#!/usr/bin/env python
# coding=utf-8
import pretty_errors

# 10.2.1 写入空文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('喂饭')
'''
open()方法:
第一参数:文件名
第二参数:模式参数
        r --只读,文件必须存在
        r+ --读写模式,在文件头部新增内容,文件必须存在
        w --清空原内容后写入,可自行创建文件
        a --在文件末尾添加新内容,可自行创建文件              
'''

# 10.2.2 写入多行
filedh = 'dh.txt'
with open(filedh, 'w') as file_object:
    file_object.write('第一行内容.\n')  # 使用换行符\n来实现多行写入
    file_object.write('第二行内容.\n')
    file_object.write('再加一行.\n')
    file_object.write('over....')
