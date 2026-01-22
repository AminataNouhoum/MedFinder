from Medicament import Medicament
class Pharmacien:
    def __init__(self, nom_pharmacie,mot_de_passe, ID,telephone:int,adresse:str):
        self.__nom_pharmacie = nom_pharmacie
        self.__mot_de_passe = mot_de_passe
        self.__ID = ID
        self.__telephone = telephone
        self.__adresse = adresse
        self.__medicaments=[]
    @property
    def nom_pharmacie(self):
        return self.__nom_pharmacie
    @property
    def mot_de_passe(self):
        return self.__mot_de_passe
    @property
    def ID(self):
        return self.__ID
    @property
    def telephone(self):
        return self.__telephone
    @property
    def adresse(self):
        return self.__adresse
    @property
    def medicaments(self):
        return self.__medicaments
    @nom_pharmacie.setter
    def nom_pharmacie(self, nom_pharmacie):
        self.__nom_pharmacie = nom_pharmacie
    @mot_de_passe.setter
    def mot_de_passe(self, mot_de_passe):
        self.__mot_de_passe = mot_de_passe
    @ID.setter
    def ID(self, ID):
        self.__ID = ID
    @telephone.setter
    def telephone(self, telephone):
        self.__telephone = telephone
    @adresse.setter
    def adresse(self, adresse):
        self.__adresse = adresse
    def ajouter_medicament(self,nom_medicament:str,prix_medicament:float,quantite_medicament:int):
        med=Medicament(nom_medicament,prix_medicament,quantite_medicament)
        self.__medicaments.append(med)
    def modifier_quantite_medicament(self,medicament:Medicament,nouvelle_quantite:int):
        if medicament in self.medicaments:
            medicament.quantite = nouvelle_quantite
    def modifier_prix_medicament(self,medicament:Medicament,nouveau_prix:float):
        if medicament in self.medicaments:
            medicament.prix = nouveau_prix
    def modifier_adresse(self,adresse:str):
        self.__adresse = adresse



