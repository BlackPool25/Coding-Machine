import tkinter as tk

root = tk.Tk()

root.geometry("800x800")
root.title("My First GUI")

label = tk.Label(root, text = "Hello World!", font=("Monotype Corsiva", 21))
label.pack()

root.mainloop()