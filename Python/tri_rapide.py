
def tri_rapide(tab : list,debut : int, fin : int) -> list:
    if len(tab) <= 1:
        return tab
    else :
        idx_pivot = debut
        idx_gauche = debut + 1
        idx_droit = fin

        while idx_gauche < idx_droit :
            while tab[idx_gauche] <= tab[idx_pivot] :
                idx_gauche += 1
            while tab[idx_droit] >= tab[idx_pivot] :
                idx_droit -= 1

            tab[idx_droit],tab[idx_gauche]\
            = tab[idx_gauche],tab[idx_droit]

            idx_gauche += 1
            idx_droit -= 1

        tab = tab[1:idx_gauche]+\
        [tab[idx_pivot]]+tab[idx_droit+1:]