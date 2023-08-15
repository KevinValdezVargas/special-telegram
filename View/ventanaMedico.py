from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.mantenimientoMedico import *
from Controller.controllerMedico import *

aMed = arregloMedico()

class ventanaMedico(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(ventanaMedico,self).__init__(parent)
        uic.loadUi("UI/ventanaMedico.ui",self)
        #COLOCAR LOS BOTONES(btn)
        self.listarDatos()
        self.show()

    def obtenerCodigo(self):
        return self
    
    def obtenerNombres(self):
        return self
    
    def obtenerApellidos(self):
        return self
    
    def obtenerCmp(self):
        return self
    
    def obtenerIdEspecialidad(self):
        return self
    
    def listarDatos(self):
        self #COLOCAR LOS TABLES(tbl)

    def grabar(self):
        try:
            pos = aMed.buscarMedico(self.obtenerCodigo())
            objMed = aMed.devolverMedico(pos)
            objMed.setNombres(self.obtenerNombres())
            objMed.setApellidos(self.obtenerApellidos())
            objMed.setCmp(self.obtenerCmp())
            objMed.setIdEspecialidad(self.obtenerIdEspecialidad())
            aMed.grabar()
            self.listarDatos()
        except:
            QtWidgets.QMessageBox.information(self,"Registrar medico", 
            "Ha ocurrido un error al registrar el cliente", QtWidgets.QMessageBox.Ok)

    def registrar(self):

        objMed = controllerMedico(self.obtenerCodigo(),self.obtenerNombres(),
                                  self.obtenerApellidos(),self.obtenerCmp(),self.obtenerIdEspecialidad)
        aMed.adicionarMedico(objMed)
        aMed.grabar()
        self.listarDatos()
        QtWidgets.QMessageBox.information(self, "Registar medico",
            "Medico registrado con exito!", QtWidgets.QMessageBox.Ok)
        
    def eliminar(self):

        if aMed.tamañoMantenimientoMedico() == 0:
            QtWidgets.QMessageBox.information(self, "Elimar medico", "No existen medicos a eliminar!", QtWidgets.QMessageBox.Ok)

        else:
            fila = self.tblMedicos.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                codigo = self.tblMedicos.item(indiceFila, 0).text()
                pos = aMed.buscarMedico(codigo)
                aMed.grabar()
                self.listarDatos()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar medico", "Debe seleccionar una fila", QtWidgets.QMessageBox.Ok)

    def modificar(self):

        if aMed.tamañoMantenimientoMedico() == 0:
            QtWidgets.QMessageBox.information(self,"Modificando medicos", "No se encontraron registros al codigo ingresado", QtWidgets.QMessageBox.Ok)

        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self,"Modificar medico", "Ingrese el codigo a modificar")

            pos = aMed.buscarMedico(codigo)
            if pos != -1:
                objMed = aMed.devolverMedico(pos)
                self
                self
                self
                self
                self