from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.mantenimientoEspecialidad import *
from Controller.controllerEspecialidad import *

aEspe = arregloEspecialidad()

class ventanaEspecialidad(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(ventanaEspecialidad,self).__init__(parent)
        uic.loadUi("UI/ventanaEspecialidad.ui",self)
        #self.btnRegistrar().clicked.connect(self.registrar)
        #self.btnEliminar().clicked.connect(self.eliminar)
        #self.btnModificar().clicked.connect(self.modificar)
        #self.btnActualizar().clicked.connect(self.actualizar)
        self.listarDatos()
        self.show()

    # def obtenerIdEspecialidad(self):
    #     return self.txtId.text()
    #
    # def obtenerEspecialidad(self):
    #     return self.txtEspecialidad.text()

    def listarDatos(self):
        self.tblEspecialidad.setRowCount(aEspe.tamañoMantenimientoEspecialidad())
        self.tblEspecialidad.setColumnCount(2)
        self.tblEspecialidad.verticalHeader().setVisible(False)

        for i in range(0, aEspe.tamañoMantenimientoEspecialidad()):
            self.tblEspecialidad.setItem(i,0,QtWidgets.QTableWidgetItem(aEspe.devolverEspecialidad(i).getIdEspecialidad()))
            self.tblEspecialidad.setItem(i,1,QtWidgets.QTableWidgetItem(aEspe.devolverEspecialidad(i).getEspecialidad()))

    #
    # def grabar(self):
    #     try:
    #         pos = aEspe.buscarEspecialidad(self.obtenerIdEspecialidad())
    #         objEspe = aEspe.devolverEspecialidad(pos)
    #         objEspe.setEspecialidad(self.obtenerEspecialidad())
    #         aEspe.grabar()
    #         self.listarDatos()
    #     except:
    #         QtWidgets.QMessageBox.information(self,"Registrar Especialidad", "Ha ocurrido un error al registrar la especialidad", QtWidgets.QMessageBox.Ok)
    #
    # def registrar(self):
    #     objEspe = controllerEspecialidad(self.obtenerIdEspecialidad(), self.obtenerEspecialidad())
    #     aEspe.adicionarEspecialidad(objEspe)
    #     aEspe.grabar()
    #     self.ListarDatos()
    #     QtWidgets.QMessageBox.information(self,"Registrar Especialidad",
    #     "Especialidad Registrada con Exito", QtWidgets.QMessageBox.Ok)
    #
    # def eliminar(self):
    #     if aEspe.tamañoMantenimientoEspecialidad() == 0:
    #          QtWidgets.QMessageBox.information(self,"Eliminar Especialidad",
    #         "No existe Especialidad seleccionada para eliminar", QtWidgets.QMessageBox.Ok)
    #     else:
    #         fila = self.tblEspecialidad.selectedItems()
    #         if fila:
    #             indiceFila = fila[0].row()
    #             idEspecialidad = self.tblEspecialidad.item(indiceFila, 0).text()
    #             pos = aEspe.buscarEspecialidad(idEspecialidad)
    #             aEspe.eliminarEspecialidad(pos)
    #             aEspe.grabar()
    #             self.listarDatos
    #         else:
    #             QtWidgets.QMessageBox.information(self,"Eliminar Especialidad",
    #             "Hubo un error al tratar de eliminar la especialidad", QtWidgets.QMessageBox.Ok)
    #
    # def modificar(self):
    #     if aEspe.tamañoMantenimientoEspecialidad() == 0:
    #         QtWidgets.QMessageBox.information(self, "Modificar Especialidad...",
    #         "No se encontraron registros para el ID Ingresado a buscar", QtWidgets.QMessageBox.Ok)
    #     else:
    #         idEspe, _ = QtWidgets.QInputDialog.getText(self,"Buscar Especialidad", "Ingrese el ID a Modificar")
    #         pos = aEspe.buscarEspecialidad(idEspe)
    #
    #         if pos != -1:
    #             objEspe = aEspe.devolverEspecialidad(pos)
    #             self.txtId.setText(objEspe.getIdEspecialidad())
    #             self.txtEspecialidad.setText(objEspe.setEspecialidad())
