from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from View.ventanaEspecialidad import ventanaEspecialidad
from View.ventanaMedico import ventanaMedico
from View.ventanaArea import ventanaArea

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("UI/ventanaPrincipal.ui", self)
        self.show()

    # Procesos
        self.actionMedicos.triggered.connect(self.abrirVentanaMedicos)
        self.actionEspecialidades.triggered.connect(self.abrirVentanaEspecialidades)
        self.actionAreas.triggered.connect(self.abrirVentanaAreas)

    def abrirVentanaMedicos(self):
        vMedico = ventanaMedico(self)
        vMedico.show()

    def abrirVentanaEspecialidades(self):
        vEspecialidades = ventanaEspecialidad(self)
        vEspecialidades.show()

    def abrirVentanaAreas(self):
        vAreas = ventanaArea(self)
        vAreas.show()

    def cerrar(self):
        self.close()