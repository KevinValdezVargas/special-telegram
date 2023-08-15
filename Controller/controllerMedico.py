class controllerMedico:
    __codigo = ""
    __nombres = ""
    __apellidos = ""
    __cmp = ""
    __idEspecialidad = ""

    def __init__(self, codigo, nombres, apellidos, cmp, idEspecialidad):
        
        self.__codigo = codigo
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__cmp = cmp
        self.__idEspecialidad = idEspecialidad

    #METODOS GET
    def getCodigo(self):
        return self.__codigo
    
    def getNombres(self):
        return self.__nombres
    
    def getApellidos(self):
        return self.__apellidos
    
    def getCmp(self):
        return self.__cmp
    
    def getIdEspecialidad(self):
        return self.__idEspecialidad
    
    #METODOS SET
    def setCodigo(self,codigo):
        self.__codigo = codigo

    def setNombres(self,nombres):
        self.__nombres = nombres

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def setCmp(self, cmp):
        self.__cmp = cmp

    def setIdEspecialidad(self, idEspecialidad):
        self.__idEspecialidad = idEspecialidad