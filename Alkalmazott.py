from datetime import datetime

class Alkalmazott:
    def __init__(self, nev:str="", szul_datum:str="", fizetes:int=1000, pozicio:str=""):
        self.nev = nev
        self.szul_datum = szul_datum
        self.fizetes = fizetes
        self.pozicio = pozicio
        self.kor=self.korbeallit()

    def korbeallit(self):
        jelenlegi_ev=datetime.now().year
        return jelenlegi_ev - self.szul_datum

    def __str__(self):
        return f"Név: {self.nev}, Kor: {self.kor}, Fizetés: {self.fizetes}, Pozíció: {self.pozicio}"

    





