#!/usr/bin/python3

import zipfile
from timeit import default_timer as timer
from collections import deque

zip_file = 'secret.zip' # works for test.zip but takes too long on secret.zip (tried all combinations of 6 characters)

zip_file = zipfile.ZipFile(zip_file)

characters = ['matthew', 'spencer', 'elizabeth', 'alfred', '1979', 'birmingham', 'hemmingwood', 'spiffy', 'programmer', 'doctor']
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
