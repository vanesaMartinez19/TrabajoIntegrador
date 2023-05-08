from manejadorAlumnos import ManejadorAlumnos
from ClaseManejadorMaterias import ManejadorMaterias

def Test():
    print('hola')



if __name__ == '__main__':
    mAlumnos = ManejadorAlumnos()
    mAlumnos.testManejadorAlumnos()
    print(mAlumnos)
    mMateriaAp = ManejadorMaterias()
    mMateriaAp.testManejadorMaterias()
    print(mMateriaAp)

    while True:
        print("Seleccione una opción:")
        print("a- Consultar Promedio con aplazos y sin aplazos de un alumno")
        print("b- Estudiantes que aprobaron en forma promocional una materia con nota mayor o igual a 7")
        print("c- Listado de alumnos ordenado por año que cursan y alfabeticamente por apellido y nombre")
        print("d- Salir")
        opcion = input()

        if opcion == "a":
            m = int(input("Ingrese DNI del alumno: "))
            promedio=mMateriaAp.promedio_con_aplazos()
            print("Millas acumuladas:", promedio)

        elif opcion == "b":
            mat = int(input("Ingrese la materia a buscar: "))
            print("materias:", mMateriaAp.listar_por_materia(mat))
        elif opcion == "c":
            print("listado:", mMateriaAp.listar_por_anio())




