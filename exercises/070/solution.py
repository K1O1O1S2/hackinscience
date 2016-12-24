#!/usr/bin/python
alphabet = range(97, 123, 1)
i = 0
for letter1 in alphabet:
    for letter2 in alphabet:
        if letter1 != letter2:
            print(chr(letter1) + chr(letter2))
