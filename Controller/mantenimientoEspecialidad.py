from Controller.controllerEspecialidad import *

class arregloEspecialidad:

    def __init__(self):
        self.dataEspecialidad = []
        self.cargar()

    def adicionarEspecialidad(self, objEspe):
        self.dataEspecialidad.append(objEspe)

    def devolverEspecialidad(self, pos):
        return self.dataEspecialidad[pos]
    
    def tamañoMantenimientoEspecialidad(self):
        return len(self.dataEspecialidad)

    def buscarEspecialidad(self, idEspecialidad):
        for i in range(self.tamañoMantenimientoEspecialidad()):
            if idEspecialidad == self.dataArea[i].getIdEspecialidad():
                return i
        return -1

    def eliminarEspecialidad(self, indice):
        del(self.dataEspecialidad[indice])

    def modificarEspecialidad(self, objEspecialidad, pos):
        self.dataEspecialidad[pos]=objEspecialidad
    
    def retonarDatos(self):
        return self.dataEspecialidad

    def cargar(self):
        archivo = open("Model/especialidad.txt","r",encoding="UTF-8")

        for linea in archivo.readlines():
            columna = str(linea).split(",")
            idEspecialidad = columna[0]
            especialidad = columna[1].strip()
            objEspecialidad = controllerEspecialidad(idEspecialidad, especialidad)
            self.adicionarEspecialidad(objEspecialidad)
        archivo.close()

    def grabar(self):
        archivo = open("Model/especialidad.txt", "w+", encoding="UTF-8")
        for i in range(self.tamañoMantenimientoEspecialidad()):
            archivo.write(str(self.devolverEspecialidad(i).getIdEspecialidad()) + ","
            + str(self.devolverEspecialidad(i).getEspecialidad()) + "\n")
        archivo.close()