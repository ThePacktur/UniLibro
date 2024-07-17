class Sistema:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.prestamos = {}
        self.multa = {}

    def registrar_libro(self, codigo, titulo, autor, stock):
        self.libros[codigo] = {'titulo': titulo, 'autor': autor, 'stock': stock}

    def registrar_usuario(self, tipo, nombre, rut, contacto):
        self.usuarios[rut] = {'tipo': tipo, 'nombre': nombre, 'contacto': contacto, 'multa': 0}

    def realizar_prestamo(self, rut, codigo_libro):
        if rut in self.usuarios and codigo_libro in self.libros and self.libros[codigo_libro]['stock'] > 0:
            self.libros[codigo_libro]['stock'] -= 1
            self.prestamos[(rut, codigo_libro)] = True
            return True
        return False

    def devolver_prestamo(self, rut, codigo_libro):
        if (rut, codigo_libro) in self.prestamos:
            self.libros[codigo_libro]['stock'] += 1
            del self.prestamos[(rut, codigo_libro)]
            return True
        return False

    def buscar_usuario(self, rut):
        return self.usuarios.get(rut, None)

    def registrar_pago_multa(self, rut):
        if rut in self.usuarios:
            self.usuarios[rut]['multa'] = 0

    def modificar_stock(self, codigo_libro, nuevo_stock):
        if codigo_libro in self.libros:
            self.libros[codigo_libro]['stock'] = nuevo_stock

    def aplicar_multa(self, rut, monto_multa):
        if rut in self.usuarios:
            self.usuarios[rut]['multa'] += monto_multa