import pygame
import colors
from pygame.locals import *

class button(object):
    def __init__(self, name, Text, Sprite, x , y, colorkey):
        self.name = name
        self.sprite = sprite(name+Sprite, Sprite, 0 , 0, colorkey)
        self.text = text(name+Text, Text,(self.sprite.surface.get_width())/2
                         ,(self.sprite.surface.get_height())/2,
                         colors.black , 42)
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.visible = True
        self.surface = self.sprite.surface
        self.surface.blit(self.text.surface, 
                          (self.text.x - self.text.surface.get_width()/2, 
                           self.text.y - self.text.surface.get_height()/2))
        self.rect = self.surface.get_rect()
        self.alpha = 100
   
    def onClick(self, w):
        return 0

    def setAlpha(self, alpha):
        self.alpha = alpha
        self.surface.set_alpha(alpha)

class text(object):
    def __init__(self, name, text, x, y, color, size):
        self.name = name
        self.text = text
        self.pos = (x,y)
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.font = pygame.font.Font(None, self.size)
        self.surface = self.font.render(text, 1, (color))
        self.rect = self.surface.get_rect()
        self.visible = True
        self.alpha = 100

    def onClick(self, w):
        return 0

    def setAlpha(self, alpha):
        self.alpha = alpha
        self.surface.set_alpha(alpha)

    def setText(self, text):
        self.text = text
        self.font = pygame.font.Font(None, self.size)
        self.surface = self.font.render(text, 1, (self.color))

class sprite(object):
    def __init__(self, name, path, x , y, colorkey):
        self.name = name
        self.path = path;
        self.x = x;
        self.y = y;
        self.pos = (x, y)
        self.surface = pygame.image.load(path).convert()
        self.colorkey = colorkey
        self.surface.set_colorkey(colorkey)
        self.rect = self.surface.get_rect()
        self.visible = True
        self.alpha = 100

    def onClick(self, w):
        return 0

    def move(self, window,  x, y):
        self.x = self.x + x;
        self.y = self.y + y;
        self.pos = (self.x, self.y)
        window.update()

    def setAlpha(self, alpha):
        self.alpha = alpha
        self.surface.set_alpha(alpha)
