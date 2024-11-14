
def etlap(lista):
    '''Itt irjuk ki az ételek neveit'''
    for i in range(0, len(lista),1):
        print(f"** {lista[i].nev} {lista[i].ar:>10}Ft **")

def atlag_ar(lista):
    osszeg:float=0
    for i in range(0, len(lista),1):
        osszeg+=lista[i].ar
        return osszeg/len(lista)
    
def legdragabb(lista):
    max_index=0
    for i in range(0, len(lista),1):
        if(lista[i].ar>lista[max_index].ar):
            max_index=i
    return max_index







def dolgozo(lista):
    for i in range(0, len(lista),1):
        print( f"Név: {lista[i].nev}, Kor: {lista[i].kor}, Fizetés: {lista[i].fizetes}, Pozíció: {lista[i].pozicio}")

def osszfizetes(lista):
    ossz:int=0
    for i in range(0, len(lista),1):
        ossz+=lista[i].fizetes
    return ossz

def legidosebb(lista):
    max_index=0
    for i in range(0, len(lista),1):
        if(lista[i].kor>lista[max_index].kor):
            max_index=i
    return lista[max_index]