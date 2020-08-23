def ubbi_dubbi(word):
    final_word = []
    for letter in word:
        if letter in 'aeiou':
            final_word.append("ub"+letter)
        else:
            final_word.append(letter)
    print(''.join(final_word))        
 
ubbi_dubbi("elephant")