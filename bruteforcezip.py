#!/usr/bin/python3

import zipfile
from timeit import default_timer as timer
from collections import deque

zip_file = 'test.zip' # works for test.zip but takes too long on secret.zip (tried all combinations of 6 characters)

zip_file = zipfile.ZipFile(zip_file)

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
to_try = deque(characters)

start = timer()
while to_try:
    word = to_try.popleft()
    print(f'trying word: {word}')
    try:
        zip_file.extractall(pwd=bytes(word, 'utf-8'))
    except:
        for character in characters:
            to_try.append(word + character)
    else:
        print(f'[+] Password found in {timer() - start} seconds: {word}')
        exit(0)


print('[!] Password not found, try other words.')
