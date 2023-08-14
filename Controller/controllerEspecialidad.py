class controllerEspecialidad:
    __idEspecialidad = ""
    __especialidad = ""
    
    def __init__(self, idEspecialidad, especialidad):
        self.__idEspecialidad = idEspecialidad
        self.__especialidad = especialidad

    #METODO GET
    def getIdEspecialidad(self):
        return self.__idEspecialidad
    
    def getEspecialidad(self):
        return self.__especialidad

    #METODO SET

    def setIdEspecialida(self, idEspecialidad):
        self.__idEspecialidad = idEspecialidad
    
    def setEspecialidad(self, especialidad):
        self.__especialidad = especialidad