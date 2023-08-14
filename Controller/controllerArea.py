class controllerArea:
    __idArea = ""
    __n_Oficinas = ""
    __n_Camas = ""
    __mt2 = ""

    def  __init__(self, idArea, n_Oficinas, n_Camas, mt2):

        self.__idArea = idArea
        self.__n_Oficinas = n_Oficinas
        self.__n_Camas = n_Camas
        self.__mt2 = mt2

    #METDOS GET
    def getIdArea(self):
        return self.__idArea
    
    def getN_Oficinas(self):
        return self.__n_Oficinas

    def getN_Camas(self):
        return self.__n_Camas
    
    def getMt2(self):
        return self.__mt2
    
    #METODOS SET

    def setIdArea(self,idArea):
        self.__idArea = idArea

    def setN_Oficinas(self,n_Oficinas):
        self.__n_Oficinas = n_Oficinas
    
    def setN_camas(self,n_Camas):
        self.__n_Camas = n_Camas

    def setMt2(self,mt2):
        self.__mt2 = mt2
