sentence = 'I completely agree with you'
result = list(map(lambda word: len(word), sentence.split()))
print(f"Text : {sentence}")
print(result)