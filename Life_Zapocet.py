#######################
###   Life - hra    ###
### Daniel Bartušek ###
###     NPRG011     ###
#######################
import random
import time
import copy
import sys
import msvcrt
import re

##TBD##
#unittest podle priklad zip-testy

class HraciPlocha:
    # Na začátku hry potřebujeme nastavit velikost pole
    def __init__(self, vyska, typ, pole, volbaUtvaru = None):
        self.vyska = vyska
        self.pole = pole
        self.typ = typ
        self.abecedaList = self.abeceda()
        self.povoleneZnaky = ['0','1','O','-']

        #Nastaveni tvorby pole
        if (self.pole == 1):
             self.stav = self.novePole()
        if (self.pole == 2):
            self.stav = self.vlastniPole()
        elif (self.pole == 3):
            #Nastavení předdefinovaného útvaru
            if volbaUtvaru == 1:
                self.stav = self.fumarole()
            elif volbaUtvaru == 2:
                self.stav = self.pentomino()
            elif volbaUtvaru == 3:
                self.stav = self.boatmaker()
            #Tvorba pole pro počítání přežitých kol každé buňky.
        if self.typ == 3:
            self.poctyZivych = self.countZivota(self.stav)

    # Vygenerování náhodného startovacího pole
    def novePole(self):
        poleSloupcu = [None]*self.vyska # Vygenerováním prázného pole předem se ušetří čas u přiřazování hodnot.
        for x in range(self.vyska):
            sloupec = [None]*self.vyska
            for y in range(self.vyska):
                sloupec[y] = random.choice('-''O')# Pro každé políčko se náhodně přiřadí 0 (mrtvá buňka) nebo 1 (živá buňka)
            poleSloupcu[x] = sloupec
        return poleSloupcu

    def vlastniPole(self):
        pole = x = [[None]*self.vyska for i in range(self.vyska)]
        x = 0
        y = 0
        # Protože uživatel bude pole specifikovat po řádcích v konzoli, je lepší v tomto případě plnit také po řádcích.
        while True:
            znak = sys.stdin.read(1)
            while znak not in self.povoleneZnaky:
                if znak == '\n':
                    znak = sys.stdin.read(1)
                    if znak == '\n':
                        print(f"Ještě zbývá naplnit {self.vyska*self.vyska-self.vyska*y-x} polí.") # V případě, že autor odenteruje prázdný řádek, chceme mu napovědět, co má dělat.
                    elif znak in self.povoleneZnaky:
                        break
                znak = sys.stdin.read(1) #Dosazujeme jen žívé nebo mrtvé buňky. Ostatní znaky, jako například odenterování, mezery nebo chybně zadané znaky nebereme v úvahu.
            if znak == '1' or znak == 'O':
                pole[x][y]='O'
            else:
                pole[x][y]='-'
            x+=1 #Doplnili jsme buňku, posopuváme ukazatel na další pole.
            if x == self.vyska:
                #Máme plné pole
                if y == self.vyska-1:
                    return pole
                #Máme konec řádku
                else:
                    y+=1
                    x = 0

    ##Výčet písmen pro označování sloupců
    def abeceda(self):
        return ["  ",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #První prvek je mezera pro zajištění odsazení.

    #Generujeme pole, které každé buňce počítá počet jejich období, co přežila
    def countZivota(self,pole):
        poleSloupcu = [None]*self.vyska 
        for x in range(self.vyska):
            sloupec = [0]*self.vyska # Ze začátku natavíme všem buňkám 0, protože ještě nepřežily žádné období.
            for y in range(self.vyska):
                if pole[x][y] == 'O':
                    sloupec[y] == 1
            poleSloupcu[x] = sloupec
        return poleSloupcu
    
    def stred(self):
        #Vycentrování obrazců podle parity velikosti pole
        if self.vyska % 2 == 0:
            stred = self.vyska//2-1
        else:
            stred = self.vyska//2
        return stred


    #Tvorba předdefinovaných polí
    def pentomino(self):
        stred = self.stred()
        pole = [["-" for x in range(self.vyska)] for y in range(self.vyska)]
        pole[stred+2][stred]= 'O'
        pole[stred+1][stred+1]= 'O'
        pole[stred][stred-1]= 'O'
        pole[stred+1][stred-1]= 'O'
        pole[stred+2][stred-1]= 'O'
        return pole

    def boatmaker(self):
        stred = self.stred()
        pole = [["-" for x in range(self.vyska)] for y in range(self.vyska)]
        pole[stred+1][stred-1]= 'O'
        pole[stred+2][stred-2]= 'O'
        pole[stred+3][stred-3]= 'O'
        pole[stred+4][stred-4]= 'O'
        pole[stred+5][stred-5]= 'O'
        pole[stred+6][stred-6]= 'O'
        pole[stred+7][stred-6]= 'O'
        pole[stred+7][stred-5]= 'O'
        pole[stred][stred]= 'O'
        pole[stred-1][stred+1]= 'O'
        pole[stred-2][stred+2]= 'O'
        pole[stred-3][stred+3]= 'O'
        pole[stred-4][stred+4]= 'O'
        pole[stred-5][stred+5]= 'O'
        pole[stred-6][stred+6]= 'O'
        pole[stred-6][stred+7]= 'O'
        pole[stred-6][stred+8]= 'O'
        pole[stred-6][stred+9]= 'O'
        pole[stred-6][stred+10]= 'O'
        pole[stred-7][stred+6]= 'O'
        pole[stred-8][stred+6]= 'O'
        pole[stred-9][stred+6]= 'O'
        pole[stred-10][stred+6]= 'O'
        return pole

    def fumarole(self):
        stred = self.stred()
        pole = [["-" for x in range(self.vyska)] for y in range(self.vyska)]
        pole[stred][stred-3]= 'O'
        pole[stred+1][stred-3]= 'O'
        pole[stred-2][stred-2]= 'O'
        pole[stred+3][stred-2]= 'O'
        pole[stred-2][stred-1]= 'O'
        pole[stred+3][stred-1]= 'O'
        pole[stred-2][stred]= 'O'
        pole[stred+3][stred]= 'O'
        pole[stred-1][stred+1]= 'O'
        pole[stred+2][stred+1]= 'O'
        pole[stred-1][stred+2]= 'O'
        pole[stred+2][stred+2]= 'O'
        pole[stred-3][stred+2]= 'O'
        pole[stred+4][stred+2]= 'O'
        pole[stred-3][stred+3]= 'O'
        pole[stred+4][stred+3]= 'O'
        pole[stred-2][stred+3]= 'O'
        pole[stred+3][stred+3]= 'O'
        return pole

    #Vyhodnocení stávajícího pole a tvorba nového
    def vyhodnotNove(self):
        ziveOkoli = 0 #Pro ukládání počtu živých sousedních buněk.
        poleSloupcu = [None]*self.vyska
        for x in range(self.vyska):
            novySloupec = ['-']*self.vyska
            for y in range(self.vyska):
                if y>=1 and self.stav[x][y-1]=='O': # Buňka není na horním okraji self.stav, takže se můžeme ptát na horního souseda.
                    ziveOkoli += 1
                if x>=1 and self.stav[x-1][y]=='O': # Buňka není na levém okraji self.stav, takže se můžeme ptát na levého souseda.
                    ziveOkoli += 1
                if x+1<self.vyska and self.stav[x+1][y]=='O': # Buňka není na pravém okraji self.stav, takže se můžeme ptát na pravého souseda.
                    ziveOkoli += 1
                if y+1<self.vyska and self.stav[x][y+1]=='O': # Buňka není na dolním okraji self.stav, takže se můžeme ptát na dolního souseda.
                    ziveOkoli += 1
                if x+1<self.vyska and y>=1 and self.stav[x+1][y-1]=='O': # Buňka není na pravém ani horním okraji, takže se můžeme ptát na souseda vpravo nahoře
                    ziveOkoli += 1
                if x+1<self.vyska and y+1<self.vyska and self.stav[x+1][y+1]=='O': # Buňka není na pravém ani dolním okraji, takže se můžeme ptát na souseda vpravo dole.
                    ziveOkoli += 1
                if x>=1 and y>=1 and self.stav[x-1][y-1]=='O': # Buňka není na levém ani horním okraji, takže se můžeme ptát na souseda vlevo nahoře
                    ziveOkoli += 1
                if x>=1 and y+1<self.vyska  and self.stav[x-1][y+1]=='O': # Buňka není na levém ani horním okraji, takže se můžeme ptát na souseda vlevo dole
                    ziveOkoli += 1

                #Vyhodnocení stavu každé buňky, a přiřazení nové hodnoty do sloupce nového pole "novySloupec"
                #Ošetřujeme pouze stavy, kdy bude v novém poli 1. Pokud buňka neoživne, už tam je nastavená 0, a není potřeba nic měnit.
                if self.stav[x][y] == 'O' and ziveOkoli>=2 and ziveOkoli<4: #Živá buňka buňka s 2 a více žijícími sousedy, takže přežije do dalšího tahu, a zkopíruje se do nového pole.
                    novySloupec[y] = 'O'
                elif self.stav[x][y] == '-' and ziveOkoli==3: #Mrvtá buňka má 3 živé sousedy, takže oživne. Nemůže však vzniknou, pokud má 4 a více sousedů, protože nemá prostor.
                    novySloupec[y] = 'O'
                elif self.stav[x][y] == 'O' and ziveOkoli>=4: #Buňka má moc sousedů a umírá na nedostatek prostoru.
                    novySloupec[y] = '-'
                ziveOkoli = 0
            poleSloupcu[x] = novySloupec

            #Přepočet počtu přeživších buněk
        if self.typ == 3:
            for x in range(self.vyska):
                for y in range(self.vyska):
                    if poleSloupcu[x][y] == 'O': 
                        self.poctyZivych[x][y] += 1 #Pokud v novém poli je žijící buňka, zvýšíme její počet přežitých kol. (V opačném případě umřela, ale počet přežitých kol jí zůstává)
        return poleSloupcu
           
    def tiskarna(self,pole):
        global kolo
        if self.typ != 3:
            print("\n") #Mezera mezi tahy pro lepší rozlišení.

        #pokud tiskneme počty přežitých kol, musíme zarovnat na počet jednotek, které má max.
        #tisk počtů poznáme tak, že v náhodném políčku je číslice
        if (isinstance(pole[0][0],int)):

            #max = self.findMax()
            #delka = str(len(str(max)))
            #odsazeni = "%"+delka+"d"
            #print(abeceda[0],end = "")
            for i in range(self.vyska+1): #První tiskneme mezeru, takže musíme zvýšit range o 1
                print(self.abecedaList[i],end = "  ") #Tisk označení sloupců s odsazením podle počtu číslic v nejdéle žijící buňce.
            print()
            radek = 1 #Counter pro označení řádků
            for y in range(self.vyska):
                print("%2d" %radek, end = " ")
                radek += 1
                for x in range(self.vyska):
                    print("%2d" %pole[x][y], end = " ") #Po řádcích se vytiskne stav pole. Výška y se pro druhý for loop nemění.
                print() # Na konci řádku se přesouváme na další řádek.
        #Jinak tiskneme jen stav buněk, které jsou vždy dlouhé jeden znak, a není třeba řešit formátování.
        else:
            for i in range(self.vyska+1): #První tiskneme mezeru, takže musíme zvýšit range o 1
                print(self.abecedaList[i],end = " ") #Tisk označení sloupců
            print()
            radek = 1 #Counter pro označení řádků
            for y in range(self.vyska):
                print("%2d" %radek, end = " ")
                radek += 1
                for x in range(self.vyska):
                    print(pole[x][y], end = " ") #Po řádcích se vytiskne stav pole. Výška y se pro druhý for loop nemění.
                print() # Na konci řádku se přesouváme na další řádek.

    def novyTah(self):
        self.stav = self.vyhodnotNove() #Naplnění nového pole na základě obsazení stávajícího.  

     #Najdi buňku s nejvíce přežitými koly.
    def findMax(self):
        max = self.poctyZivych[0][0]
        for x in range(self.vyska):
            for y in range(self.vyska):
                if max < self.poctyZivych[x][y]:
                    max = self.poctyZivych[x][y]
        return max
    def typ3(self,sazkaBunka):
        y_sazka = int(sazkaBunka[1:])-1 #Řádky jsou číslované od 1, takže index zmenšíme o 1
        x_sazka = self.abecedaList.index(sazkaBunka[0])-1 ##protože máme ve výčtu sloupců mezeru, index musíme zmenšit o 1. 
        print("Počty kol, které jednotlivé buňky přežily :")
        self.tiskarna(self.poctyZivych) # Tisk aktuálního pole s počty
        max = self.findMax()

        #Pokud na hráčem vybrané pozici je bunka, která žila stejně dlouho, jako identifikované maximum, hráč vyhrál
        if max == self.poctyZivych[x_sazka][y_sazka]:
            print("Gratulujeme, vaše vybraná buňka je jednou z nejdéle žijících.")
        else:
            print("Bohužel jsou v poli buňky, které přežily déle.")
                   

    def checkSymetrie(self):
        #Kontrolujeme podle osy y
        i=0 #Counter pro počet asymetrických prvků.
        
        if self.vyska %2 == 1:
            range_x = self.vyska//2-1 #Při liché velikosti nechceme zajít až k prostřednímj sloupci.
        else:
            range_x = self.vyska//2
        for y in range(self.vyska):
            for x in range(self.vyska//2):
                if self.stav[x][y] != self.stav[-(x+1)][y]: #x[0] == x[-1]
                    print(f"Políčko na pozici {self.abecedaList[x+1]}{y+1} není symetrické s políčkem na pozici {self.abecedaList[self.vyska-x]}{y+1}...")
                    i+=1
        if i == 0:
            print("Obrazec je symetrický")

    def zmenTri(self,vstup):
        for i in range(min(3,len(vstup))): #Pokud se uživateli podařilo zadat více změn, provedou se jen první 3 požadavky.
            policko = vstup[i]
            y_pick = int(policko[1:])-1 #Řádky jsou číslované od 1, takže index zmenšíme o 1
            x_pick = self.abecedaList.index(policko[0])-1 ##protože máme ve výčtu sloupců mezeru, index musíme zmenšit o 1.
            if self.stav[x_pick][y_pick] == 'O':
                self.stav[x_pick][y_pick] = '-'
            else:
                self.stav[x_pick][y_pick] = 'O'
        return self.stav




#Kontrola správného vstupu
while True:
    try:
        vyska = int(input("Zadejte veliost pole v rozashu 2-26: "))
    except ValueError:
        print ("Prosím, zadejte číselnou hodnotu")
    else:
        if 2<=vyska<=26:
            break
        else:
            print("Výška není v povoleném rozsahu")

print()

print("Zadej typ hry:")
print("     1. Běžná simulace")
print("     2. Doplnění do symetrie")
print("     3. Sázka na život")

#Kontrola správného vstupu
while True:
    try:
        typ = int(input())
    except ValueError:
        print ("Prosím, zadejte číselnou hodnotu")
    else:
        if typ == 1 or typ == 2 or typ == 3:
            break
        else:
            print("Zadejte validní typ")

print()

print("Zadej způsob tvorby pole:")
print("     1. Náhodné pole")
print("     2. Vlastní pole")
print("     3. Vybraný útvar")

#Kontrola správného vstupu
while True:
    try:
        pole = int(input())
    except ValueError:
        print ("Prosím, zadejte číselnou hodnotu")
    else:
        if pole == 1 or pole == 2:
            break
        elif pole == 3 and vyska<20:
            print("Pro tento typ je potřeba zadat větší výšku větší než 20, prosím zvolte jiný typ")
        elif pole ==3 and vyska>=20:
            break
        else:
            print("Zadejte validní tvorbu pole")

print()

if pole == 3:
    print("Zadej číslo útvaru:")
    print("     1. fumarole")
    print("     2. pentomino")
    print("     3. boatmaker")

    #Kontrola správného vstupu
    while True:
        try:
            volbaUtvaru = int(input())
        except ValueError:
            print ("Prosím, zadejte číselnou hodnotu")
        else:
            if 1<=volbaUtvaru<=3:
                break
            else:
                print("Zadejte validní útvar")
    life = HraciPlocha(vyska,typ,pole,volbaUtvaru)
else:
    life = HraciPlocha(vyska,typ,pole)

#Běžná simulace
if typ == 1:
    kolo = 0
    zmenaTed = False
    while kolo<=10: #Počet kol není nastavitelný hráčem
        life.tiskarna(life.stav)
        life.novyTah()   
        kolo+=1
        time.sleep(1)
    print("Konec simulace")

# Doplnění do symetrie
elif typ == 2:
    kolo = 0
    zmenaTed = False
    while kolo<=10:
        life.tiskarna(life.stav)
        kolo+=1
        t0 = time.time()
        try:
            print("Pokud si přejete vstoupit tento tah, stiskněte ctrl+c")
            time.sleep(1)
        except KeyboardInterrupt:
            zmenaTed = True
            break
        life.novyTah()

    if zmenaTed:
        spatnyVstup = False
        print("Zadejte pole, která chcete změnit (ve tvaru \"a1 d3 c17\"):")

        #Kontrola správného vstupu
        while True:
            polickaZmeneni = input()
            vstupniList = polickaZmeneni.split()

            #Kontrola korekntího vstupu      
            for i in range(min(3,len(vstupniList))): #Pokud se uživateli podařilo zadat více změn, provedou se jen první 3 požadavky. ###zmenit TBD
                policko = vstupniList[i]
                if policko[0] in life.abecedaList[1:1+vyska] and policko[1:].isnumeric() and int(policko[1:])<=vyska:
                    pass
                else:
                    spatnyVstup = True

            if spatnyVstup:
                print("Prosím, zadejte správný vstup")
                spatnyVstup = False
            else:
                 break

        life.stav = life.zmenTri(vstupniList)
        life.tiskarna(life.stav)
        life.checkSymetrie()
    else:
        print("Zdá se, že jste nezadal žádnou změnu")

#Sázka na život
elif typ == 3:
    kolo = 1
    life.tiskarna(life.stav)
    life.novyTah()
    print("Prosím, označte buňku, na kterou vsázíte, přežije nejdéle")
    print("Nejdřív zadejte písmeno sloupce, poté číslo řádku (ve formátu \"b5\")")
    spatnyVstup = False

    #Kontrola správného vstupu
    while True:
        sazkaBunka = input()
        if sazkaBunka[0] in life.abecedaList[1:1+vyska] and sazkaBunka[1:].isnumeric() and int(sazkaBunka[1:])<=vyska:
            pass
        else:
            spatnyVstup = True

        if spatnyVstup:
            print("Prosím, zadejte správný vstup")
            spatnyVstup = False
        else:
                break

    while kolo<=10:
        life.tiskarna(life.stav)
        life.novyTah()
        kolo+=1
        time.sleep(1)
    life.typ3(sazkaBunka) #Necháme hru dojet do konce, pak vyhodnotíme životy buněk.