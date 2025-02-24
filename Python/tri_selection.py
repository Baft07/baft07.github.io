
def tri_selection(l : list) -> list:
    for i in range(len(l)-1):
        min = i
        for j in range(i,len(l)):
            if l[j] < l[min]:
                min = j
        l[min],l[i] = l[i],l[min]
    return l