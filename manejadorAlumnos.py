from ClaseAlumno import Alumno
import csv
import numpy as np
class ManejadorAlumnos:
    __cantidad = 0
    __dimension = 0
    __incremento = 10
    def __init__(self,dimension,incremento=10):
        self.__alumnos = np.empty(dimension,dtype=Alumno)
        self.__cantidad = 0
        self.__dimension = dimension

    def __str__(self):
        s = 'algo\n'
        for i in range(self.__cantidad):
            unAlumno = self.__alumnos[i]
            s += '{}'.format(i+1)+str(unAlumno)+'\n'
        return s

    def agregarAlumno(self,unAlumno):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad]= unAlumno
        self.__cantidad+= 1
    def testManejadorAlumnos(self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            dni = int(fila[0])
            apellido = fila[1]
            nombre = fila[2]
            carrera = fila[3]
            anio = int(fila[4])
            unAlumno = Alumno(dni, apellido, nombre, carrera, anio)
            self.agregarAlumno(unAlumno)
            #self.alumnos.append(unAlumno)
        archivo.close()

    def buscar_por_dni(self, dni):
        for alumno in self.alumnos:
            if alumno.dni == dni:
                return alumno
        return None

    def listar_por_anio(self):
        return sorted(self.alumnos)




