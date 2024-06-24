# Auteur: Pablo Hidalgo Etienne        , matricule  20266668
#          Gabriel Barroso Magno Viana , matricule: 20283304 
#
# Date:   12/12/2023
#
# Ce programme cree un jeu web pour jouer au jeu “addiction solitaire”.
# un jeu joue en solitaire (un seul joueur) 
# avec des cartes a jouer standard (52 cartes).

import math

# Déclaration des tables de jeu et des variables de contrôle
      

# Table pour suivre l'état du jeu Master Mind
table_master_mind = []


# Table pour stocker les indices des cartes mises en surbrillance
# (lignes vertes)
table_lime = []


# Table pour stocker les indices des cartes absentes (marquées "A")
table_absent = []


# Table pour stocker les cartes actuelles du jeu
table_cartes = []


# Variable pour suivre le nombre de brassages disponibles
brassages_disponibles = 3

# Couleurs possibles des cartes (Clubs, Diamond, Heart, Spade)
couleurs_possibles = ['C','D','H','S']


# Valeurs possibles des cartes (As, 2, 3, ..., Roi)
valeurs_possibles = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']


# Table de contrôle, peut-être utilisée pour suivre l'état des cartes
table_de_controle = []




def test_tab_ordonee():
    # Définissez les couleurs et les valeurs possibles
    couleurs_possibles = ['C', 'D', 'H', 'S']
    valeurs_possibles = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                         'J', 'Q', 'K']

    # Appelez la fonction tab_ordonee avec les couleurs et les valeurs
    resultat = tab_ordonee(couleurs_possibles, valeurs_possibles)

    # Vérifiez la longueur de la liste résultante
    assert len(resultat) == len(couleurs_possibles) * len(valeurs_possibles)

    # Vérifiez que chaque carte possible est présente dans la liste résultante
    for valeur in valeurs_possibles:
        for couleur in couleurs_possibles:
            carte = valeur + couleur
            assert carte in resultat

    # Vérifiez que la liste résultante est ordonnée comme prévu
    for i in range(len(resultat) - 1):
        assert resultat[i] < resultat[i + 1]


def test_eliminer_A():
    # Créez une table avec des cartes ordonnées
    couleurs_possibles = ['C', 'D', 'H', 'S']
    valeurs_possibles = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                         'J', 'Q', 'K']
    table = tab_ordonee(couleurs_possibles, valeurs_possibles)

    # Appelez la fonction eliminer_A avec la table
    resultat = eliminer_A(table.copy())

    # Vérifiez que les premières cartes de chaque groupe de 13 cartes
    # sont marquées comme "absent"
    for i in range(0, 52, 13):
        assert resultat[i] == "absent"

    # Vérifiez que les autres cartes n'ont pas été modifiées
    for i in range(1, 52):
        if i % 13 != 0:
            assert resultat[i] == table[i]


def test_echanger_valeurs():
    # Créez une table avec des valeurs spécifiques
    table = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # Appelez la fonction echanger_valeurs avec la table
    resultat = echanger_valeurs(table.copy(), 1, 10)

    # Vérifiez que les valeurs des indices spécifiés ont été correctement
    # échangées
    assert resultat[1] == 'Q'
    assert resultat[10] == '2'

    # Vérifiez que les autres valeurs n'ont pas été modifiées
    for i in range(len(table)):
        if i != 1 and i != 10:
            assert resultat[i] == table[i]


def test_victoire():
    # Cas où le joueur gagne
    victoire_1 = victoire([
        'A', '2', '3', '4',
        '5', '6', '7', '8',
        '9', '10', 'J', 'Q',
        'K', 'A', '2', '3',
        '4', '5', '6', '7',
        '8', '9', '10', 'J',
        'Q', 'K', 'A', '2',
        '3', '4', '5', '6',
        '7', '8', '9', '10',
        'J', 'Q', 'K', 'A',
        '2', '3', '4', '5',
        '6', '7', '8', '9',
        '10', 'J', 'Q', 'K'
    ])

    # Cas où le joueur ne gagne pas
    victoire_2 = victoire([
        'A', '2', '3', '4',
        '5', '6', '7', '8',
        '9', '10', 'J', 'Q',
        'K', 'A', '2', '3',
        '4', '5', '6', '7',
        '8', '9', '10', 'J',
        'Q', 'K', 'A', '2',
        '3', '4', '5', '6',
        '7', '8', '9', '10',
        'J', 'Q', 'K', 'A',
        '2', '3', '4', '5',
        '6', '7', '8', '9',
        '10', 'J', 'Q', 'K',
        'A', '2', '3', '4',
        '5', '6', '7', '8',
        '9', '10', 'J', 'Q',
        'K', 'A', '2', '3',
        '4', '5', '6', '7',
        '8', '9', '10', 'J',
        'Q', 'K', 'A', '2',
        '3', '4', '5', '6',
        '7', '8', '9', '10',
        'J', 'Q', 'K'
    ])

    # Vérifiez les résultats
    assert victoire_1 is True
    assert victoire_2 is False


# Fonction pour tester bouton_brasser_les_cartes
def test_bouton_brasser_les_cartes():
    # Initialisation des variables globales
    global table_cartes
    global table_master_mind
    global brassages_disponibles

    
    # Affectation de valeurs initiales
    
    # Exemple de valeurs initiales pour la table de cartes
    table_cartes = ["C1", "D2", "H3", "S4"]  
    # Exemple de valeurs initiales pour le jeu Master Mind
    table_master_mind = ["R", "G", "B", "Y"]  
    brassages_disponibles = 3

    # Appel de la fonction bouton_brasser_les_cartes
    bouton_brasser_les_cartes()

    # Vérification si les variables globales sont mises à jour correctement
    # Vous devrez adapter ces assertions en fonction de votre implémentation 
    # réelle
    
    # Vérifie si la table de cartes a la bonne taille après le brassage
    assert len(table_cartes) == 4  
    # Vérifie si le jeu Master Mind a la bonne taille après le brassage
    assert len(table_master_mind) == 4
    # Vérifie si le nombre de brassages disponibles est décrémenté correctement
    assert brassages_disponibles == 2  


# Fonction pour tester diviser_par_ligne
def test_diviser_par_ligne():
    # Créez une table avec des valeurs spécifiques
    table = [
        'A', '2', '3', '4',
        '5', '6', '7', '8',
        '9', '10', 'J', 'Q',
        'K', 'A', '2', '3',
        '4', '5', '6', '7',
        '8', '9', '10', 'J',
        'Q', 'K', 'A', '2',
        '3', '4', '5', '6',
        '7', '8', '9', '10',
        'J', 'Q', 'K', 'A',
        '2', '3', '4', '5',
        '6', '7', '8', '9',
        '10', 'J', 'Q', 'K'
    ]

    # Appelez la fonction diviser_par_ligne avec la table
    resultat = diviser_par_ligne(table)

    # Vérifiez la longueur de la liste résultante
    assert len(resultat) == 4

    # Vérifiez que chaque ligne a la longueur attendue
    for ligne in resultat:
        assert len(ligne) == 13

    # Vérifiez que les éléments de chaque ligne proviennent
    # de la table d'entrée
    for i in range(4):
        for j in range(13):
            assert resultat[i][j] == table[j * 4 + i]


# Fonction pour tester chercher_index
def test_chercher_index():
    # Cas où la séquence n'est jamais brisée
    resultat_1 = chercher_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    # Cas où la séquence est brisée à l'index 5
    resultat_2 = chercher_index([1, 2, 3, 4, 17, 18, 19, 20, 21, 22, 23, 24])

    # Cas où la séquence est brisée à l'index 2
    resultat_3 = chercher_index([1, 2, 18, 19, 5, 6, 7, 8, 9, 10, 11, 12])

    # Cas où la séquence est brisée dès le début
    resultat_4 = chercher_index([17, 18, 19, 20, 21, 22, 23, 24, 9, 10,
                                 11, 12])

    # Vérifiez les résultats
    assert resultat_1 == 12
    assert resultat_2 == 5
    assert resultat_3 == 2
    assert resultat_4 == 1


# Fonction pour tester x_dans_la_table
def test_x_dans_la_table():
    # Cas où "x" est présent dans la table
    resultat_1 = x_dans_la_table(["A", "2", "3", "x", "5", "6", "7", "8"])

    # Cas où "x" n'est pas présent dans la table
    resultat_2 = x_dans_la_table(["A", "2", "3", "4", "5", "6", "7", "8"])

    # Cas où la table est vide
    resultat_3 = x_dans_la_table([])

    # Vérifiez les résultats
    assert resultat_1 is True
    assert resultat_2 is False
    assert resultat_3 is False


# Fonction pour tester rearanger
def test_rearanger():
    # Créez une table avec des valeurs spécifiques
    table = [
        ['A1', 'B1', 'C1'],
        ['A2', 'B2', 'C2'],
        ['A3', 'B3', 'C3'],
        ['A4', 'B4', 'C4']
    ]

    # Appelez la fonction rearanger avec la table
    resultat = rearanger(table)

    # Vérifiez la table réarrangée
    assert resultat == ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4',
                        'C1', 'C2', 'C3', 'C4']

    


def test_melanger():
    # Créez deux tables avec des valeurs spécifiques
    table_mm = ['R', 'G', 'B', 'Y']
    table_cartes = ['C1', 'D2', 'H3', 'S4']

    # Copiez les tables pour conserver les valeurs d'origine
    table_mm_copie = table_mm.copy()
    table_cartes_copie = table_cartes.copy()

    # Appelez la fonction melanger avec les deux tables
    resultat = melanger(table_mm, table_cartes)

    # Vérifiez que les tables d'origine ne sont pas égales 
    # aux tables résultantes
    assert table_mm != resultat[0]
    assert table_cartes != resultat[1]

    # Vérifiez que les tables résultantes ont la même longueur
    # que les tables d'origine
    assert len(table_mm) == len(resultat[0])
    assert len(table_cartes) == len(resultat[1])

    # Vérifiez que les éléments d'origine sont toujours présents dans
    # les tables résultantes
    for elem in table_mm_copie:
        assert elem in resultat[0]

    for elem in table_cartes_copie:
        assert elem in resultat[1]

    # Vérifiez que les éléments sont mélangés sans utiliser any
    mm_melange = False
    for i in range(len(resultat[0])-1):
        if resultat[0][i] != resultat[0][i+1]:
            mm_melange = True
            break

    cartes_melange = False
    for i in range(len(resultat[1])-1):
        if resultat[1][i] != resultat[1][i+1]:
            cartes_melange = True
            break

    assert mm_melange
    assert cartes_melange


def test_embaraseur_carte_NEW():
    # Créez deux tables avec des valeurs spécifiques 
    # (vous devez les adapter à vos besoins)
    global table_master_mind
    global table_cartes
    table_master_mind = ['A', '2', '3', '4', '5', '6', '7', '8']
    table_cartes = ['C1', 'D2', 'H3', 'S4', 'C5', 'D6', 'H7', 'S8']

    # Copiez les tables pour conserver les valeurs d'origine
    table_mm_copie = table_master_mind.copy()
    table_cartes_copie = table_cartes.copy()

    # Appelez la fonction embaraseur_carte_NEW avec les deux tables
    resultat = embaraseur_carte_NEW()

    # Vérifiez que les tables d'origine ne sont pas égales
    # aux tables résultantes
    assert table_master_mind != resultat[1]
    assert table_cartes != resultat[0]

    # Vérifiez que les tables résultantes ont la même longueur
    # que les tables d'origine
    assert len(table_master_mind) == len(resultat[1])
    assert len(table_cartes) == len(resultat[0])

    # Vérifiez que les éléments d'origine sont toujours présents dans
    # les tables résultantes
    for elem in table_mm_copie:
        assert elem in resultat[1]

    for elem in table_cartes_copie:
        assert elem in resultat[0]

    # Vérifiez que les éléments sont mélangés sans utiliser any
    mm_melange = False
    for i in range(len(resultat[1])-1):
        if resultat[1][i] != resultat[1][i+1]:
            mm_melange = True
            break

    cartes_melange = False
    for i in range(len(resultat[0])-1):
        if resultat[0][i] != resultat[0][i+1]:
            cartes_melange = True
            break

    assert mm_melange
    assert cartes_melange


def test_carte_verte():
    # Créez deux tables avec des valeurs spécifiques
    # (vous devez les adapter à vos besoins)
    global table_master_mind
    global table_cartes
    table_master_mind = ['A', '2', '3', '4', '5', '6', '7', '8']
    table_cartes = ['C1', 'D2', 'H3', 'S4', 'C5', 'D6', 'H7', 'S8']

    # Appelez la fonction carte_verte avec les deux tables
    cartes_lime, cartes_absent = carte_verte(table_master_mind, table_cartes)

    # Vérifiez que les cartes absentes et les cartes vertes sont correctement
    # identifiées
    assert set(cartes_lime) == {4, 5, 6, 7}
    assert set(cartes_absent) == {0, 1, 2, 3}

  


def test_nouvelles_cartes_lime():
    # Créez des variables globales nécessaires
    # (vous devez les adapter à vos besoins)
    global table_master_mind
    global table_cartes
    global brassages_disponibles
    global table_lime
    global table_absent

    # Simulez différentes situations pour tester la fonction
    brassages_disponibles = 3  # Définissez le nombre de brassages disponibles

    # Cas où aucune carte verte n'est présente
    table_master_mind = ['A', '2', '3', '4', '5', '6', '7', '8']
    table_cartes = ['C1', 'D2', 'H3', 'S4', 'C5', 'D6', 'H7', 'S8']
    table_lime = []
    table_absent = []
    nouvelles_cartes_lime()
    # Le nombre de brassages disponibles doit diminuer
    assert brassages_disponibles == 2
    # Le joueur n'a pas gagné
    assert victoire(table_master_mind) is False  

    # Cas où toutes les cartes sont vertes et le joueur a gagné
    table_master_mind = ['A', '2', '3', '4', '5', '6', '7', '8']
    table_cartes = ['C1', 'D2', 'H3', 'S4', 'C5', 'D6', 'H7', 'S8']
    table_lime = [4, 5, 6, 7]
    table_absent = []
    nouvelles_cartes_lime()
    # Le nombre de brassages disponibles doit diminuer
    assert brassages_disponibles == 1  
    # Le joueur a gagné
    assert victoire(table_master_mind) is True  

    # Cas où le joueur a gagné mais n'a plus de brassages disponibles
    brassages_disponibles = 0
    table_master_mind = ['A', '2', '3', '4', '5', '6', '7', '8']
    table_cartes = ['C1', 'D2', 'H3', 'S4', 'C5', 'D6', 'H7', 'S8']
    table_lime = [4, 5, 6, 7]
    table_absent = []
    nouvelles_cartes_lime()
    # Le nombre de brassages disponibles ne doit pas changer
    assert brassages_disponibles == 0  
    # Le joueur a gagné
    assert victoire(table_master_mind) is True  


def test_reinicialiser():
    # Créez des variables globales nécessaires
    # (vous devez les adapter à vos besoins)
    global table_de_controle
    global table_cartes
    global table_master_mind
    global table_lime
    global table_absent
    global brassages_disponibles

    # Initialisez les variables globales
    brassages_disponibles = 0
    table_de_controle = [1, 2, 3, 4]
    valeurs_possibles = ['A', '2', '3', '4']
    couleurs_possibles = ['C', 'D', 'H', 'S']

    # Définissez une fonction factice pour remplacer document.querySelector
    def fake_query_selector(selector):
        return {'#conditions_du_jeu': {'innerHTML': ''}}

    # Redéfinissez la fonction embaraseur_carte_NEW pour éviter les effets
    # indésirables
    def fake_embaraseur_carte_NEW():
        return [[1, 2, 3, 4], [1, 2, 3, 4]]

    global document
    document = fake_query_selector

    global embaraseur_carte_NEW
    embaraseur_carte_NEW = fake_embaraseur_carte_NEW

    # Appelez la fonction reinicialiser
    reinicialiser()

    # Vérifiez que les variables globales sont réinitialisées correctement
    assert brassages_disponibles == 3
    assert table_master_mind == [1, 2, 3, 4]


def test_clic():
    # Créez des variables globales nécessaires
    # (vous devez les adapter à vos besoins)
    global table_lime
    global table_absent
    global table_cartes
    global table_master_mind
    global brassages_disponibles

    # Initialisez les variables globales
    brassages_disponibles = 3
    table_lime = [0, 1, 2, 3]
    table_absent = [4, 5, 6, 7]
    table_cartes = ['C1', 'D2', 'H3', 'S4', 'C5', 'D6', 'H7', 'S8']
    table_master_mind = ['A', '2', '3', '4', '5', '6', '7', '8']

    # Appelez la fonction clic avec un index spécifique
    # (vous devez adapter cet index à vos besoins)
    clic(0)

    # Vérifiez que les tables sont correctement mises à jour après le clic
    assert table_cartes == ['C5', 'D2', 'H3', 'S4', 'C1', 'D6', 'H7', 'S8']
    assert table_master_mind == ['5', '2', '3', '4', 'A', '6', '7', '8']


def testes():
    test_tab_ordonee()
    test_carte_verte()
    test_nouvelles_cartes_lime()
    test_reinicialiser()
    test_clic()
    test_embaraseur_carte_NEW()
    test_melanger()
    test_rearanger()
    test_x_dans_la_table()
    test_chercher_index()
    test_diviser_par_ligne()
    test_bouton_brasser_les_cartes()
    test_victoire()
    test_eliminer_A()
    test_tab_ordonee()
    test_echanger_valeurs()



# La boucle "for" itère sur les indices de 0 à 51 inclus.
for i in range(52):  
    # Ajoute chaque indice à la liste "table_de_controle".
    table_de_controle.append(i)

# Fonction pour retirer la mise en surbrillance verte des cartes
def retirer_vert():
    # Itération sur les indices des cartes de 0 à 51 inclus
    for i in range(52):
        # Sélectionne l'élément de la carte par son ID
        carte = document.querySelector('#carte' + str(i))
        # Supprime l'attribut de style pour retirer la mise en surbrillance
        carte.removeAttribute("style")


# Fonction pour créer une table ordonnée de cartes en fonction des couleurs
# et des valeurs possibles
def tab_ordonee(couleurs_possibles, valeurs_possibles):
    # Initialisation d'une liste vide pour stocker les cartes ordonnées
    tab = []

    # Boucle imbriquée pour créer les combinaisons de valeurs et de couleurs
    for valeur in valeurs_possibles:     
        for couleur in couleurs_possibles:
            # Ajout de chaque combinaison à la liste
            tab.append(valeur + couleur)

    # Retourne la liste résultante
    return tab


# Fonction pour marquer les premières cartes comme "absent" dans une table
def eliminer_A(tab):
    # Itération sur les indices 0, 13, 26 et 39 de la table
    for i in range(0, 4):
        # Marque la carte comme "absent"
        tab[i] = "absent"
    
    # Retourne la table modifiée
    return tab


# Fonction pour échanger les valeurs de deux indices dans une table
def echanger_valeurs(tab, index1, index2):
    # Stocke temporairement la valeur de l'index1
    temp = tab[index1]
    
    # Remplace la valeur de l'index1 par celle de l'index2
    tab[index1] = tab[index2]
    
    # Remplace la valeur de l'index2 par la valeur temporaire (stockée)
    tab[index2] = temp
    
    # Retourne la table modifiée
    return tab


# Fonction pour vérifier si le joueur a gagné
def victoire(tab):
    # Divise la table en lignes
    comparer_victoire = diviser_par_ligne(tab)
    
    # Vérifie chaque ligne
    for i in range(4):
        # Vérifie si la première carte de la ligne appartient à la première
        # rangée
        if comparer_victoire[i][0] // 4 == 1:
            # Cherche l'index où la séquence est brisée
            index = chercher_index(comparer_victoire[i])
            
            # Si l'index n'est pas la longueur de la ligne, la séquence n'est
            # pas complète
            if not index == len(comparer_victoire[i]):
                return False
    
    # Si toutes les séquences sont complètes, le joueur a gagné
    return True


def bouton_brasser_les_cartes():
    # Utilisation des variables globales pour les tables de cartes,
    # le jeu Master Mind et le nombre de brassages disponibles
    global table_cartes
    global table_master_mind
    global brassages_disponibles
    
    # Décrémente le nombre de brassages disponibles
    brassages_disponibles -= 1
    
    # Appelle la fonction pour mélanger les cartes
    tab_provisionel = embaraseur_carte_NEW() 
    table_cartes = tab_provisionel[0]
    table_master_mind = tab_provisionel[1]
    
   
    
    # Vérifie s'il ne reste plus de brassages et met à jour le texte en
    # conséquence
    if brassages_disponibles == 0:
        conditions_du_jeu = document.querySelector('#conditions_du_jeu') 
        conditions_du_jeu.innerHTML = "Vous ne pouvez plus brasser les cartes"
    else:
        conditions_du_jeu = document.querySelector('#counter') 
        conditions_du_jeu.innerHTML = " " + str(brassages_disponibles) + " "
    
    # Met à jour les nouvelles cartes surlignées en vert
    nouvelles_cartes_lime()


# Fonction pour diviser une table en lignes
def diviser_par_ligne(tab):
    # Initialisation d'une liste pour stocker les lignes
    divition_lignes = [[], [], [], []]
    
    # Boucle pour chaque ligne
    for i in range(4):
        # Boucle pour chaque élément de la ligne dans la table
        for j in range(0, 51, 4):
            # Ajoute l'élément à la ligne correspondante
            divition_lignes[i].append(tab[j + i])
    
    # Retourne la liste de lignes résultante
    return divition_lignes


# Fonction pour chercher l'index où une séquence est brisée dans une table
def chercher_index(tab):
    # Utilisation de la variable globale pour la table Master Mind
    global table_master_mind
    
    # Initialisation de l'index à 1
    index = 1
    
    # Boucle pour chaque élément dans la table, sauf le dernier
    for i in range(len(tab)-1):
        # Vérifie si la séquence est brisée en comparant les valeurs
        # adjacentes
        if tab[i] % 4 == tab[i+1] % 4 and (tab[i]//4) + 1 == tab[i+1]//4:
            index += 1
        else:
            return index  # Retourne l'index où la séquence est brisée
    
    # Si aucune séquence n'est brisée, retourne l'index actuel
    return index
 

# Fonction pour vérifier la présence de "x" dans une table
def x_dans_la_table(tab):
    # Vérifie si "x" est présent dans la table
    if "x" in tab:
        return True
    return False


# Fonction pour réarranger une table en retirant les éléments de chaque
# colonne
def rearanger(tab):
    # Initialisation d'une nouvelle table réarrangée
    table_rearangee = []
    
    # Boucle pour chaque élément dans la première colonne
    for i in range(len(tab[0])):
        # Boucle pour chaque colonne
        for j in range(len(tab)):
            # Retire l'élément de la colonne et l'ajoute à la table réarrangée
            ajouter = tab[j].pop(0)
            table_rearangee.append(ajouter)
    
    # Retourne la table réarrangée
    return table_rearangee


# Fonction pour mélanger deux tables
def melanger(table_shuffle_mm, table_shuffle_cartes):
    import math
    import random
    
    # Boucle pour chaque élément dans la table, en commençant par la fin
    for i in range(len(table_shuffle_mm) - 1, 0, -1):
        # Sélectionne une sous-table à mélanger
        a_brasser = table_shuffle_mm[0:i]
        
        # Sélectionne un index aléatoire dans la sous-table
        index = math.floor(len(a_brasser) * random.random())

        # Échange les éléments entre l'élément actuel et l'index sélectionné
        # pour la table Master Mind
        temp = table_shuffle_mm[i]
        table_shuffle_mm[i] = table_shuffle_mm[index]
        table_shuffle_mm[index] = temp 

        # Échange les éléments entre l'élément actuel et l'index sélectionné
        # pour la table de cartes
        temp = table_shuffle_cartes[i] 
        table_shuffle_cartes[i] = table_shuffle_cartes[index]
        table_shuffle_cartes[index] = temp
        
    # Retourne les deux tables mélangées
    deux_tables = [table_shuffle_mm, table_shuffle_cartes]
    return deux_tables


# Fonction pour embarquer les cartes de manière nouvelle
def embaraseur_carte_NEW():
    # Initialisation des tables
    table_shuffle_mm = []
    table_shuffle_cartes = []
    global table_master_mind
    global table_cartes

    # Division des 4 lignes pour les cartes Master Mind et les cartes
    # à mélanger
    lignes_m_m = diviser_par_ligne(table_master_mind)
    lignes_cartes = diviser_par_ligne(table_cartes)

    # Séparation des cartes fixes des cartes à mélanger
    for i in range(4):
        if lignes_m_m[i][0] // 4 != 1:
            for _ in range(len(lignes_m_m[i])):
                pop = lignes_m_m[i].pop(0)
                table_shuffle_mm.append(pop)
                lignes_m_m[i].append("x")

                pop = lignes_cartes[i].pop(0)
                table_shuffle_cartes.append(pop)
                lignes_cartes[i].append("x")

        else:
            index = chercher_index(lignes_m_m[i])
            for j in range(index, len(lignes_m_m[i])):
                table_shuffle_mm.append(lignes_m_m[i][j])
                table_shuffle_cartes.append(lignes_cartes[i][j])

            for j in range(index, len(lignes_m_m[i])):
                lignes_m_m[i][j] = "x"
                lignes_cartes[i][j] = "x"

    # Mélange des deux tables
    deux_table = melanger(table_shuffle_mm, table_shuffle_cartes)
    table_shuffle_mm = deux_table[0]
    table_shuffle_cartes = deux_table[1]

    # Remplacement des cartes dans les lignes originales
    for i in range(len(lignes_m_m)):
        while x_dans_la_table(lignes_m_m[i]) == True:
            a_ajouter = table_shuffle_mm.pop(0)
            lignes_m_m[i].remove("x")
            lignes_m_m[i].append(a_ajouter)

            a_ajouter = table_shuffle_cartes.pop(0)
            lignes_cartes[i].remove("x")
            lignes_cartes[i].append(a_ajouter)

    # Réarrangement final des tables Master Mind et cartes
    table_master_mind = rearanger(lignes_m_m)
    table_cartes = rearanger(lignes_cartes)

    # Mise à jour des images des cartes dans le document
    # (utilisez cela dans votre code réel, pas dans Python)
    for i in range(len(table_master_mind)):
        # Cherche la balise par rapport a son id
        carte = document.querySelector('#carte' + str(i))
        # Actualise l'image de la carte
        carte.innerHTML = '<img src="cards/' + table_cartes[i] + '.svg">'  

    # Retourne les deux tables mises à jour
    deux_tables = [table_cartes, table_master_mind]
    return deux_tables


# Fonction pour identifier les cartes vertes
def carte_verte(table_master_mind, table_cartes):   
    table_lime = []
    table_absent = []

    for i in range(len(table_master_mind)):
        if table_cartes[i] == "absent":
            # Si c'est absent, ajoute à la liste des absents
            table_absent.append(i)  

            if i // 4 == 0:  # Si le absent est à gauche
                for k in range(len(table_master_mind)):
                    # Carte 2, reste vert si et seulement si le index i//4
                    # est vide
                    if table_master_mind[k] // 4 == 1:  
                        table_lime.append(k)
                        # Remplacez la ligne suivante par le code 
                        # correspondant à votre environnement réel 
                        # (JavaScript dans un navigateur, par exemple)
                        case = document.querySelector("#carte" + str(k))
                        case.setAttribute("style", "background-color: lime")

            elif i // 4 != 0:  # Si le absent n'est pas à gauche
                for k in range(len(table_master_mind)):
                    if table_cartes[i - 4] == "absent" or table_master_mind[
                        i - 4] // 4 == 12:
                        table_absent.remove(i)
                        break
                    else:
                        if table_master_mind[i - 4] % 4 == table_master_mind[
                            k] % 4 and (table_master_mind[
                            i - 4] // 4) + 1 == table_master_mind[k] // 4:
                            table_lime.append(k)
                            # Remplacez la ligne suivante par le code 
                            # correspondant à votre environnement réel 
                            # (JavaScript dans un navigateur, par exemple)
                            case = document.querySelector("#carte" + str(k))
                            case.setAttribute(
                                "style", "background-color: lime")

    return table_lime, table_absent


# Fonction pour mettre à jour les nouvelles cartes vertes
def nouvelles_cartes_lime():
    retirer_vert()  # Retire le style vert des cartes
    global table_lime
    global table_master_mind
    global table_cartes
    global table_absent

    table_lime, table_absent = carte_verte(table_master_mind, table_cartes)
    
    if table_lime == []:
        if victoire(table_master_mind):
            conditions_du_jeu = document.querySelector('#conditions_du_jeu')
            conditions_du_jeu.innerHTML = "Vous avez réussi! Bravo!"
        elif brassages_disponibles == 0:
            conditions_du_jeu = document.querySelector('#conditions_du_jeu')
            conditions_du_jeu.innerHTML = """
            Vous n'avez pas réussi à placer toutes les cartes... Essayez 
            à nouveau!"""


# Fonction pour réinitialiser le jeu
def reinicialiser():
    global table_de_controle
    global table_cartes
    global table_master_mind
    global table_lime
    global table_absent
    global brassages_disponibles

    brassages_disponibles = 3
    etat_de_brassage = document.querySelector('#conditions_du_jeu')
    etat_de_brassage.innerHTML = '''
    Vous pouvez encore <button onclick="bouton_brasser_les_cartes()"> Brasser
    les cartes </button><em id="counter"> 3 </em>fois'''

    retirer_vert()  # Retire le style vert des cartes
    table_ordonee = tab_ordonee(couleurs_possibles, valeurs_possibles)
    table_cartes = eliminer_A(table_ordonee)
    table_master_mind = table_de_controle.copy()

    # Appel de la fonction qui mélange les cartes
    tab_provisionel = embaraseur_carte_NEW()  
    table_cartes = tab_provisionel[0]
    table_master_mind = tab_provisionel[1]

    nouvelles_cartes_lime()


# Fonction déclenchée lors du clic sur un bouton
def clic(i):
    global table_lime
    global table_absent
    global table_cartes
    global table_master_mind
    global brassages_disponibles

    for j in range(len(table_lime)):
        if i == table_lime[j]:
            if table_master_mind[i] // 4 == 1:
                extra = len(table_lime) - len(table_absent)
                if len(table_absent) < extra:
                    extra = j

                # Modification des images des cartes dans l'interface graphique
                carte_est_2 = document.querySelector('#carte' + str(
                    table_absent[0]))
                carte = document.querySelector('#carte' + str(table_lime[j]))
                carte_est_2.innerHTML = '<img src="cards/' + str(
                    table_cartes[table_lime[j]]) + '.svg">'
                carte.innerHTML = '<img src="cards/' + str(
                    table_cartes[table_absent[j - extra]]) + '.svg">'

                # Échanger les valeurs dans les tables
                table_cartes = echanger_valeurs(
                    table_cartes, table_absent[0], table_lime[j])
                table_master_mind = echanger_valeurs(
                    table_master_mind, table_absent[0], table_lime[j])
            else:
                if len(table_lime) > len(table_absent):
                    extra = len(table_lime) - len(table_absent)

                    # Modification des images des cartes dans l'interface 
                    # graphique
                    carte1 = document.querySelector(
                        '#carte' + str(table_absent[j - extra]))
                    carte2 = document.querySelector(
                        '#carte' + str(table_lime[j]))
                    carte1.innerHTML = '<img src="cards/' + str(
                        table_cartes[table_lime[j]]) + '.svg">'
                    carte2.innerHTML = '<img src="cards/' + str(
                        table_cartes[table_absent[j - extra]]) + '.svg">'

                    # Échanger les valeurs dans les tables
                    table_cartes = echanger_valeurs(
                        table_cartes, table_absent[j - extra], table_lime[j])
                    table_master_mind = echanger_valeurs(
                        table_master_mind, table_absent[
                            j - extra], table_lime[j])

                else:
                    # Modification des images des cartes dans l'interface
                    # graphique
                    carte1 = document.querySelector(
                        '#carte' + str(table_absent[j]))
                    carte2 = document.querySelector(
                        '#carte' + str(table_lime[j]))
                    carte1.innerHTML = '<img src="cards/' + str(
                        table_cartes[table_lime[j]]) + '.svg">'
                    carte2.innerHTML = '<img src="cards/' + str(
                        table_cartes[table_absent[j]]) + '.svg">'

                    # Échanger les valeurs dans les tables
                    table_cartes = echanger_valeurs(
                        table_cartes, table_absent[j], table_lime[j])
                    table_master_mind = echanger_valeurs(
                        table_master_mind, table_absent[j], table_lime[j])

            break

    nouvelles_cartes_lime()  # Met à jour l'affichage après le clic

    
def init():
# changer le contenu HTML de l’´el´ement racine
    racine = document.querySelector("#cb-body")
    racine.innerHTML = """
<style>

    /* Styles de la table */
    table {
    border-collapse: collapse;
    width: 75%;
    margin-top: 20px; /* Adds margin above the table */
    margin-left: 1em;
    }

    /* Styles des cellules de la table */
    td {
    border: 1px solid #ddd;
    padding: 4px;
    text-align: center;
    }

   /* Style pour les images à l'intérieur des cellules */
    td img {
    max-width: 100px;
    height: auto; 
    display: block; 
    margin: 0 auto; 
    }

    /* Styles pour les boutons */
    button {
    border: none; /* Removes border */
    padding: 5px 20px; /* Adds spacing between text and button */
    text-align: center; /* Aligns text to the center of the button */
    text-decoration: none; /* Removes text underline */
    display: inline-block; /* Aligns the button to the center of the text */
    font-size: 16px; /* Sets the button text size */
    margin: 4px 2px; /* Adds margin between text and button */
    cursor: pointer; /* Sets the button cursor */
    }

    /* Styles de la classe Options */
    #options {
    margin: 1em;
    }
</style>

<div id="cb-body">
    <table>
      <tr>
        <td id="carte0" onclick="clic(0)"><img src="cards/AC.svg"></td> 
        <td id="carte4" onclick="clic(4)"><img src="cards/2C.svg"></td>
        <td id="carte8" onclick="clic(8)"><img src="cards/3C.svg"></td>
        <td id="carte12" onclick="clic(12)"><img src="cards/4C.svg"></td>
        <td id="carte16" onclick="clic(16)"><img src="cards/5C.svg"></td>
        <td id="carte20" onclick="clic(20)"><img src="cards/6C.svg"></td>
        <td id="carte24" onclick="clic(24)"><img src="cards/7C.svg"></td>
        <td id="carte28" onclick="clic(28)"><img src="cards/8C.svg"></td>
        <td id="carte32" onclick="clic(32)"><img src="cards/9C.svg"></td>
        <td id="carte36" onclick="clic(36)"><img src="cards/10C.svg"></td>
        <td id="carte40" onclick="clic(40)"><img src="cards/JC.svg"></td>
        <td id="carte44" onclick="clic(44)"><img src="cards/QC.svg"></td>
        <td id="carte48" onclick="clic(48)"><img src="cards/KC.svg"></td>
      </tr>
      <tr>
        <td id="carte1" onclick="clic(1)"><img src="cards/AD.svg"></td> 
        <td id="carte5" onclick="clic(5)"><img src="cards/2D.svg"></td>
        <td id="carte9" onclick="clic(9)"><img src="cards/3D.svg"></td>
        <td id="carte13" onclick="clic(13)"><img src="cards/4D.svg"></td>
        <td id="carte17" onclick="clic(17)"><img src="cards/5D.svg"></td>
        <td id="carte21" onclick="clic(21)"><img src="cards/6D.svg"></td>
        <td id="carte25" onclick="clic(25)"><img src="cards/7D.svg"></td>
        <td id="carte29" onclick="clic(29)"><img src="cards/8D.svg"></td>
        <td id="carte33" onclick="clic(33)"><img src="cards/9D.svg"></td>
        <td id="carte37" onclick="clic(37)"><img src="cards/10D.svg"></td>
        <td id="carte41" onclick="clic(41)"><img src="cards/JD.svg"></td>
        <td id="carte45" onclick="clic(45)"><img src="cards/QD.svg"></td>
        <td id="carte49" onclick="clic(49)"><img src="cards/KD.svg"></td>
      </tr>
      <tr>
        <td id="carte2" onclick="clic(2)"><img src="cards/AH.svg"></td> 
        <td id="carte6" onclick="clic(6)"><img src="cards/2H.svg"></td>
        <td id="carte10" onclick="clic(10)"><img src="cards/3H.svg"></td>
        <td id="carte14" onclick="clic(14)"><img src="cards/4H.svg"></td>
        <td id="carte18" onclick="clic(18)"><img src="cards/5H.svg"></td>
        <td id="carte22" onclick="clic(22)"><img src="cards/6H.svg"></td>
        <td id="carte26" onclick="clic(26)"><img src="cards/7H.svg"></td>
        <td id="carte30" onclick="clic(30)"><img src="cards/8H.svg"></td>
        <td id="carte34" onclick="clic(34)"><img src="cards/9H.svg"></td>
        <td id="carte38" onclick="clic(38)"><img src="cards/10H.svg"></td>
        <td id="carte42" onclick="clic(42)"><img src="cards/JH.svg"></td>
        <td id="carte46" onclick="clic(46)"><img src="cards/QH.svg"></td>
        <td id="carte50" onclick="clic(50)"><img src="cards/KH.svg"></td>
      </tr>
      <tr>
        <td id="carte3" onclick="clic(3)"><img src="cards/AS.svg"></td> 
        <td id="carte7" onclick="clic(7)"><img src="cards/2S.svg"></td>
        <td id="carte11" onclick="clic(11)"><img src="cards/3S.svg"></td>
        <td id="carte15" onclick="clic(15)"><img src="cards/4S.svg"></td>
        <td id="carte19" onclick="clic(19)"><img src="cards/5S.svg"></td>
        <td id="carte23" onclick="clic(23)"><img src="cards/6S.svg"></td>
        <td id="carte27" onclick="clic(27)"><img src="cards/7S.svg"></td>
        <td id="carte31" onclick="clic(31)"><img src="cards/8S.svg"></td>
        <td id="carte35" onclick="clic(35)"><img src="cards/9S.svg"></td>
        <td id="carte39" onclick="clic(39)"><img src="cards/10S.svg"></td>
        <td id="carte43" onclick="clic(43)"><img src="cards/JS.svg"></td>
        <td id="carte47" onclick="clic(47)"><img src="cards/QS.svg"></td>
        <td id="carte51" onclick="clic(51)"><img src="cards/KS.svg"></td>
      </tr> 
    </table> 
    
    <div id = "options">
      <p id="conditions_du_jeu"> Vous pouvez encore 
      <button onclick="bouton_brasser_les_cartes()"> Brasser les cartes 
      </button><em id="counter"> 3 </em> fois </p>
      <button onclick="reinicialiser()"> Nouvelle partie </button>
    </div>
   
  </div>"""
    reinicialiser()