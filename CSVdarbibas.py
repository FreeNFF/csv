import csv

with open("boja_gajusies.csv",encoding="utf-8") as file:
    csv1 = csv.reader(file)
    saraksts = list(csv1)
    print("Izdruka ir: ", saraksts)
    print("--------------------------------------------------------")
    print("Datnes nosaukums ir: ", file.name)

#masīva garums
print("--------------------------------------------------------")
garums = len(saraksts)
print("Rindu skaits: ",garums)
print("--------------------------------------------------------")

#pirmais elements
pirmais = saraksts[1]
print("Pirmais elements: ",pirmais)
print("--------------------------------------------------------")

pieci = saraksts[1:6]
print("Pirmie pieci elementi: ", pieci)

def elements():
    karta = int(input("Ievadiet, kuru elementu jūs vēlaties redzēt: "))
    print("Izvēlētais elements ir ",karta,": ", saraksts[karta])

elements()