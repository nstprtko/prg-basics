paragraph = "cat dog mouse cat rat cat mouse"
words = paragraph.split()
word_dict ={}
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(word_dict)