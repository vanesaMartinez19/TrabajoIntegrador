import numpy as np

# Clase Alumno
class Alumno:
    __dni = 0
    __apellido = ''
    __nombre = ''
    __carrera = ''
    __anio = 0

    def __init__(self, dni, apellido, nombre, carrera, anio):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.carrera = carrera
        self.anio = anio

    def __str__(self):
        return f"{self.dni} {self.apellido} {self.nombre} - {self.carrera} {self.anio}"

    def agregar_materia_aprobada(self, materia, fecha, nota, aprobacion):
        self.materias.append((materia, fecha, nota, aprobacion))

    def promedio_con_aplazos(self):
        notas = [nota for (_, _, nota, _) in self.materias]
        return np.mean(notas)

    def promedio_sin_aplazos(self):
        notas = [nota for (_, _, nota, _) in self.materias if nota >= 4]
        return np.mean(notas)

    def __lt__(self, otro):
        if self.anio == otro.anio:
            return self.apellido + self.nombre < otro.apellido + otro.nombre
        else:
            return self.anio < otro.anio

