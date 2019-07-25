import subprocess
import pyautogui
from time import sleep

from secrets import LOJASENHA

# Pontual
subprocess.Popen(r'\\amazonia\Work\estoque\Pontual.exe')
sleep(3)
pyautogui.click(403, 347)
pyautogui.typewrite(LOJASENHA + "\n")
sleep(2)
pyautogui.click(145, 152)
sleep(1)
subprocess.run(r'C:\Users\Heitor\Desktop\code\tabelas-autoupload\winactivateloja.exe')
pyautogui.click(130, 100)

sleep(3)

# Uniao
subprocess.Popen(r'\\amazonia\Work\UNIAO\Pontual.exe')
sleep(3)
pyautogui.click(403, 347)
pyautogui.typewrite(LOJASENHA + "\n")
sleep(2)
pyautogui.click(145, 152)
sleep(1)
subprocess.run(r'C:\Users\Heitor\Desktop\code\tabelas-autoupload\winactivateloja.exe')
pyautogui.click(130, 100)
