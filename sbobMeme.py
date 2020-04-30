import tkinter as tk
import pyperclip

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 200, height = 100)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(100, 10, window=entry1)

def spongeText ():  
    x1 = entry1.get()

    memeString = []
    [memeString.append(v.upper()) if i % 2 != 0 else memeString.append(v.lower()) for i,v in enumerate(x1)]
    pyperclip.copy(''.join(memeString))

    #message1 = tk.Message(root, text=''.join(memeString))
    #message1.pack(fill=tk.BOTH, expand=True)

    #label1 = tk.Label(root, text=''.join(memeString))
    #label1.pack(fill=tk.BOTH, expand=True)
    #canvas1.create_window(200, 230, window=label1)
    
button1 = tk.Button(text='sPoNgEmEmE tHiS $hIt', command=spongeText)
canvas1.create_window(100, 30, window=button1)

root.mainloop()