
import tkinter as tk
from tkinter import messagebox

class LoanApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Préstamo de Libros")
        self.geometry("600x400")#tkinter dimencion ventana
        
        self.label_book_id = tk.Label(self, text="ID del Libro:")
        self.entry_book_id = tk.Entry(self)
        self.label_book_id.grid(row=0, column=0, padx=10, pady=5)
        self.entry_book_id.grid(row=0, column=1, padx=10, pady=5)
        
        self.label_user_id = tk.Label(self, text="ID del Usuario:")
        self.entry_user_id = tk.Entry(self)
        self.label_user_id.grid(row=1, column=0, padx=10, pady=5)
        self.entry_user_id.grid(row=1, column=1, padx=10, pady=5)
        
        self.button_loan = tk.Button(self, text="Realizar Préstamo", command=self.perform_loan)
        self.button_loan.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def perform_loan(self):
        book_id = self.entry_book_id.get()
        user_id = self.entry_user_id.get()
        #loan_date = # Obtener la fecha actual
        
        loan = Loan(book_id, user_id) #loan_date)
        loan.save_to_database()
        messagebox.showinfo("Éxito", "Préstamo realizado correctamente.")

if __name__ == "__main__":
    app = LoanApplication()
    app.mainloop()