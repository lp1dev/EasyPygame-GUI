import pygame
import colors
from pygame.locals import *

class element(object):
       def __init__(self, name, x, y):
              self.name = name
              self.x = x
              self.y = y
              self.pos = (x,y)
              self.surface
              self.visible = True
              self.isClicked = False
              self.alpha = 100

       def onClick(self, w, elem):
              return 0

       def setAlpha(self, alpha):
              self.alpha = alpha
              self.surface.set_alpha(alpha)

class menu(element):
       def __init__(self, name):
              self.name = name
              self.elems = []

       def addElem(elem):
              self.elems.append(elem)

       def setSelected(Elem):
              for elem in self.elems:
                     elem.isClicked == False
              Elem.isClicked == True

class buttonColored(element):
       def __init__(self, name, Text, x, y, x2, y2 ,bgcolor, txtcolor, size):
              self.name = name
              self.Text = Text
              self.textSize = size
              self.x = x
              self.y = y
              self.pos = (x,y)
              self.visible = True
              self.backgroundColor = bgcolor
              self.textColor = txtcolor
              self.isClicked = False
              self.shape = shape("shape_"+name, bgcolor, x, y, x2, y2)
              self.text = text("text_"+name, Text, x , y, txtcolor, size)
              self.surface = self.shape.surface
              self.surface.blit(self.text.surface ,
                                (x2/2 - self.text.surface.get_width()/2, 
                                 y2/2 - self.text.surface.get_height()/2))
              self.rect = self.surface.get_rect()
              self.alpha = 100

       def setText(self, text):
              self.Text = text
              self.redraw()

       def setTextColor(self, color):
              self.textColor = color
              self.redraw()

       def redraw(self):
              self.shape = shape("shape_"+self.name, self.backgroundColor, 
                                 self.shape.x, self.shape.y, 
                                 self.shape.x2, self.shape.y2)
              self.text = text("text_"+self.name, self.Text, self.x , self.y, self.textColor, self.textSize)
              self.surface = self.shape.surface
              self.surface.blit(self.text.surface ,
                                (self.shape.x2/2 - self.text.surface.get_width()/2, 
                                 self.shape.y2/2 - self.text.surface.get_height()/2))
              self.rect = self.surface.get_rect()

       def setBackgroundColor(self, color):
              self.backgroundColor = color
              self.redraw()
              
class shape(element):
       def __init__(self, name, color, x, y, x2, y2):
              self.name = name
              self.x = x
              self.y = y
              self.x2 = x2
              self.y2 = y2
              self.pos = (x, y)
              self.color = color
              self.visible = True
              self.surface = pygame.Surface((x2,y2))
              self.surface = self.surface.convert()
              self.surface.fill(color)
              self.rect = self.surface.get_rect()
              self.alpha = 100              

class button(element):
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

class text(element):
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
   
       def setText(self, text):
              self.text = text
              self.font = pygame.font.Font(None, self.size)
              self.surface = self.font.render(text, 1, (self.color))
              
class sprite(element):
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

       def move(self, window,  x, y):
              self.x = self.x + x;
              self.y = self.y + y;
              self.pos = (self.x, self.y)
              window.update()                     
