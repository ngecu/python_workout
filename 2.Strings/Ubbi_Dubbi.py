def ubbi_dubbi(word):
    final_word = []
    for letter in word:
        if letter in 'aeiou':
            final_word.append("ub"+letter)
        else:
            final_word.append(letter)
    return(''.join(final_word))        
 
print(ubbi_dubbi("elephant"))