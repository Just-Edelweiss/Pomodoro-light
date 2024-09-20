import tkinter as tk
from tkinter import ttk


# constants
titre = "Pomodoro"
size = "720x480"
offset = "+1100+100"

fontname = "Poppins SemiBold"
fontsizetitle = 35

def test():
    print(entry_int.get())

# initialise window
root = tk.Tk()

root.title(titre)
root.geometry(size + offset)

# texts
main_title = ttk.Label(
    master = root, text = "Choose your time", font = (fontname, fontsizetitle)
    )
main_title.pack()

# input
input_frame = ttk.Frame(master = root)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button1 = ttk.Button(master = input_frame, text = "OK", command = test)
entry.pack(side = "left", padx=10)
button1.pack()
input_frame.pack(pady = 50)

start_frame = ttk.Frame(master = root)
button2 = ttk.Button(master = start_frame, text = 'Start')
button2.pack(pady = 10)
start_frame.pack()


# run
root.mainloop()
