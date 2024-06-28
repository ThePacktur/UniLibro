import tkinter as tk
from Sistema import Sistema
from gui import BibliotecaGUI

if __name__ == "__main__":
    root = tk.Tk()
    sistema = Sistema()
    gui = BibliotecaGUI(root, sistema)
    root.mainloop()
