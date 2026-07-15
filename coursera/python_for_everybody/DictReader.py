import csv

ppl = []

with open("spirits.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        ppl.append({"name": row["name"], "home": row["home"]})

for person in sorted(ppl, key=lambda person: person["name"]):
    print(f"{person['name']} is from {person['home']}")