import keyboard
import webbrowser

def abrir_navegador():
    url = "https://jogandofoddaciptbr69burrinho.fandom.com/pt-br/wiki/JogandoFoddaci_Wiki" 
    webbrowser.open(url)
    print("Navegador aberto!")


keyboard.add_hotkey('ctrl+b', abrir_navegador)

keyboard.wait('esc')