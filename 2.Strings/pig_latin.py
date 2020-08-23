def pig_latin():
    word = input("your word \n")
    if word[0] in 'aeiou':
        return "{}way".format(word)
      
    else:
        sliced_word = word[1:]
        return "{}ay".format(sliced_word)

print(pig_latin())