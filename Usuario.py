class Usuario:
    def __init__(self, nombre, rut, contacto):
        self.nombre = nombre
        self.rut = rut
        self.contacto = contacto
        self.prestamos = []
        self.multa = 0

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def calcular_multa(self):
        return sum(p.multa for p in self.prestamos)

    def tiene_deudas(self):
        return any(p.retrasado() for p in self.prestamos) or self.calcular_multa() > 0

class Estudiante(Usuario):
    MAX_PRESTAMOS = 4
    DIAS_PRESTAMO = 7
    RENOVACION_MAX_DIAS = 3

    def puede_prestar(self):
        return len(self.prestamos) < self.MAX_PRESTAMOS and not self.tiene_deudas()

class Docente(Usuario):
    DIAS_MIN_PRESTAMO = 7
    DIAS_MAX_PRESTAMO = 20
    RENOVACIONES_MAX = 3

    def puede_prestar(self):
        return not self.tiene_deudas()
