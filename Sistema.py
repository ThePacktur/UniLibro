from Usuario import Estudiante, Docente
from Libro import Libro
from Prestamo import Prestamo
from datetime import datetime

class Sistema:
    def __init__(self):
        self.usuarios = {}
        self.libros = {}

    def registrar_usuario(self, tipo, nombre, rut, contacto):
        if tipo == "estudiante":
            usuario = Estudiante(nombre, rut, contacto)
        elif tipo == "docente":
            usuario = Docente(nombre, rut, contacto)
        self.usuarios[rut] = usuario

    def registrar_libro(self, codigo, titulo, autor, stock):
        libro = Libro(codigo, titulo, autor, stock)
        self.libros[codigo] = libro

    def realizar_prestamo(self, rut, codigo_libro):
        usuario = self.usuarios.get(rut)
        libro = self.libros.get(codigo_libro)
        if usuario and libro and libro.prestamo_disponible() and usuario.puede_prestar():
            fecha_prestamo = datetime.now().date()
            prestamo = Prestamo(libro, usuario, fecha_prestamo)
            usuario.agregar_prestamo(prestamo)
            libro.registrar_prestamo(prestamo)
            return prestamo
        return None

    def buscar_usuario(self, rut):
        return self.usuarios.get(rut)

    def buscar_libro(self, codigo):
        return self.libros.get(codigo)

    def registrar_pago_multa(self, rut):
        usuario = self.usuarios.get(rut)
        if usuario:
            usuario.multa = 0

    def modificar_stock(self, codigo_libro, nuevo_stock):
        libro = self.libros.get(codigo_libro)
        if libro:
            libro.stock = nuevo_stock
