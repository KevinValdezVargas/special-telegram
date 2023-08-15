class controllerArea:
    __idArea = ""
    __numeroOficinas = ""
    __numeroCamas = ""
    __mt2 = ""

    def  __init__(self, idArea, numeroOficinas, numeroCamas, mt2):

        self.__idArea = idArea
        self.__numeroOficinas = numeroOficinas
        self.__numeroCamas = numeroCamas
        self.__mt2 = mt2

    #METDOS GET
    def getIdArea(self):
        return self.__idArea
    
    def getNumeroOficinas(self):
        return self.__numeroOficinas

    def getNumeroCamas(self):
        return self.__numeroCamas
    
    def getMt2(self):
        return self.__mt2
    
    #METODOS SET

    def setIdArea(self,idArea):
        self.__idArea = idArea

    def setnumeroOficinas(self,numeroOficinas):
        self.__numeroOficinas = numeroOficinas
    
    def setnumeroCamas(self,numeroCamas):
        self.__numeroCamas = numeroCamas

    def setMt2(self,mt2):
        self.__mt2 = mt2
