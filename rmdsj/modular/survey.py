#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 11.2.2 一个待测试的类
class AnoymousSurvey():
    def __init__(self, question):
        """存储一个问题,并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示问卷"""
        print(self.question)

    def store_response(self, new_response):
        """将回答存入列表"""
        self.responses.append(new_response)

    def show_results(self):
        """汇总显示结果"""
        print("survey results")

        for response in self.responses:
            print("- " + response)
