#!/usr/bin/python
alphabet = range(97, 123, 1)
i = 0
for letter1 in alphabet:
    for letter2 in alphabet:
        print(chr(letter1) + chr(letter2))
