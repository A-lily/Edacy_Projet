#from pprint import pprint

class Personne: 
    def __init__(self, nom, prenom, adresse, moyenne, age,specialite, region, sexe): #constructeur
        self.nom = nom #self cest comme this dans java
        self.prenom = prenom
        self.adresse = adresse
        self.moyenne = int(moyenne)
        self.age = int(age)
        self.region = region
        self.specialite = specialite
        self.sexe = sexe
      #  pprint(vars(self))
    def obtenirInfoPersonne(self): #ca retourne une liste avec tous ces elements, pas vraiment une liste qqch quon appelle tuple dans python
        return (self.nom,self.prenom,self.adresse,str(self.moyenne),str(self.age),self.region,self.specialite,self.sexe);
def lirePersonne (chaine): # ca prends une ligne dans le csv et ca cree objet personne
    elements = chaine.split(",") # on separe les valeurs de la ligne en une liste 
    # par exemple si t`as Awa,Ly,Oe,dkasda,sasa 
    # tu auras une liste avec les variables Awa ensuite Ly puis Oe etc...
    # ensuite j`appelle cree la personen avec le constructeur que jai cree plus tot elment[0] -> nom, element [1] -> prenom etc,,,
    return Personne (elements[0],elements[1],elements[2],elements[3],elements[4],elements[5],elements[6],elements[7])

def ecrirePersonne(personne):
    # ca fait linverse de ce que la fonction pecedente faisait
    return ",".join(personne.obtenirInfoPersonne())

def obtenirStatEcole(personnes):
    total = 0
    garcons = 0
    moyenne_regions = {}
    region_compte_personnes = {}; # Li cest qqch qu`on appelle dictionnaire dans python, ca associe une variable (quon appelle cle) a une autre (quon appelle valeur), xolal ci net bi lol
    #ici on associe le nom des regions a une moyenne
    for personne in personnes: # meme chose que for (int i =0; i <personnes.length();i++) manam pour chaque personne
        if (personne.region in region_compte_personnes.keys()):# personne cest comme personnes[i]
            region_compte_personnes[personne.region] += 1
            moyenne_regions[personne.region] += personne.moyenne# si on avait deja rencontre la region avant on 
        else :
            moyenne_regions[personne.region] = 0
            region_compte_personnes[personne.region] = 0
        total = total + personne.moyenne;
        if (personne.sexe[0] == 'M'):
           # print(personne.sexe, " = M");
            garcons  = garcons + 1;
    moyenne = total / len(personnes);
    pourcGarcons = garcons * 100 /len(personnes) 
    pourcFille = 100 - pourcGarcons
    maxMoyReg = ""
    maxMoyVal = 0
    for moy_reg in region_compte_personnes.keys(): 
        if ( moyenne_regions[moy_reg] / region_compte_personnes[moy_reg] > maxMoyVal):
            maxMoyVal =  moyenne_regions[moy_reg] / region_compte_personnes[moy_reg]
            maxMoyReg = moy_reg
    #print(moyenne, str(pourcFille), str(pourcGarcons),maxMoyReg)
    return (str(moyenne), str(pourcFille), str(pourcGarcons),maxMoyReg)


listePersonne = [];
nomFichier = "donnees.csv"
with open(nomFichier, 'r') as f: # ouverture du fichier
  for line in f: # f cest le fichier donc pour chaque ligne du fichier
     listePersonne.append(lirePersonne(line))

with open('moyenne.csv', 'w') as mf:
    for personne in listePersonne:
        if personne.moyenne > 10 : #on ecrit seulement si la moyenne est sup a 10
            mf.write(ecrirePersonne(personne))

with open('age.csv', 'w') as mf:
    for personne in listePersonne:
        if personne.age > 20 : # meme logique quavant
            mf.write(ecrirePersonne(personne))
            
with open('ecole.csv', 'w') as mf:    
    mf.write(",".join(obtenirStatEcole(listePersonne)))
