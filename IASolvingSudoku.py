# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:08:46 2020
variable = case vide (n)
domains = {1, ..., 9} d=9
constraints= y'en a 3
world= une grille remplie : d^n world possible

@author: Stéphan Adjarian
"""

import random
import numpy as np

def TableauIndice(nombreCarrés):
    #Cette fonction renvoie une matrice, chaque ligne contient les indices d'un carré, 
    #chaque ligne correspond à un carré
    tab = np.zeros( (nombreCarrés, 3) )
    val=0
    for i in range(nombreCarrés):
        for j in range(3):
            tab[i][j]=val
            val+=1
    return tab

def TESTCarré(tab, coordx, coordy, valeur):
    #Cette fonction check dans quel carré la valeur se trouve puis renvoie 
    #un booléen pour dire si la valeur s'y trouve déjà ou non
    temp=TableauIndice(len(tab)//3)
    COORDXCARRE=0
    COORDYCARRE=0
    reponse=False
    """
    On check ici dans quel ligne de la matrice on se trouve
    Puisque chaque ligne correspond aux indices du carré possible
    en checkant l'indice de la ligne puis l'indice de la colonne
    on sait alors dans quel carré on se trouve.
    """
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if temp[i][j]==coordx:
                COORDXCARRE=i
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if temp[i][j]==coordy:
                COORDYCARRE=i
    #Maintenant qu'on sait dans quel carré on se trouve on check s'il n'y a pas déjà la valeur
    for i in range(COORDXCARRE*3, COORDXCARRE*3+3):
        for j in range(COORDYCARRE*3, COORDYCARRE*3+3):
            if tab[i][j]==valeur:
                reponse=True
    return reponse


def Affichage(tab):
    for i in range(len(tab)):
        print(tab[i])
    print()

def Remplissage(tab, difficulté):
    for i in range(difficulté):
        affect=False
		#Tant qu'on a pas affecté la valeur on retire aléatoirement une position et une valeur
        while affect==False:
            coordx=int(random.randrange(0,len(tab)))
            coordy=int(random.randrange(0,len(tab)))
            valeur=int(random.randrange(1,10))
			#si c'est vide on la rempli
            if tab[coordx][coordy]==0:
                if Contrainte(tab, coordx,coordy,valeur)==True:
                    tab[coordx][coordy]=valeur                  
                    affect=True   
    return tab

def IsLigne(tab,coordx,valeur):
    #valeur est-elle sur la ligne ?
    #renvoie true si la valeur est déjà présente -->pas bon
    #false sinon --> bon
    reponse=False; 
    for i in range(len(tab)):
        if tab[coordx][i]==valeur:
            reponse=True
    return reponse

def IsColonne(tab, coordy, valeur):
    #valeur est-elle sur la colonne ?
    #renvoie true si la valeur est déjà présente -->pas bon
    #false sinon --> bon  
    reponse=False; 
    for j in range(len(tab)):
        if tab[j][coordy]==valeur:
            reponse=True
    return reponse

def IsLigneColonne(tab, coordx, coordy, valeur):
    #si le ligne est présente sur la ligne et colonne 
    reponse=False
    if IsLigne(tab,coordx, valeur) or IsColonne(tab, coordy, valeur):
    #si les 2 son true alors true --> pas bon
        reponse=True
    return reponse

def Contrainte(tab, coordx, coordy,valeur):
    grosboulard=True
    for i in range(len(tab)):
		#Test de toutes les contraintes du sudoku via les fonctions appropriées
        if IsLigneColonne(tab, coordx, coordy, valeur) or TESTCarré(tab, coordx, coordy, valeur): 
            grosboulard=False          
    return grosboulard

def Resolution(tab, coordx=0, coordy=0):
    coordx, coordy = Variable(tab, coordx, coordy)
	#sortie de la récursion si on a pas trouvé de prochaine case à remplir
    if coordx == -1:
        return True
	#On test les valeurs de 1 à 9 
    for valeur in range(1,10):
		#Dès qu'une valeur satisfait les contraintes on relance l'algo dans ce noeud
        if Contrainte(tab, coordx, coordy, valeur):
            tab[coordx][coordy]=valeur
            if Resolution(tab, coordx, coordy):
                return True
			#On reset à 0 pour le back tracking
            tab[coordx][coordy]=0
    return False        

def Variable(tab, coordx, coordy):
		#Trouve la prochaine case à remplir
		#Optimisation
        for i in range(coordx,9):
            for j in range(coordy,9):
                if tab[i][j] == 0:
                    return i,j
		#Si trouve pas on cherche partout
        for i in range(0,9):
            for j in range(0,9):
                if tab[i][j] == 0:
                    return i,j
		#valeur par convention on a rien trouvé
        return -1,-1

def NouvelleMatrice(tab, difficulty):
    x=int(random.randrange(0,9)) 
    y=int(random.randrange(0,9))
    for i in range(81-difficulty):  #on laisse que n cases avec des chiffres
        while(tab[x][y]==0):
              x=int(random.randrange(0,9)) 
              y=int(random.randrange(0,9)) 
        tab[x][y]=0       
    return tab


a=9*[9*[0]]


#tab=[[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
tab=np.zeros( (9, 9) )
Remplissage(tab, 10)
print("Veuillez patienter...")
b=Resolution(tab)
print(b)
a=NouvelleMatrice(tab, 50) #indiquez ici le nombre de case déjà données
Affichage(a)
input("Grille créée. Vous pouvez essayer de la finir ou appuyer sur enter pour que l'IA la finisse à votre place ==>")
Resolution(a)
print("Une solution est :")
Affichage(a)

'''#csp constraint satisfaction problem'''