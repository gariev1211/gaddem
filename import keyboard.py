import  keyboard
def escrever():
    print("Você pressionou a tecla Alt!")
keyboard.add_hotkey('alt',escrever)
keyboard.wait('esc')