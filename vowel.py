original =input('Enter a word:')
word = original.lower()
first = word[0]

if len(original) > 0 and original.isalpha():
    if first in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print ("invalid")
    
