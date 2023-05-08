from ClaseMateria import Materia
from ClaseAlumno import Alumno
from manejadorAlumnos import ManejadorAlumnos

import csv

class ManejadorMaterias:
    def __init__(self):
        self.materias = []

    def promedio_con_aplazos(self, dni):
        alumno = self.buscar_alumno_por_dni(dni)
        if not alumno:
            return None
        notas = []
        for materia in manejador_materias.materias:
            if materia.dni == dni and (materia.aprobacion == 'E' or materia.aprobacion == 'X' or materia.nota < 4):
                notas.append(materia.nota)
        if not notas:
            return None
        promedio = sum(notas) / len(notas)
        return promedio
    def agregarMateria(self, archivo):
        with open(archivo) as f:
            for linea in f:
                datos = linea.strip().split(",")
                dni = int(datos[0])
                materia = datos[1]
                fecha = datos[2]
                nota = float(datos[3])
                aprobacion = datos[4]
                alumno = manejadorAlumnos.buscar_por_dni(dni)
                if alumno:
                    alumno.agregar_materia_aprobada(materia, fecha, nota, aprobacion)
                    self.materias.append((alumno, materia, fecha, nota, aprobacion))


    def testManejadorMaterias(self):
        archivo = open('materiasAprobadas.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            dni = int(fila[0])
            materia = fila[1]
            fecha = fila[2]
            nota = float(fila[3])
            aprobacion = fila[4]
            unaMateria = Materia(dni, materia, fecha, nota, aprobacion)
            self.agregarMateria(unaMateria)
        archivo.close()


    def listar_por_materia(self, materia):
        aprobados = [(a.dni, a.apellido, a.nombre, fecha, nota, a.anio) for (a, m, fecha, nota, aprobacion) in self.materias if m == materia and aprobacion == 'P' and nota >= 7]
        return aprobados