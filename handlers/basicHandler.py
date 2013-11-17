import sys
sys.path.append("../easyPygame")
from easyPygame import *
from pygame.locals import *

def close(loop):
    loop.stop()

def updateText(loop):
    if loop.Window.findByName("editText") is not None:
        loop.Window.input = True
        loop.Window.findByName("editText").setText(loop.Buffer)
        loop.Window.update()

handler = eventHandler()
handler.addEvent(close, QUIT)
handler.addEvent(close, K_ESCAPE)
handler.addEvent(updateText, KEYDOWN)
