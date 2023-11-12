import pyautogui
import time

# Temps de pause entre chaque appui sur la touche Z (en secondes)
a = int(input("pause_between_keypresses"))
# Nombre de fois que la touche Z sera pressée
b = int(input("number_of_keypresses"))
action = 0.0000000000001
c = int(input("point_ax"))
d = int(input("point_ay"))
e = "Ended !"

for _ in range(b):
    pyautogui.moveTo(c, d, duration=action)
    pyautogui.click()
    pyautogui.press('c')
    pyautogui.press('o')
    pyautogui.press('n')
    pyautogui.press('t')
    pyautogui.press('i')
    pyautogui.press('n')
    pyautogui.press('u')
    pyautogui.press('e')
    pyautogui.press('enter')
    time.sleep(a)
print (e)