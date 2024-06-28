import tkinter as tk
from tkinter import messagebox
from Sistema import Sistema

class BibliotecaGUI:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Sistema de Préstamos de Biblioteca")
        self.crear_widgets()

    def crear_widgets(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.libros_menu = tk.Menu(self.menu)
        self.usuarios_menu = tk.Menu(self.menu)
        self.prestamos_menu = tk.Menu(self.menu)

        self.menu.add_cascade(label="Libros", menu=self.libros_menu)
        self.menu.add_cascade(label="Usuarios", menu=self.usuarios_menu)
        self.menu.add_cascade(label="Préstamos", menu=self.prestamos_menu)

        self.libros_menu.add_command(label="Agregar Libro", command=self.agregar_libro)
        self.libros_menu.add_command(label="Modificar Stock", command=self.modificar_stock)

        self.usuarios_menu.add_command(label="Registrar Usuario", command=self.registrar_usuario)
        self.usuarios_menu.add_command(label="Buscar Usuario", command=self.buscar_usuario)

        self.prestamos_menu.add_command(label="Realizar Préstamo", command=self.realizar_prestamo)
        self.prestamos_menu.add_command(label="Registrar Pago Multa", command=self.registrar_pago_multa)

    def agregar_libro(self):
        self.limpiar_frame()
        tk.Label(self.root, text="Código").grid(row=0)
        tk.Label(self.root, text="Título").grid(row=1)
        tk.Label(self.root, text="Autor").grid(row=2)
        tk.Label(self.root, text="Stock").grid(row=3)

        codigo = tk.Entry(self.root)
        titulo = tk.Entry(self.root)
        autor = tk.Entry(self.root)
        stock = tk.Entry(self.root)

        codigo.grid(row=0, column=1)
        titulo.grid(row=1, column=1)
        autor.grid(row=2, column=1)
        stock.grid(row=3, column=1)

        tk.Button(self.root, text="Agregar", command=lambda: self.sistema.registrar_libro(codigo.get(), titulo.get(), autor.get(), int(stock.get()))).grid(row=4, columnspan=2)
        tk.Button(self.root, text="Volver", command=self.limpiar_frame).grid(row=5, columnspan=2)

    def modificar_stock(self):
        self.limpiar_frame()
        tk.Label(self.root, text="Código").grid(row=0)
        tk.Label(self.root, text="Nuevo Stock").grid(row=1)

        codigo = tk.Entry(self.root)
        stock = tk.Entry(self.root)

        codigo.grid(row=0, column=1)
        stock.grid(row=1, column=1)

        tk.Button(self.root, text="Modificar", command=lambda: self.sistema.modificar_stock(codigo.get(), int(stock.get()))).grid(row=2, columnspan=2)
        tk.Button(self.root, text="Volver", command=self.limpiar_frame).grid(row=3, columnspan=2)

    def registrar_usuario(self):
        self.limpiar_frame()
        tk.Label(self.root, text="Tipo").grid(row=0)
        tk.Label(self.root, text="Nombre").grid(row=1)
        tk.Label(self.root, text="RUT").grid(row=2)
        tk.Label(self.root, text="Contacto").grid(row=3)

        tipo = tk.Entry(self.root)
        nombre = tk.Entry(self.root)
        rut = tk.Entry(self.root)
        contacto = tk.Entry(self.root)

        tipo.grid(row=0, column=1)
        nombre.grid(row=1, column=1)
        rut.grid(row=2, column=1)
        contacto.grid(row=3, column=1)

        tk.Button(self.root, text="Registrar", command=lambda: self.sistema.registrar_usuario(tipo.get(), nombre.get(), rut.get(), contacto.get())).grid(row=4, columnspan=2)
        tk.Button(self.root, text="Volver", command=self.limpiar_frame).grid(row=5, columnspan=2)

    def buscar_usuario(self):
        self.limpiar_frame()
        tk.Label(self.root, text="RUT").grid(row=0)
        
        rut = tk.Entry(self.root)
        rut.grid(row=0, column=1)

        tk.Button(self.root, text="Buscar", command=lambda: self.mostrar_informacion_usuario(rut.get())).grid(row=1, columnspan=2)
        tk.Button(self.root, text="Volver", command=self.limpiar_frame).grid(row=2, columnspan=2)

    def mostrar_informacion_usuario(self, rut):
        self.limpiar_frame()
        usuario = self.sistema.buscar_usuario(rut)
        if usuario:
            tk.Label(self.root, text=f"Nombre: {usuario.nombre}").grid(row=0)
            tk.Label(self.root, text=f"RUT: {usuario.rut}").grid(row=1)
            tk.Label(self.root, text=f"Contacto: {usuario.contacto}").grid(row=2)
            tk.Label(self.root, text="Préstamos:").grid(row=3)
            
            for i, prestamo in enumerate(usuario.prestamos):
                tk.Label(self.root, text=f"{prestamo.libro.titulo} - {prestamo.fecha_prestamo} a {prestamo.fecha_devolucion}").grid(row=4+i)
            
            tk.Label(self.root, text="Deudas:").grid(row=4+len(usuario.prestamos))
            for i, prestamo in enumerate(usuario.prestamos):
                if prestamo.retrasado():
                    tk.Label(self.root, text=f"{prestamo.libro.titulo} - Multa: ${prestamo.multa}").grid(row=5+len(usuario.prestamos)+i)
        else:
            tk.Label(self.root, text="Usuario no encontrado").grid(row=0)

        tk.Button(self.root, text="Volver", command=self.limpiar_frame).grid(row=6+len(usuario.prestamos), columnspan=2)

    def realizar_prestamo(self):
        self.limpiar_frame()
        tk.Label(self.root, text="RUT").grid(row=0)
        tk.Label(self.root, text="Código Libro").grid(row=1)

        rut = tk.Entry(self.root)
        codigo = tk.Entry(self.root)

        rut.grid(row=0, column=1)
        codigo.grid(row=1, column=1)

        tk.Button(self.root, text="Prestar", command=lambda: self.mostrar_prestamo(self.sistema.realizar_prestamo(rut.get(), codigo.get()))).grid(row=2, columnspan=2)
        tk.Button(self.root, text="Volver", command=self.limpiar_frame).grid(row=3, columnspan=2)

    def mostrar_prestamo(self, prestamo):
        self.limpiar_frame()
        if prestamo:
            tk.Label(self.root, text=f"Libro: {prestamo.libro.titulo}").grid(row=0)
            tk.Label(self.root, text=f"Usuario: {prestamo.usuario.nombre}").grid(row=1)
            tk.Label(self.root, text=f"Fecha Préstamo: {prestamo.fecha_prestamo}").grid(row=2)
            tk.Label(self.root, text=f"Fecha Devolución: {prestamo.fecha_devolucion}").grid(row=3)
        else:
            tk.Label(self.root, text="Préstamo no realizado").grid(row=0)
        
        tk.Button(self.root, text="Volver", command=self.limpiar_frame).grid(row=4, columnspan=2)

    def registrar_pago_multa(self):
        self.limpiar_frame()
        tk.Label(self.root, text="RUT").grid(row=0)
        
        rut = tk.Entry(self.root)
        rut.grid(row=0, column=1)

        tk.Button(self.root, text="Registrar Pago", command=lambda: self.sistema.registrar_pago_multa(rut.get())).grid(row=1, columnspan=2)
        tk.Button(self.root, text="Volver", command=self.limpiar_frame).grid(row=2, columnspan=2)

    def limpiar_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.crear_widgets()
