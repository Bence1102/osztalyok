import fugvenyek
'''Hozz létre egy osztalyzatok listát és
osztalyzatok_lista=[3,4,5,2,3,4,5,4]
nevek=["Béla","Pista","Ági","Rozi",]

nevek és a nevekhez tartozó ostályok összetartoznak

etelek=["húsleves","krumplis"]
ar=[2134,3456]

Új adatszerkezet - ami egybe tudja kezelni az összetartozó adatokat

személy={név: "Béla", osztalyzat:3}

kaja1={nev:"húsleves",ar:2134}
kaja2={nev:"krumplis",ar:2134}

objektumok - tulajdonságokkal és viselkedéssel bíró adatszerkezet

Készítünk egy sablont, ami alapján le tudjuk gyártani a konkrét egyedeket.
OSZTÁLY -sablon - terjtajz
OBJEKTUM - konkrét egyedek - konkrét termék


'''


'''1.lépés: osztály létrehozása'''
"""konstruktor feladata, hogy  létrehozza a konkrét példányt
adatokkal a tervrajzból
beállítsa az adattagokat - objektum tulajdonságok értékei
"""
        

'''from Etel import Etel

"""2.létrehozzuk a konkrét példányt a tervrajz alapján"""
etel1=Etel("Húsleves",1234)
etel2=Etel("Krumplis",2345)
etel3=Etel("Rántott hús",2645)
etel4=Etel("Palacsinta",1345)
etel_lista=[]
etel_lista.append(Etel("Húsleves",1234))
etel_lista.append(Etel("Rántott hús",2645))
etel_lista.append(Etel("Rántott hús",2645))
etel_lista.append(Etel("Palacsinta",1345))

print("Szia én vagyok a minimanó " +etel1.nev+" Az állapotom " + etel1.allapot)
etel1.keszul()
print("Szia én vagyok a minimanó " +etel1.nev+ " Az állapotom " + etel1.allapot)
print("Szia én vagyok a minimanó " +etel2.nev+ " Az állapotom " + etel2.allapot)



"""Irj egy metódust, amely paraméterben megkapja a listát és kiírja az 
    ételek neveit és árait látványo formában"""

fugvenyek.etlap(etel_lista)


Irj metódust,...., az ételek átlagárát
atlag_ar=fugvenyek.atlag_ar(etel_lista)
print(f"Az ételek átlagára: {atlag_ar}")

irj metódust... a legdrágább ételek nevét és árát irjuk ki
max_i=fugvenyek.legdragabb(etel_lista)
print(f"A legdrágább étel neve és ára {etel_lista[max_i].nev}, {etel_lista[max_i].ar}")


print(etel_lista[0])'''


"""hoz létre egy alkalmazott osztalyt, amelyikben az infókat 
tudod tárolni egy cég dolgozóiról:
nev
szul_datum
fizetes
pozicio
kor

készíts kor metodust, ami megmodnja az adott ember korát
__str__

hozz létre legalább 5 embert, tedd bele őket listába
-mennyi az össz fizetés
-Hány éves a legidősebb ember
-hány ember van "beosztott" pozicióban?
-kinek a legalancsonyabb a fizetése?

++ az osztáynak legyen fizetés emelés metodusa, amely a fizetést 
megemeli a paraméterben megadott százalék értékkel.
A legkisebb fizetésű ember fizetés emeld meg 20%-al.

"""


from Alkalmazott import Alkalmazott

dolgozo1=Alkalmazott("Farkas Piroska", 1998, 500.000, "beosztott")
dolgozo2=Alkalmazott("Füty Imre", 1995, 320.000, "beosztott")
dolgozo3=Alkalmazott("Hiszékeny Mónika", 1949, 450.000, "vezető")
dolgozo4=Alkalmazott("Viz Elek",1990, 300.000, "beosztott")
dolgozo5=Alkalmazott("Hát Izsák",1987, 350.000, "beosztott")
alkalmazottak = []
alkalmazottak.append(Alkalmazott("Farkas Piroska", 1998, 500000, "beosztott"))
alkalmazottak.append(Alkalmazott("Füty Imre", 1995, 320000, "beosztott"))
alkalmazottak.append(Alkalmazott("Hiszékeny Mónika", 1949, 450000, "vezető"))
alkalmazottak.append(Alkalmazott("Viz Elek",1990, 300000, "beosztott"))
alkalmazottak.append(Alkalmazott("Hát Izsák",1987, 350000, "beosztott"))

fugvenyek.dolgozo(alkalmazottak)

osszes_fizetes = fugvenyek.osszfizetes(alkalmazottak)
print(f"Összes fizetés: {osszes_fizetes} Ft")
legidosebb_dolgozo=fugvenyek.legidosebb(alkalmazottak)
print(f"Legisősebb alkalmazott: {legidosebb_dolgozo}")



