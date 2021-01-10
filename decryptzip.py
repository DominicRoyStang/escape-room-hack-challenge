#!/usr/bin/python3

import zipfile

zip_file = 'test.zip'

zip_file = zipfile.ZipFile(zip_file)

words = ['hunter1', 'secret', 'dcba'] # works for test.zip but we need it to work on secret.zip

for word in words:
    print('trying word:', word)
    try:
        zip_file.extractall(pwd=bytes(word, 'utf-8'))
    except:
        continue
    else:
        print('[+] Password found:', word)
        exit(0)

print('[!] Password not found, try other words.')
