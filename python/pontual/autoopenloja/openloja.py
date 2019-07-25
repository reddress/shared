import subprocess
import pyautogui
from time import sleep

from secrets import LOJASENHA

# Pontual
subprocess.Popen(r'\\amazonia\Work\estoque\Pontual.exe')
sleep(3)
pyautogui.click(403, 347)
pyautogui.typewrite(LOJASENHA + "\n")

sleep(3)

# Uniao
subprocess.Popen(r'\\amazonia\Work\UNIAO\Pontual.exe')
sleep(3)
pyautogui.click(403, 347)
pyautogui.typewrite(LOJASENHA + "\n")
