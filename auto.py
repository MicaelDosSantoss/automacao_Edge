import pyautogui
from time import sleep
import json
import random


with open('pokemon.json','r') as pokemon_json:
    pokemons = json.load(pokemon_json)



pyautogui.press('winleft')
sleep(1)
pyautogui.write('Edge')
pyautogui.press('enter')
sleep(8)
i = 0

while i <= 30:
  
    al = random.choice(pokemons) 
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.write(al)
    pyautogui.press('enter')
    sleep(4)
    i += 1
    print(f"{i}")


# a = pyautogui.KEYBOARD_KEYS

# for t in a:
#     print(f"{t}")