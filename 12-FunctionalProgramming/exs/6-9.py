temperatures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

positive = list(filter(lambda city : temperatures[city] > 0, temperatures))
print(f'cities with positive temp : {', '.join(map(str,positive))}')