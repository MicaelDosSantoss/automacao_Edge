import pyautogui # automatição é python
from time import sleep # para dar um intervalo para os comandos 
import json # Para a trnaformação de arquivos para json
import random # bliblioteca de randomização 


with open('pokemon.json','r') as pokemon_json: # esse with abre o arquivo json, é depois da um load em json para uma variavel
    pokemons = json.load(pokemon_json)



pyautogui.press('winleft') # pressionar uma tecla
sleep(1) # intervalo
pyautogui.write('Edge') # escrever
pyautogui.press('enter') 
sleep(8)
i = 0

while i <= 30:
  
    al = random.choice(pokemons) # pega um pokemon dos 1018
    pyautogui.hotkey('ctrl', 'e') # pressionar teclas, mais trás a possiblidade de inserir atalhos
    pyautogui.write(al)
    pyautogui.press('enter')
    sleep(4)
    i += 1
    print(f"{i}")


# a = pyautogui.KEYBOARD_KEYS

# for t in a:
#     print(f"{t}")