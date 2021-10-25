#!/usr/bin/env python
# coding=utf-8
import pretty_errors

from survey import AnoymousSurvey

question = "你说啥语言?"
my_survey = AnoymousSurvey(question)

my_survey.show_question()
print("输入 'q' 退出\n")
while True:
    response = input("语言:")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\n结果")
my_survey.show_results()
