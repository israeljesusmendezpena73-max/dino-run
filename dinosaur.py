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
fs=-15
g=0.8
tem=0
teo=36
sy=300
ds=0
vy=0
vc=2
ees=True
ed=1
dino_img=pygame.image_load(os.path.join("img","dino.png").convert_alpha
cactus_img=pygame.image_load(os.path.join("img","cactus.png").convert_alpha
dino dunk_img=pygame.image_load(os.path.join("img","dino dunk.png").convert_alpha
roca_img=pygame.image_load(os.path.join("img","roca.png").convert_alpha
def jugar():
  tem=0
  cactuse=[]
  while mode==True:
  dy=dino.y
  dx=dino.x
  dcollider=(40,40,dx+10,dy+20)
  keys=pygame.key.get_pressed
  if keys[pygame.a] or  keys[pygame.SPACE] or keys[pygame.K_UP] and ds<3:
    dino.y +=fs
    ees=False
    ds+=1
    vy=fs
    vy+=g
    if dino.y>=sy:
      while ees=False:
        dino.y-=g
        delay(10)
        if dino.y<sy
        ees=True
        ds=0
  if keys[pygame.K_DOWN] or keys[pygame.s]:
        ed=0
        dcollider=pygame.rect(40,20,dx+10,dy)
        dino dunk.x=rx
        dino dunk.y=ry
  elif  not(keys[pygame.K_DOWN] or keys[pygame.s]):
        ed=1
  if ed=1:
        window.blit(dino_img)
  elif ed=0
       window.blit(dino dunk_img)
