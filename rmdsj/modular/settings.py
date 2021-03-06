#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 12章游戏的设置类
class Settings():

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 子弹颜色
        self.bullets_allowed = 3  # 子弹数量

        # 飞船的设置
        self.ship_speed_factor = 1.5  # 每次移动1.5个像素
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1--右移,-1为左移
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''动态更新游戏设置'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1--右移,-1为左移
        self.fleet_direction = 1

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
