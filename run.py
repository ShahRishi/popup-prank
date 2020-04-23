from pynput.keyboard import Key, Listener
from PIL import Image, ImageTk
import threading
import tkinter as tk

threads = {}

def Open():
    window = tk.Tk()
    window.title("Astley")
    window.geometry("275x183")
    window.configure(background='grey')
    img = ImageTk.PhotoImage(Image.open("images/astley.jpg"), master=window)
    panel = tk.Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.attributes("-topmost", True)
    window.mainloop()

def on_press(key):
    try:
        KEY = key.char.lower()
        if KEY in ['b', 'o', 'i']:
            thread_id = len(threads) + 1
            threads[thread_id] = threading.Thread(target=Open)
            threads[thread_id].start()
    except:
            pass
    return True

with Listener(on_press=on_press) as listener:
    listener.join()
