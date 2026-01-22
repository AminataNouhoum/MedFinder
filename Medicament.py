class Medicament:
    def __init__(self,nom:str,prix:float,quantite:int):
        self.__nom = nom
        self.__prix = prix
        self.__quantite = quantite
    @property
    def nom(self):
        return self.__nom
    @property
    def prix(self):
        return self.__prix
    @property
    def quantite(self):
        return self.__quantite
    @nom.setter
    def nom(self,nom):
        self.__nom = nom
    @prix.setter
    def prix(self,prix):
        self.__prix = prix
    @quantite.setter
    def quantite(self,quantite):
        self.__quantite = quantite