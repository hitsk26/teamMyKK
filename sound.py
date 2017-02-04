#!/usr/bin/env python
#-*- cording: utf-8 -*-

import pygame.mixer
import time

# mixerモジュールの初期化
pygame.mixer.init()
# 音楽ファイルの読み込み
pygame.mixer.music.load("/home/tsuzuku/python_games/match1.wav")
# 音楽再生、および再生回数の設定(-1はループ再生)
pygame.mixer.music.play(-1)

time.sleep(60)
# 再生の終了
pygame.mixer.music.stop()