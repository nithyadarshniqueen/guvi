original =input('Enter a ch:')
ch = original.lower()
first = ch[0]

if len(original) > 0 and original.isalpha():
    if first in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print ("invalid")
