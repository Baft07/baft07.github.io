
def tri_insertion(tab : list) :
    for i in range(1,len(tab)):
        val_à_inserer = tab[i]
        j = i-1
        while tab[j] > val_à_inserer and j >=0 :
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = val_à_inserer
    return(tab)