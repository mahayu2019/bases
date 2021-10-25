#!/usr/bin/env python
# coding=utf-8
import pretty_errors


cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
