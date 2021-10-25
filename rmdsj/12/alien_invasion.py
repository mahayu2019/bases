#!/usr/bin/env python
# coding=utf-8
import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # 初始化游戏并创建屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("游戏")
    # 创建按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 设置背景色
    bg_color = (ai_settings.bg_color)

    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 创建一个存储子弹的编组
    bullets = Group()

    # 创建外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个外星人
    alien = Alien(ai_settings, screen)


    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()
