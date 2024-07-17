import tkinter as tk
from tkinter import messagebox
from Sistema import Sistema

class BibliotecaGUI:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Sistema de Préstamos de Biblioteca")
        self.tipo_usuario = None  # Almacena el tipo de usuario logueado
        self.usuario_actual = None
        self.frame_contenido = tk.Frame(self.root, padx=20, pady=20)
        self.frame_contenido.pack(fill='both', expand=True)
        self.crear_pantalla_principal()

    def crear_pantalla_principal(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Bienvenido al Sistema de Préstamos de Biblioteca", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.frame_contenido, text="Iniciar Sesión", command=self.crear_pantalla_login, width=20, height=2).pack(pady=5)
        tk.Button(self.frame_contenido, text="Registrarse", command=self.crear_pantalla_registro, width=20, height=2).pack(pady=5)

    def crear_pantalla_login(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Iniciar Sesión", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="RUT:", font=("Arial", 12)).pack(pady=5)
        rut = tk.Entry(self.frame_contenido, width=30)
        rut.pack(pady=5)

        tk.Label(self.frame_contenido, text="Contraseña:", font=("Arial", 12)).pack(pady=5)
        contrasena = tk.Entry(self.frame_contenido, show='*', width=30)
        contrasena.pack(pady=5)

        tk.Button(self.frame_contenido, text="Iniciar Sesión", command=lambda: self.iniciar_sesion(rut.get(), contrasena.get()), width=15).pack(pady=20)
        tk.Button(self.frame_contenido, text="Volver", command=self.crear_pantalla_principal, width=15).pack(pady=5)

    def crear_pantalla_registro(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Registrarse", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="Tipo de Usuario:", font=("Arial", 12)).pack(pady=5)
        tipo_usuario = tk.Entry(self.frame_contenido, width=30)
        tipo_usuario.pack(pady=5)

        tk.Label(self.frame_contenido, text="Nombre:", font=("Arial", 12)).pack(pady=5)
        nombre = tk.Entry(self.frame_contenido, width=30)
        nombre.pack(pady=5)

        tk.Label(self.frame_contenido, text="RUT:", font=("Arial", 12)).pack(pady=5)
        rut = tk.Entry(self.frame_contenido, width=30)
        rut.pack(pady=5)

        tk.Label(self.frame_contenido, text="Contacto:", font=("Arial", 12)).pack(pady=5)
        contacto = tk.Entry(self.frame_contenido, width=30)
        contacto.pack(pady=5)

        tk.Label(self.frame_contenido, text="Contraseña:", font=("Arial", 12)).pack(pady=5)
        contrasena = tk.Entry(self.frame_contenido, show='*', width=30)
        contrasena.pack(pady=5)

        tk.Button(self.frame_contenido, text="Registrar", command=lambda: self.registrar_usuario(tipo_usuario.get(), nombre.get(), rut.get(), contacto.get(), contrasena.get()), width=15).pack(pady=20)
        tk.Button(self.frame_contenido, text="Volver", command=self.crear_pantalla_principal, width=15).pack(pady=5)

    def iniciar_sesion(self, rut, contrasena):
        usuario = self.sistema.iniciar_sesion(rut, contrasena)
        if usuario:
            self.tipo_usuario = usuario['tipo']
            self.usuario_actual = usuario
            self.crear_menu()
        else:
            messagebox.showwarning("Error", "RUT o contraseña incorrectos")

    def registrar_usuario(self, tipo, nombre, rut, contacto, contrasena):
        exito = self.sistema.registrar_usuario(tipo, nombre, rut, contacto, contrasena)
        if exito:
            messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
            self.crear_pantalla_login()
        else:
            messagebox.showwarning("Error", "No se pudo registrar el usuario")

    def crear_menu(self):
        self.limpiar_frame()
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        volver_menu = tk.Menu(self.menu, tearoff=0)
        volver_menu.add_command(label="Volver", command=self.crear_pantalla_principal)
        self.menu.add_cascade(label="Opciones", menu=volver_menu)

        if self.tipo_usuario == "Administrador":
            self.libros_menu = tk.Menu(self.menu, tearoff=0)
            self.usuarios_menu = tk.Menu(self.menu, tearoff=0)
            self.prestamos_menu = tk.Menu(self.menu, tearoff=0)
            
            self.menu.add_cascade(label="Libros", menu=self.libros_menu)
            self.menu.add_cascade(label="Usuarios", menu=self.usuarios_menu)
            self.menu.add_cascade(label="Préstamos", menu=self.prestamos_menu)
            
            self.libros_menu.add_command(label="Agregar Libro", command=self.agregar_libro)
            self.libros_menu.add_command(label="Modificar Stock", command=self.modificar_stock)
            
            
            self.usuarios_menu.add_command(label="Buscar Usuario", command=self.buscar_usuario)
            
            self.prestamos_menu.add_command(label="Realizar Préstamo", command=self.realizar_prestamo)
            self.prestamos_menu.add_command(label="Registrar Pago Multa", command=self.registrar_pago_multa)
            self.prestamos_menu.add_command(label="Aplicar Multa", command=self.aplicar_multa)
        
        elif self.tipo_usuario == "Docente":
            self.prestamos_menu = tk.Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label="Préstamos", menu=self.prestamos_menu)
            self.prestamos_menu.add_command(label="Realizar Préstamo", command=self.realizar_prestamo)
            self.prestamos_menu.add_command(label="Devolver Libro", command=self.devolver_libro)
            self.prestamos_menu.add_command(label="Pagar Multa", command=self.pagar_multa_docente)

        elif self.tipo_usuario == "Estudiante":
            self.prestamos_menu = tk.Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label="Préstamos", menu=self.prestamos_menu)
            self.prestamos_menu.add_command(label="Realizar Préstamo", command=self.realizar_prestamo)
            self.prestamos_menu.add_command(label="Devolver Libro", command=self.devolver_libro)
            self.prestamos_menu.add_command(label="Pagar Multa", command=self.pagar_multa_estudiante)

    def agregar_libro(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Agregar Libro", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.frame_contenido, text="Código:", font=("Arial", 12)).grid(row=1, column=0, sticky='e')
        tk.Label(self.frame_contenido, text="Título:", font=("Arial", 12)).grid(row=2, column=0, sticky='e')
        tk.Label(self.frame_contenido, text="Autor:", font=("Arial", 12)).grid(row=3, column=0, sticky='e')
        tk.Label(self.frame_contenido, text="Stock:", font=("Arial", 12)).grid(row=4, column=0, sticky='e')

        codigo = tk.Entry(self.frame_contenido, width=30)
        titulo = tk.Entry(self.frame_contenido, width=30)
        autor = tk.Entry(self.frame_contenido, width=30)
        stock = tk.Entry(self.frame_contenido, width=30)

        codigo.grid(row=1, column=1)
        titulo.grid(row=2, column=1)
        autor.grid(row=3, column=1)
        stock.grid(row=4, column=1)

        tk.Button(self.frame_contenido, text="Agregar", command=lambda: self.guardar_libro(codigo.get(), titulo.get(), autor.get(), stock.get()), width=15).grid(row=5, columnspan=2, pady=10)

    def guardar_libro(self, codigo, titulo, autor, stock):
        self.sistema.registrar_libro(codigo, titulo, autor, int(stock))
        messagebox.showinfo("Éxito", "Libro agregado correctamente")
        self.crear_menu()

    def modificar_stock(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Modificar Stock", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="Código del Libro:", font=("Arial", 12)).pack(pady=5)
        codigo = tk.Entry(self.frame_contenido, width=30)
        codigo.pack(pady=5)

        tk.Label(self.frame_contenido, text="Nuevo Stock:", font=("Arial", 12)).pack(pady=5)
        nuevo_stock = tk.Entry(self.frame_contenido, width=30)
        nuevo_stock.pack(pady=5)

        tk.Button(self.frame_contenido, text="Modificar", command=lambda: self.guardar_modificacion_stock(codigo.get(), nuevo_stock.get()), width=15).pack(pady=20)

    def guardar_modificacion_stock(self, codigo, nuevo_stock):
        exito = self.sistema.modificar_stock_libro(codigo, int(nuevo_stock))
        if exito:
            messagebox.showinfo("Éxito", "Stock modificado correctamente")
            self.crear_menu()
        else:
            messagebox.showwarning("Error", "No se pudo modificar el stock")

    def realizar_prestamo(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Realizar Préstamo", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="RUT del Usuario:", font=("Arial", 12)).pack(pady=5)
        rut_usuario = tk.Entry(self.frame_contenido, width=30)
        rut_usuario.pack(pady=5)

        tk.Label(self.frame_contenido, text="Código del Libro:", font=("Arial", 12)).pack(pady=5)
        codigo_libro = tk.Entry(self.frame_contenido, width=30)
        codigo_libro.pack(pady=5)

        tk.Label(self.frame_contenido, text="Días de Préstamo:", font=("Arial", 12)).pack(pady=5)
        dias_prestamo = tk.Entry(self.frame_contenido, width=30)
        dias_prestamo.pack(pady=5)

        tk.Button(self.frame_contenido, text="Prestar", command=lambda: self.procesar_prestamo(rut_usuario.get(), codigo_libro.get(), dias_prestamo.get()), width=15).pack(pady=20)

    def procesar_prestamo(self, rut_usuario, codigo_libro, dias_prestamo):
        exito = self.sistema.prestar_libro(rut_usuario, codigo_libro, int(dias_prestamo))
        if exito:
            messagebox.showinfo("Éxito", "Préstamo realizado correctamente")
            self.crear_menu()
        else:
            messagebox.showwarning("Error", "No se pudo realizar el préstamo")

    def registrar_pago_multa(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Registrar Pago de Multa", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="RUT del Usuario:", font=("Arial", 12)).pack(pady=5)
        rut_usuario = tk.Entry(self.frame_contenido, width=30)
        rut_usuario.pack(pady=5)

        tk.Label(self.frame_contenido, text="Monto a Pagar:", font=("Arial", 12)).pack(pady=5)
        monto_pagar = tk.Entry(self.frame_contenido, width=30)
        monto_pagar.pack(pady=5)

        tk.Button(self.frame_contenido, text="Registrar Pago", command=lambda: self.procesar_pago_multa(rut_usuario.get(), float(monto_pagar.get())), width=15).pack(pady=20)

    def procesar_pago_multa(self, rut_usuario, monto_pagar):
        exito = self.sistema.pagar_multa(rut_usuario, monto_pagar)
        if exito:
            messagebox.showinfo("Éxito", "Pago de multa registrado correctamente")
            self.crear_menu()
        else:
            messagebox.showwarning("Error", "No se pudo registrar el pago de la multa")

    def aplicar_multa(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Aplicar Multa", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="RUT del Usuario:", font=("Arial", 12)).pack(pady=5)
        rut_usuario = tk.Entry(self.frame_contenido, width=30)
        rut_usuario.pack(pady=5)

        tk.Label(self.frame_contenido, text="Código del Libro:", font=("Arial", 12)).pack(pady=5)
        codigo_libro = tk.Entry(self.frame_contenido, width=30)
        codigo_libro.pack(pady=5)

        tk.Label(self.frame_contenido, text="Monto de la Multa:", font=("Arial", 12)).pack(pady=5)
        monto_multa = tk.Entry(self.frame_contenido, width=30)
        monto_multa.pack(pady=5)

        tk.Button(self.frame_contenido, text="Aplicar Multa", command=lambda: self.procesar_aplicar_multa(rut_usuario.get(), codigo_libro.get(), float(monto_multa.get())), width=15).pack(pady=20)

    def procesar_aplicar_multa(self, rut_usuario, codigo_libro, monto_multa):
        exito = self.sistema.aplicar_multa(rut_usuario, codigo_libro, monto_multa)
        if exito:
            messagebox.showinfo("Éxito", "Multa aplicada correctamente")
            self.crear_menu()
        else:
            messagebox.showwarning("Error", "No se pudo aplicar la multa")

    def devolver_libro(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Devolver Libro", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="Código del Libro:", font=("Arial", 12)).pack(pady=5)
        codigo_libro = tk.Entry(self.frame_contenido, width=30)
        codigo_libro.pack(pady=5)

        tk.Button(self.frame_contenido, text="Devolver", command=lambda: self.procesar_devolucion(codigo_libro.get()), width=15).pack(pady=20)

    def procesar_devolucion(self, codigo_libro):
        exito = self.sistema.devolver_libro(codigo_libro)
        if exito:
            messagebox.showinfo("Éxito", "Libro devuelto correctamente")
            self.crear_menu()
        else:
            messagebox.showwarning("Error", "No se pudo devolver el libro")

    def pagar_multa_docente(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Pagar Multa (Docente)", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="Monto de la Multa:", font=("Arial", 12)).pack(pady=5)
        monto_multa = tk.Entry(self.frame_contenido, width=30)
        monto_multa.pack(pady=5)

        tk.Button(self.frame_contenido, text="Pagar", command=lambda: self.procesar_pago_multa(self.usuario_actual['rut'], float(monto_multa.get())), width=15).pack(pady=20)

    def pagar_multa_estudiante(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Pagar Multa (Estudiante)", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="Monto de la Multa:", font=("Arial", 12)).pack(pady=5)
        monto_multa = tk.Entry(self.frame_contenido, width=30)
        monto_multa.pack(pady=5)

        tk.Button(self.frame_contenido, text="Pagar", command=lambda: self.procesar_pago_multa(self.usuario_actual['rut'], float(monto_multa.get())), width=15).pack(pady=20)

    def buscar_usuario(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Buscar Usuario", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="RUT del Usuario:", font=("Arial", 12)).pack(pady=5)
        rut_usuario = tk.Entry(self.frame_contenido, width=30)
        rut_usuario.pack(pady=5)

        tk.Button(self.frame_contenido, text="Buscar", command=lambda: self.procesar_busqueda_usuario(rut_usuario.get()), width=15).pack(pady=20)

    def procesar_busqueda_usuario(self, rut_usuario):
        usuario = self.sistema.buscar_usuario(rut_usuario)
        if usuario:
            info_usuario = f"Tipo: {usuario['tipo']}\nNombre: {usuario['nombre']}\nRUT: {usuario['rut']}\nContacto: {usuario['contacto']}"
            messagebox.showinfo("Usuario Encontrado", info_usuario)
        else:
            messagebox.showwarning("Error", "Usuario no encontrado")

    def limpiar_frame(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

# Crear una instancia del sistema y de la interfaz gráfica
sistema = Sistema()
root = tk.Tk()
app = BibliotecaGUI(root, sistema)
root.mainloop()
