#!/usr/bin/env python
# coding=utf-8
import pretty_errors

# 2.4.3 使用str()避免类型错误
age = 23
message = "happy " + str(age) + "rd birthday"
print(message)
