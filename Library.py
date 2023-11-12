class Livre:
    num_isbn_counter = 0
    dif __init__(self, titre, auteur):
    self.titre = titre
    self.auteur = auteur
    Livre.num_isbn_counter += 1
    self.num_isbn = Livre.num_isbn_counter

class Library:
    def __init__(self):
        self.Livre = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            print(f"Numéro ISBN : {livre.num_isbn}, Le titre : {livre.titre}, L'auteur : {livre.auteur}")

    def rechercher_livre(self, titre):
        resultats = []
        for livre in self.livres

        ## https://youtu.be/zes5tLXXnEQ?t=1414