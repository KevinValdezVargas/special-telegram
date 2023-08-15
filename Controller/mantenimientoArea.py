from Controller.controllerArea import *

class arregloArea:

    def __init__(self):
        self.dataArea = []
        self.cargar()

    def adicionarArea(self, objArea):
        self.dataArea.append(objArea)

    def devolverArea(self, pos):
        return self.dataArea[pos]
    
    def tamañoMantenimientoArea(self):
        return len(self.dataArea)

    def buscarArea(self, idArea):
        for i in range(self.tamañoMantenimientoArea()):
            if idArea == self.dataArea[i].getIdArea():
                return i
        return -1

    def eliminarArea(self, indice):
        del(self.dataArea[indice])

    def modificarArea(self, objArea, pos):
        self.dataArea[pos]=objArea
    
    def retonarDatos(self):
        return self.dataArea

    def cargar(self):
        archivo = open("Model/area.txt","r",encoding="UTF-8")

        for linea in archivo.readlines():
            columna = str(linea).split(",")
            idArea = columna[0]
            numeroOficinas = columna[1]
            numeroCamas = columna[2]
            mt2 = columna[3].strip()
            objArea = controllerArea(idArea, numeroOficinas, numeroCamas, mt2)
            self.adicionarArea(objArea)
        archivo.close()

    def grabar(self):
        archivo = open("Model/area.txt", "w+", encoding="UTF-8")
        for i in range(self.tamañoMantenimientoArea()):
            archivo.write(str(self.devolverCliente(i).getDni()) + ","
            + str(self.devolverArea(i).getnumeroOficinas()) + ","
            + str(self.devolverArea(i).getnumeroCamas()) + ","
            + str(self.devolverArea(i).getMt2()) + "\n")
        archivo.close()