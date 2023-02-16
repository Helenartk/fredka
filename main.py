zmienna= "ciąg znaków"
print(len(zmienna)) # drukuje na ekranie i liczy ilość znaków
print(zmienna[1:5]) # drukuje od 2 do 6 znaku
print(zmienna[2:]) # drukuje od 3 znaku do końca
print(zmienna[-1]) # drukuje ostatni znak od końca
print(zmienna[:5]) # drukuje od początku do 6 bznaku
print(zmienna[:]) # skrajne z obu końców
print(zmienna[::2]) # co drugi znak od początku do końca

# [x:y:z]
# x-początek y-koniec z-korok
print(zmienna) #caly string

imie = "Helena"
nazwisko = "Rutkowska"
print(imie +" " +nazwisko) #" " spacja prezy drukowaniu
print(imie * 3, nazwisko, end="\n") # (,) spacja, (\n) kończy linię
print(imie * 3, nazwisko, end="---\n") # (*) razy (ctrl d) kopiuje linie!!!

print(f"witaj{imie}ghfjafsiGGFHG") # (f) pokazuje, że to zformatowany string musi być na początku
print(type(imie)) #drukuje typ zmiennej

x = input("Podaj swój wiek") # jak zapominiałam wstawić cudzysłów to zaznaczam wsztko i klikam cudzysłów od razu daje dwa
print(int(x) + 2) #zmienićtyp zmiennej

james_bond = 7 #nasz cel 007
# .zfill()
print(james_bond.zfill(3)) # to jest żle i mamy znależć problem
print(str(james_bond).zfill(3))




