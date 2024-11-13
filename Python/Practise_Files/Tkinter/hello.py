import tkinter as tk

window = tk.Tk() #instanctiate an instance of a window
window.geometry("700x800")
window.title("Bro Code first GUI Program")

icon = tk.PhotoImage(file='image.png')
window.iconphoto(True, icon)
window.config(background="#B2BEB5")

window.mainloop() #place window of computer screen