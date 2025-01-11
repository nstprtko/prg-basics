values = [48,47,54,50,42,68,39,46]
too_high = list(filter(lambda speed: speed >50, values))
values_form = ', '.join(map(str,values))
too_high_form = ', '.join(map(str,too_high))
print(f'Recorded values : {values_form}')
print(f'Speed too high : {too_high_form}')
