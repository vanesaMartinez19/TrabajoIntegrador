class Materia:
    __dni = 0
    __materia = ''
    __fecha = ''
    __nota = 0.0
    __aprobacion = ''
    def __init__(self, dni, materia, fecha, nota, aprobacion):
        self.dni = dni
        self.materia = materia
        self.fecha = fecha
        self.nota = nota
        self.aprobacion = aprobacion

    def __str__(self):
        return f"{self.dni} {self.materia} {self.fecha} {self.nota} {self.aprobacion}"

    def __lt__(self, otro):
        if self.fecha != otro.fecha:
            return self.fecha < otro.fecha
        else:
            return self.nota < otro.nota