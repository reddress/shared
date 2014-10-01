import os
from pyrobot import Robot

os.chdir("c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/pontual/robo/")
robot = Robot()

robot.set_mouse_pos(40, 40)
robot.click_mouse(button="left")

robot.press_and_release("F9")
