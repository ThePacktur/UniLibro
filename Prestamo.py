from Usuario import Estudiante, Docente
from datetime import datetime, timedelta

class Prestamo:
    MULTA_POR_DIA = 1000

    def __init__(self, libro, usuario, fecha_prestamo):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = self.calcular_fecha_devolucion()
        self.renovaciones = 0

    def calcular_fecha_devolucion(self):
        if isinstance(self.usuario, Estudiante):
            return self.fecha_prestamo + timedelta(days=Estudiante.DIAS_PRESTAMO)
        elif isinstance(self.usuario, Docente):
            return self.fecha_prestamo + timedelta(days=Docente.DIAS_MIN_PRESTAMO)

    def renovar(self):
        if isinstance(self.usuario, Estudiante) and self.renovaciones < 1:
            self.fecha_devolucion += timedelta(days=Estudiante.RENOVACION_MAX_DIAS)
            self.renovaciones += 1
        elif isinstance(self.usuario, Docente) and self.renovaciones < Docente.RENOVACIONES_MAX:
            self.fecha_devolucion += timedelta(days=Docente.DIAS_MIN_PRESTAMO)
            self.renovaciones += 1

    def retrasado(self):
        return datetime.now().date() > self.fecha_devolucion

    @property
    def multa(self):
        if self.retrasado():
            dias_retraso = (datetime.now().date() - self.fecha_devolucion).days
            return dias_retraso * self.MULTA_POR_DIA
        return 0
