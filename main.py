import tkinter as tk

class Graf(tk.Frame) :
    def __init__(self, h, w, data):
        super().__init__()

        self.master.title("Graf")
        self.pack(fill = tk.BOTH, expand = True)

        canvas = tk.Canvas(self)
        canvas.configure(background="white")

        canvas.pack(fill = tk.BOTH, expand = True)


data = [[-10,100],[-9,81],[-8,64],[-7,49],[-6,36],[-5,25],[-4,16],
        [5,25],[6,36],[7,49],[8,64],[9,81],[10,100]]

def main() :
    window = tk.Tk()
    h, w = 400, 400
    g = Graf(h, w, data)
    window.geometry(str(w)+"x"+str(h)+"+100+100")

if __name__ == '__main__' :
    main()

