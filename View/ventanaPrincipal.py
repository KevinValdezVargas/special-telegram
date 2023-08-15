# from PyQt5 import QtWidgets, uic
# from PyQt5 import QtGui
# from View.ventanaEspecialidad import ventanaDocente
# from View.ventanaMedico import ventanaEspecialidad
# from View.ventanaArea import ventanaEstudiante
#
# class VentanaPrincipal(QtWidgets.QMainWindow):
#     def __init__(self, parent = None):
#         super(VentanaPrincipal, self).__init__(parent)
#         uic.loadUi("UI/ventanaPrincipal.ui", self)
#         self.show()
#
#     # Procesos
#         self.actionDocente.triggered.connect(self.abrirVentanaDocente)
#         self.actionEspecialidad.triggered.connect(self.abrirVentanaEspecialidad)
#         self.actionEstudiante.triggered.connect(self.abrirVentanaEstudiante)
#
#     def cerrar(self):
#         self.close()