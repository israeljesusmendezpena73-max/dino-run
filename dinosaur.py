import pygame
import sys
import random
import os
pygame.init()
cielo=(10,10,10)
x,y=800,500
window=pygame.display.set_mode(x,y)
pygame.display.set_caption("dino run")
Fuente=pygame.font.Sysfont(arial,24)
fps=pygame.tick.Clock
vob=0
fs=15
g=0.8
teo=36
dino_img=pygame.image_load(os.path.join("img","dino.png").convert_alpha
cactus_img=pygame.image_load(os.path.join("img","cactus.png").convert_alpha
roca_img=pygame.image_load(os.path.join("img","roca.png").convert_alpha                           
def jugar():
  
