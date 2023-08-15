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
        self.btnRegistrar.clicked.connect(self.registrar)
        # self.btnEliminar.clicked.connect(self.eliminar)
        # self.btnModificar.clicked.connect(self.modificar)
        # self.btnActualizar.clicked.connect(self.grabar)
        self.listarDatos()
        self.show()

    def obtenerCodigo(self):
        return self.txtCodigo.text()

    def obtenerNombres(self):
        return self.txtNombres.text()

    def obtenerApellidos(self):
        return self.txtApellidos.text()

    def obtenerCmp(self):
        return self.txtCmp.text()

    def obtenerIdEspecialidad(self):
        return self.txtId.text()

    def listarDatos(self):
        self.tblMedicos.setRowCount(aMed.tamañoMantenimientoMedico())
        self.tblMedicos.setColumnCount(5)
        self.tblMedicos.verticalHeader().setVisible(False)

        for i in range(0, aMed.tamañoMantenimientoMedico()):
            self.tblMedicos.setItem(i, 0, QtWidgets.QTableWidgetItem(aMed.devolverMedico(i).getCodigo()))
            self.tblMedicos.setItem(i, 1, QtWidgets.QTableWidgetItem(aMed.devolverMedico(i).getNombres()))
            self.tblMedicos.setItem(i, 2, QtWidgets.QTableWidgetItem(aMed.devolverMedico(i).getApellidos()))
            self.tblMedicos.setItem(i, 3, QtWidgets.QTableWidgetItem(aMed.devolverMedico(i).getCmp()))
            self.tblMedicos.setItem(i, 4, QtWidgets.QTableWidgetItem(aMed.devolverMedico(i).getIdEspecialidad()))

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
                                  self.obtenerApellidos(),self.obtenerCmp(),self.obtenerIdEspecialidad())
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
                aMed.eliminarMedico(pos)
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
                self.txtCodigo.setText(objMed.getCodigo())
                self.txtNombres.setText(objMed.getNombres())
                self.txtApellidos.setText(objMed.getApellidos())
                self.txtCmp.setText(objMed.getCmp())
                self.txtId.setText(objMed.getIdEspecialidad())