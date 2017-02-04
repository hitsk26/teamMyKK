#!/usr/bin/env python
#-*- cording: utf-8 -*-
import pygame.mixer
import time

def play(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    
    pygame.mixer.music.play(10)
    pygame.mixer.music.set_volume(0.8)
    time.sleep(10)
    pygame.mixer.music.stop()
