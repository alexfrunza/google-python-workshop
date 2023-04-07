"""
    Acest program verfica daca un string primit de la tastatura este un CNP
    valid
"""

# Am folosit aceasta biblioteca pentru a termina executia programului mai
# devreme
import sys

cnp = input("Adauga un CNP pentru validare: ")

if len(cnp) != 13:
    print("CNP-ul are o lungime gresita!")
    sys.exit()

# Metoda isdigit(), returneaza true doar daca toate caracterele sunt cifre
if not cnp.isdigit():
    print("CNP-ul contine caractere invalide!")
    sys.exit()

# Prima cifra trebuie sa fie intre 1 si 9
if cnp[0] == "0":
    print("Prima cifra din CNP este invalida!")
    sys.exit()

if cnp[0] in {"5", "6"} and int(cnp[1:3]) > 23:
    print("CNP-ul nu este corect, deoarece apartine unei persoane care"
          "inca nu s-a nascut!")
    sys.exit()

if not (1 <= int(cnp[3:5]) <= 12):
    print("Luna din CNP este invalida!")
    sys.exit()

if cnp[5:7] == "00":
    print("CNP-ul nu are o zi valida!")
    sys.exit()

# Calculare an de nastere, pentru a vedea ulterior daca anul este bisect
# ne va ajuta sa verificam daca luna februarie are un numar valid de zile
elif cnp[0] in {"3", "4"}:
    an = "18"
elif cnp[0] in {"5", "6"}:
    an = "20"
else:
    an = "19"

an += cnp[1:3]
an = int(an)

an_bisect = False
if (an % 4 == 0 and an % 100 != 0) or an % 400 == 0:
    an_bisect = True

luni_cu_31_zile = {1, 3, 5, 7, 8, 10, 12}
luni_cu_30_zile = {4, 6, 9, 11}

# Verificam daca numarul de zile din luna corespunde cu luna
if int(cnp[3:5]) in luni_cu_30_zile and int(cnp[5:7]) > 30:
    print("CNP-ul nu are o zi valida!")
    sys.exit()

if int(cnp[3:5]) in luni_cu_31_zile and int(cnp[5:7]) > 31:
    print("CNP-ul nu are o zi valida!")
    sys.exit()

if cnp[3:5] == "02" and an_bisect and int(cnp[5:7]) > 29:
    print("CNP-ul nu are o zi valida!")
    sys.exit()

if cnp[3:5] == "02" and not an_bisect and int(cnp[5:7]) > 28:
    print("CNP-ul nu are o zi valida!")
    sys.exit()

# Testare cod judet/sector
if not (1 <= int(cnp[7:9]) <= 52):
    print("CNP-ul nu are un cod de judet/sector valid!")
    sys.exit()

# Numarul NNN din CNP trebuia sa ia valori intre 001 si 999
if cnp[9:12] == "000":
    print("CNP-ul nu are indicele NNN corect!")
    sys.exit()

# Calculare cifra de control a CNP-ului dat si verificarea cu cifra de control
# din CNP
control_number = "279146358279"
control_sum = 0
for cifra_cnp, cifra_c in zip(cnp, control_number):
    control_sum += int(cifra_cnp) * int(cifra_c)

control_digit = 1 if control_sum % 11 == 10 else control_sum % 11

if cnp[12] != str(control_digit):
    print("Cifra de control a CNP-ului nu este corecta")
    sys.exit()

print("CNP-ul introdus este valid!")
