def f(name):
    return ''.join(word[0] for word in name.split())

print(f('Python'))