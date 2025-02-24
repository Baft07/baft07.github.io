
def tri_bulle(L : list,) -> list:
    n = len(L)
    echange=True
    while echange :
        echange = False
        for j in range(0,n-cpt):
            if L[j]<L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                echange = True
    return(L)
