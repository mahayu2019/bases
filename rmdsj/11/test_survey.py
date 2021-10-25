#!/usr/bin/env python
# coding=utf-8
import pretty_errors
from survey import AnoymousSurvey
import unittest



class TestAnonmyousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "你说啥语言?"
        my_survey = AnoymousSurvey(question)
        my_survey.store_response('英语')

        self.assertIn('英语', my_survey.responses)

    def test_store_three_response(self):
        question = "你说啥语言?"
        my_survey = AnoymousSurvey(question)
        responses = ['韩语', '日语', '德语']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

