#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame import gfxdraw
pygame.init()
 
k = 8
W = 100
H = 100
win_w = W*k
win_h = H*k
setpix = gfxdraw.pixel
window = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("LIFE")
icon = pygame.image.load("/home/user/Документы/python/myprogram/glider-small.png")
pygame.display.set_icon(icon)
pol1 = [[0]*(W) for i in range(H)]
pol2 = [[0]*(W) for i in range(H)]
 
pol1[4][2] = 1
pol1[2][3] = 1
pol1[4][3] = 1
pol1[3][4] = 1
pol1[4][4] = 1
pol1[40][11] = 1
pol1[40][12] = 1
pol1[40][13] = 1
pol1[40][29] = 1
pol1[39][30] = 1
pol1[41][30] = 1
pol1[60][60] = 1
pol1[61][60] = 1
pol1[60][61] = 1
pol1[30][31] = 1
pol1[31][31] = 1
pol1[29][31] = 1
pol1[77][20] = 1
pol1[77][21] = 1
pol1[77][22] = 1
pol1[56][14] = 1
pol1[56][15] = 1
 
def matr(old,sosed):
    if sosed <= 1:
        n = 0
    elif sosed == 2:
        n = old
    elif sosed == 3:
        n = 1
    else:
        n = 0    
    return n
       
def update(prev, next):
    for i in range(0,H):
        for j in range(0,W):
            if i == 0 and j == 0:
                k1 = prev[0][1]
                k2 = prev[1][1]
                k3 = prev[1][0]
                k4 = prev[H-1][0]
                k5 = prev[H-1][W-1]
                k6 = prev[H-1][1]
                k7 = prev[0][W-1]
                k8 = prev[1][W-1]
            elif i == 0 and j == W-1:
                k1 = prev[0][W-2]
                k2 = prev[1][W-2]
                k3 = prev[1][W-1]
                k4 = prev[1][0]
                k5 = prev[0][0]
                k6 = prev[H-1][W-1]
                k7 = prev[H-1][W-2]
                k8 = prev[H-1][0]                                  
            elif i == H-1 and j == 0:
                k1 = prev[H-2][j]
                k2 = prev[H-2][1]
                k3 = prev[H-1][1]
                k4 = prev[H-2][W-1]
                k5 = prev[H-1][W-1]
                k6 = prev[0][0]
                k7 = prev[0][1]
                k8 = prev[0][W-1]
            elif i == H-1 and j == W-1:
                k1 = prev[H-2][W-1]
                k2 = prev[H-1][W-2]
                k3 = prev[H-2][W-2]
                k4 = prev[H-2][0]
                k5 = prev[H-1][0]
                k6 = prev[0][W-1]
                k7 = prev[0][W-2]
                k8 = prev[0][0]
            elif i >=1 and i <= H-2 and j == 0:
                k1 = prev[i-1][0]
                k2 = prev[i+1][0]
                k3 = prev[i-1][1]
                k4 = prev[i][1]
                k5 = prev[i+1][1]
                k6 = prev[i-1][W-1]
                k7 = prev[i][W-1]
                k8 = prev[i+1][W-1]
            elif i >=1 and i <= H-2 and j == W-1:
                k1 = prev[i-1][W-1]
                k2 = prev[i+1][W-1]
                k3 = prev[i][W-2]
                k4 = prev[i-1][W-2]
                k5 = prev[i+1][W-2]
                k6 = prev[i-1][0]
                k7 = prev[i][0]
                k8 = prev[i+1][0]
            elif i == 0 and j >= 1 and j <= W-2:
                k1 = prev[0][j+1]
                k2 = prev[0][j-1]
                k3 = prev[H-1][j-1]
                k4 = prev[H-1][j]
                k5 = prev[H-1][j+1]
                k6 = prev[1][j-1]
                k7 = prev[1][j]
                k8 = prev[1][j+1]
            elif i == H-1 and j >= 1 and j <= W-2:
                k1 = prev[H-1][j+1]
                k2 = prev[H-1][j-1]
                k3 = prev[0][j-1]
                k4 = prev[0][j]
                k5 = prev[0][j+1]
                k6 = prev[H-2][j-1]
                k7 = prev[H-2][j]
                k8 = prev[H-2][j+1]
            else:
                k1 = prev[i][j-1]
                k2 = prev[i][j+1]
                k3 = prev[i-1][j-1]
                k4 = prev[i-1][j]
                k5 = prev[i-1][j+1]
                k6 = prev[i+1][j-1]
                k7 = prev[i+1][j]
                k8 = prev[i+1][j+1]
           
            kpos = prev[i][j]
            sosed = k1 + k2 + k3 + k4 + k5 + k6 + k7 + k8
            next[i][j] = matr(prev[i][j],sosed)
    for i in range(0,H):
        for j in range(0,W):
            if next[i][j] == 1:
                pygame.draw.rect(window, (0, 255, 0), (j*k,i*k,k,k), 0)
   
    for i in range(0,win_w,k):
        pygame.draw.line(window, (20, 20, 20), (i, 0), (i, win_w))
    for i in range(0,win_h,k):
        pygame.draw.line(window, (20, 20, 20), (win_w, i), (0, i))
 
 
   
 
def react_to_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        else:
            print event
 
flag = 0
N=10000
while N>0 and (pol1 != pol2):
    pygame.time.wait(10)
    window.fill((0,0,0))
    N = N + 1
    if flag == 0:
        update(pol1, pol2)
        flag = 1
    else:
        update(pol2, pol1)
        flag = 0
    pygame.display.flip()
    react_to_events()
