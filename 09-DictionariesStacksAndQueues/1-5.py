countries = [
{"name":"Poland", "population":38000000},
{"name":"Germany", "population": 80000000},
{"name":"Sweden", "population": 10000000},
{"name":"France", "population": 68000000},
{"name":"Spain", "population": 48000000},
]
print("COUNTRY   POPULATION")
for item in countries:
    name = item['name']
    population = item['population']
    print(name, population)