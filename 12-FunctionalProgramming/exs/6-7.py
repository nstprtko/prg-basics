def ski(arr):

    result = list(map(lambda scores: sum(scores)-max(scores)-min(scores), ratings))
    return result

ratings = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

my_ski = ', '.join(map(str,ski(ratings)))
print(my_ski)