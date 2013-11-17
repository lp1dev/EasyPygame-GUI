#!/usr/bin/python2

import sys
sys.path.append("easyPygame")
sys.path.append("handlers")
from easyPygame import *
from pygame.locals import *
import pygame
import colors
import basicHandler

def changeClickedState(elem):
    if (elem.isClicked == False):
        elem.setTextColor(colors.white)
        elem.setBackgroundColor(colors.blue_marine)
    else:
        elem.setTextColor(colors.gray)
        elem.setBackgroundColor(colors.dark_gray)
    if(elem.isClicked == True):
        elem.isClicked = False;
    else:
        elem.isClicked = True;

def clearScreen(w):
    w.elems = []
    drawLeftMenu(w)

def createDialogListener(loop, elem):
    w = loop.Window
    if (elem.name == "editText"):
        w.input = True
    if (elem.name == "validate"):
           changeClickedState(elem)
    w.update()

def leftMenuClickListener(loop, elem):
    w = loop.Window
    changeClickedState(elem)
    if (elem.name == "create"):
        if w.findByName("createTitle") is None:
            clearScreen(w)
            openCreateDialog(w)
        if (w.findByName("load").isClicked == True):
            changeClickedState(w.findByName("load"))
    else:
        if (w.findByName("loadTitle") is None):
            clearScreen(w)
            openLoadDialog(w)
        if (w.findByName("create").isClicked == True):
            changeClickedState(w.findByName("create"))
    w.update()

def openLoadDialog(w):
    clearScreen(w)
    w.addElem(text("loadTitle", "Load an existing project", 210 , 10, colors.dark_gray, 30))
    w.addElem(text("projectName", "Project's file", 210, 50, colors.dark_gray, 23))
    w.addElem(buttonColored("editText", "|", 210, 80, 210, 30, colors.dark_gray, colors.gray ,25))
    w.addElem(buttonColored("validate", "Open", 210, 120, 100, 30, colors.dark_gray, colors.gray, 25))

def openCreateDialog(w):
    w.addElem(text("createTitle", "Create a new project", 210 , 10, colors.dark_gray, 30))
    w.addElem(text("projectName", "Project's name", 210, 50, colors.dark_gray, 23))
    w.addElem(buttonColored("editText", "|", 210, 80, 210, 30, colors.dark_gray, colors.gray ,25))
    w.addElem(buttonColored("validate", "Create", 210, 120, 100, 30, colors.dark_gray, colors.gray, 25))
    w.findByName("validate").onClick = createDialogListener
    w.findByName("editText").onClick = createDialogListener

def drawLeftMenu(w):
    w.addElem(shape("bg_left_menu", colors.gray, 0, 0, 200, 600))
    w.addElem(text("projects", "Projects", 10,5, colors.dark_gray, 30))
 
    w.addElem(buttonColored("load", "Load Project", 0, 45, 200, 40, 
                           colors.dark_gray, colors.gray, 24))

    w.addElem(buttonColored("create", "Create Project", 0, 90, 200, 40,
                            colors.dark_gray, colors.gray, 24))
    w.findByName("load").onClick = leftMenuClickListener
    w.findByName("create").onClick = leftMenuClickListener
 
def main():
    pygame.init()
    w = window(800, 600, "EasyPygame - GUI 0.1", "res/icon.png")
    w.setBackgroundColor(colors.white)
    drawLeftMenu(w)
    w.loop(basicHandler.handler)

main()
