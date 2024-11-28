import csv

with open("kugosana.csv",encoding="utf-8") as file:
    csv = csv.reader(file)
    saraksts = list(csv)

print("Faila nosaukums:",file.name)
print(saraksts)