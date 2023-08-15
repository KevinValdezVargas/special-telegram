from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.mantenimientoArea import *
from Controller.controllerArea import *

aArea = arregloArea()

class ventanaArea(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(ventanaArea,self).__init__(parent)
        uic.loadUi("UI/ventanaArea.ui",self)
        #COLOCAR LOS BOTONES(btn)
        self.listarDatos()
        self.show()
    
    def obtenerIdArea(self):
        return self

    def obtenerNumeroOficinas(self):
        return self

    def obtenerNumeroCamas(self):
        return self
    
    def obtenerMt2(self):
        return self

    def listarDatos(self):
        self.tblAreas.setRowCount(aArea.tamañoMantenimientoArea())
        self.tblAreas.setColumCount(4)
        self.tblAreas.verticalHeader().setVisible(False)

        for i in range(0, aArea.tamañoMantenimientoArea()):
            self.tblAreas.setItem(i,0,QtWidgets.QTableWidgetItem(aArea.devolverArea(i).getIdArea()))
            self.tblAreas.setItem(i,1,QtWidgets.QTableWidgetItem(aArea.devolverArea(i).getNumeroOficinas()))
            self.tblAreas.setItem(i,2,QtWidgets.QTableWidgetItem(aArea.devolverArea(i).getNumeroCamas()))
            self.tblAreas.setItem(i,3,QtWidgets.QTableWidgetItem(aArea.devolverArea(i).getMt2()))
    
    def grabar(self):
        try:
            pos = aArea.buscarArea(self.obtenerIdArea())
            objArea = aArea.devolverArea(pos)
            objArea.setNumeroOficinas(self.obtenerNumeroOficinas())
            objArea.setNumeroCamas(self.obtenerNumeroCamas())
            objArea.setMt2(self.obtenerMt2())
            aArea.grabar()
            self.listarDatos()
        except:
            QtWidgets.QMessageBox.information(self,"Registrar Área", "Ha ocurrido un error al registrar el Área", QtWidgets.QMessageBox.Ok)
    
    def registrar(self):
        objArea = controllerArea(self.obtenerIdArea(), self.obtenerNumeroOficinas(), self.obtenerNumeroCamas(), self.obtenerMt2())
        aArea.adicionarArea(objArea)
        aArea.grabar()
        self.ListarDatos()
        QtWidgets.QMessageBox.information(self,"Registrar Área",
        "Área Registrada con Exito", QtWidgets.QMessageBox.Ok)

    def eliminar(self):
        if aArea.tamañoMantenimientoArea() == 0:
             QtWidgets.QMessageBox.information(self,"Eliminar Área",
            "No existe Área seleccionada para eliminar", QtWidgets.QMessageBox.Ok)
        else: 
            fila = self.tblAreas.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                idArea = self.tblAreas.item(indiceFila, 0).text()
                pos = aArea.buscarArea(idArea)
                aArea.eliminarArea(pos)
                aArea.grabar()
                self.listarDatos
            else:
                QtWidgets.QMessageBox.information(self,"Eliminar Área",
                "Hubo un error al tratar de eliminar el área", QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aArea.tamañoMantenimientoArea() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Área...",
            "No se encontraron registros para el ID Ingresado a buscar", QtWidgets.QMessageBox.Ok)
        else:
            idArea, _ =QtWidgets.QInputDialog.getText(self,"Buscar Área", "Ingrese el ID a Modificar")
            pos = aArea.buscarArea(idArea)

            if pos != -1:
                objArea = aArea.devolverArea(pos)
                self.txt.setText(objArea.getIdArea())
                self.txt.setText(objArea.getNumeroOficinas())
                self.txt.setText(objArea.getNumeroCamas())
                self.txt.setText(objArea.getMt2())