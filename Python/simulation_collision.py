
'''
________________________
|                      |
|                      |
|                  *   |
|                   *  |
|          .         * |
|           .         *|
|            .       * |
|             *     *  |
|              *   *   |
|               * *    |
|________________*_____|

• Domaine rectangulaire            : rectangle de taille 100x100
• Rayon des particules             : aléatoire uniforme [0.1 ; 5]
• Nombres des particules           : 10
• Couleur des particules           : aléatoire (à vous de choisir)
• Vitesse des particules suivant x : aléatoire uniforme entre -2 et 2
• Vitesse des particules suivant y : aléatoire uniforme entre -2 et 2

• Pour déterminer la nouvelle position, il suffit d'ajouter à la position la vitesse.

• Pour la collision entre deux particules i et j à des vitesses v_i et v_j :
                v_i = (v_i_x ; v_i_y) et v_j = (v_j_x ; v_j_y)
    On calcule :
                vx = v_j_x - v_i_x
                vy = v_j_y - v_i_y
    puis on calcule l'angle :
                angle =  math.atan2(vy, vx)
    puis on calcule :
                norme_vi = math.hypot(v_i_x, v_i_y)
                norme_vj = math.hypot(v_j_x, v_j_y)
    et on en déduit les nouvelles vitesses résultantes :
                v_i = (norme_vi * math.cos(angle) ; norme_vi * math.sin(angle))
                v_j = (norme_vj * math.cos(angle + math.pi) ; norme_vj * math.sin(angle + math.pi))
'''

from random import*
import math
import matplotlib.pyplot as plt

# Parametres
nbr_particule = 10
width, height = 100, 100
position = [10,40]
rayon = 2
speed = [1,-1]
couleur = [uniform(0,1),uniform(0,1),uniform(0,1)]
T=10000 # temps

# Fonctions

def collision_mur(position : list, speed):
    if position[0]+rayon >= width or position[0]-rayon <=0:
        speed[0] = 0 - speed[0]
    if position[1]+rayon >= height or position[1]-rayon <= 0:
        speed[1] =  0 - speed[1]

def nombre_individu(nbr_particule : int):

    nombre_indiv = nbr_particule
    liste_complète = []
    for i in range(nombre_indiv):
        liste_complète.append([])
    for l in range(len(liste_complète)):

            liste_complète[l].append(l+1)
            liste_complète[l].append(randint(1, 99))
            liste_complète[l].append(randint(1, 99))
    for t in range(len(liste_complète)):
        liste_complète[t].append(uniform(1,5))
    for c in range(len(liste_complète)):
        liste_complète[c].append([uniform(0,1),uniform(0,1),uniform(0,1)])
    for v in range(len(liste_complète)):
         liste_complète[v].append([uniform(-2,2),uniform(-2,2)])

    return(liste_complète)
    # résulat affiché : [[numéro de la particule,position en x,position en y,rayon,couleur,[vitesse x,vitesse y]]

def collision_particule(liste_complete):
    for i in range(len(liste_complete)-1):
        pos_i_x = liste_complete[i][1]
        pos_i_y = liste_complete[i][2]
        v_i_x = liste_complete[i][5][0]
        v_i_y = liste_complete[i][5][1]
        rayon_i = liste_complete[i][3]
        for j in range(i+1,len(liste_complete)):
            pos_j_x = liste_complete[j][1]
            pos_j_y = liste_complete[j][2]
            v_j_x = liste_complete[j][5][0]
            v_j_y = liste_complete[j][5][1]
            rayon_j = liste_complete[j][3]

            rayon = rayon_i + rayon_j

            if math.sqrt((pos_j_x - pos_i_x)**2+(pos_j_y - pos_i_y)**2) <= rayon:
                vx = v_j_x - v_i_x
                vy = v_j_y - v_i_y

                angle =  math.atan2(vy, vx)

                norme_vi = math.hypot(v_i_x, v_i_y)
                norme_vj = math.hypot(v_j_x, v_j_y)

                liste_complete[i][5][0] = norme_vi * math.cos(angle)
                liste_complete[i][5][1] = norme_vi * math.sin(angle)

                liste_complete[j][5][0] = norme_vj * math.cos(angle + math.pi)
                liste_complete[j][5][1] = norme_vj * math.sin(angle + math.pi)

    return liste_complete





# Simulation
fig, ax = plt.subplots() # Créer une figure et un axe

liste_complete = nombre_individu(nbr_particule)

for _ in range(T):
    ax.clear()  # Mettre à jour l'affichage (inutile)

    # Créer un cercle
    for elem in range(len(liste_complete)):
        cercle = plt.Circle([liste_complete[elem][1],liste_complete[elem][2]], liste_complete[elem][3], color= liste_complete[elem][4], fill=True)
        ax.add_patch(cercle)

    # Mise à jour de la position
    for elem in range(len(liste_complete)):
        collision_mur([liste_complete[elem][1],liste_complete[elem][2]],liste_complete[elem][5])
        liste_complete = collision_particule(liste_complete)
        liste_complete[elem][1] += liste_complete[elem][5][0]
        liste_complete[elem][2] += liste_complete[elem][5][1]

    # réglage des axes
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('Collisions des particules')
    plt.pause(0.01)  # Pause pour visualiser la simulation

# Afficher le plot final
plt.show()
