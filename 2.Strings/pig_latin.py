def pig_latin():
    word = input("your word \n")
    if word[0] in 'aeiou':
        print("{}way".format(word))
      
    else:
        sliced_word = word[1:]
        print ("{}ay".format(sliced_word))

pig_latin()