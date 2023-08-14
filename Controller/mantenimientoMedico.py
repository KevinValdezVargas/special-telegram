from Controller.controllerMedico import *

class arregloMedico:

    def __init__(self):
        self.dataMedico = []
        self.cargar()

    def adicionarMedico(self, objMed):
        self.dataMedico.append(objMed)

    def devolverMedico(self, pos):
        return self.dataMedico[pos]
    
    def tamañoMantenimientoMedico(self):
        return len(self.dataMedico)
    
    def buscarMedico(self, codigo):
        for i in range(self.tamañoMantenimientoMedico()):
            if codigo == self.dataMedico[i].getCodigo():
                return i
        return -1
    
    def eliminarMedico(self, indice):
        del(self.dataMedico[indice])

    def modificarMedico(self, objMed, pos):
        self.dataMedico[pos]=objMed
    
    def retonarDatos(self):
        return self.dataMedico
    
    def cargar(self):
        archivo = open("Model/medico.txt", "r", encoding="UTF-8")

        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna[0]
            nombres = columna[1]
            apellidos = columna[2]
            cmp = columna[3]
            idEspecialidad = columna[4].strip()
            objMed = controllerMedico(codigo, nombres, apellidos, cmp, idEspecialidad)
            self.adicionarMedico(objMed)
        archivo.close()

    def grabar(self):
        archivo = open("Model/medico.txt", "w+", encoding="UTF-8")
        for i in range(self.tamañoMantenimientoMedico()):
            archivo.write(str(self.devolverMedico(i).getCodigo()) + ","
                + str(self.devolverMedico(i).getNombres()) + ","
                + str(self.devolverMedico(i).getApellidos()) + ","
                + str(self.devolverMedico(i).getCmp()) + ","
                + str(self.devolverMedico(i).getIdEspecialidad()) + "\n")
        archivo.close()