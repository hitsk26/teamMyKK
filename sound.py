#!/usr/bin/env python
#-*- cording: utf-8 -*-
import pygame.mixer
import time

pygame.mixer.init()
pygame.mixer.music.load("/home/tsuzuku/python_games/match1.wav")

pygame.mixer.music.play(3)
pygame.mixer.music.set_volume(0.8)

time.sleep(2)
pygame.mixer.music.stop()