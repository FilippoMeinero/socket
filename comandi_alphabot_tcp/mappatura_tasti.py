from pynput import keyboard

def tasto_premuto(key):
    try:
        # Verifica se il tasto premuto è una lettera
        if key.char.isalpha():
            print(f'Tasto premuto: {key.char}')
    except AttributeError:
        # Ignora i tasti speciali (shift, ctrl...)
        pass

# avvia il listener per la tastiera
with keyboard.Listener(on_press=tasto_premuto) as listener:
    listener.join()
