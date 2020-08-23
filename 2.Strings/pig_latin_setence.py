def pig_latin_setence():
    sentence = input("your sentence \n")
    new_sentence = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            new_sentence.append("{}way".format(word))
        
        else:
            sliced_word = word[1:]
            new_sentence.append("{}way".format(sliced_word))

    print(' '.join(new_sentence))

pig_latin_setence()