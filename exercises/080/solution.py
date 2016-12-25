#!/usr/bin/python
alphabet = range(97, 123, 1)
n = 26
k = 2
for letter1 in alphabet:
    for letter2 in alphabet:
        if letter1 != letter2:
            if letter1 < letter2:
                print(chr(letter1) + chr(letter2))
       
