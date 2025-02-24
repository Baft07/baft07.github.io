
def fusion(tab1 : list, tab2 : list) -> list:
    """
    Prend en argument 2 listes triées et qui renvoie une liste contenant les
    éléments des 2 listes triés
    """
    idx1 = 0 #index qui parcours tab1
    idx2 = 0 #index qui parcours tab2

    tab_final = [] #liste qui contiendra les éléments de tab1 et tab2 triés

    while idx1 < len(tab1) and idx2 < len(tab2):
        if tab1[idx1] < tab2[idx2]:
            tab_final += [tab1[idx1]]
            idx1 += 1
        else :
            tab_final += [tab2[idx2]]
            idx2 += 1
    """
    une fois qu'une des deux liste initiale a été complètement parcouruel on
    ajoute ce qu'il reste de l'autre liste
    """
##    tab_final += [tab1[i] for i in range(idx1,len(tab1))]
##    tab_final += [tab2[i] for i in range(idx2,len(tab2))]

    while idx1 < len(tab1):
        tab_final += [tab1[idx1]]
        idx1 += 1
    while idx2 < len(tab2):
        tab_final += [tab2[idx2]]
        idx2 += 1

    return tab_final
