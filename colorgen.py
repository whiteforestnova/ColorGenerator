import random
import tkinter as Tk
while True:
    hexcolornum1 = random.randrange(0, 2**24)
    hexcolor1 = hex(hexcolornum1)
    trucolor1 = "#" + hexcolor1[2:]
    print(trucolor1)

    root = Tk.Tk()
    root.configure(background=trucolor1)
    root.minsize(200, 200)
    root.maxsize(500, 500)
    root.geometry("300x300+50+50")
    input("press enter to continue:")