import tkinter as tk

class Tegning(tk.Frame) :
    def __init__(self,h,w) :
        super().__init__()
        # Tegneinstruktioner

window = tk.Tk()
t = Tegning(100,400)
window.geometry("400x100+100+100")
window.mainloop()