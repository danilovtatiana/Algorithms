'''
Write the corresponding index number for  each letter from the alphabet
'''

from string import ascii_lowercase #import the alphabet

alphabet = { #created a dictionary
    "a": 1,
    "b": 2
}
value = 1
for i in ascii_lowercase:
    if i in alphabet:
        print(i,alphabet[i])
    else:
        alphabet.update({i:value})
        print(i,alphabet[i])
    value += 1