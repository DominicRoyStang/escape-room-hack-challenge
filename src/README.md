# Memo

Our suspect is **Matthew Spencer**, son of **Elizabeth Spencer** and **Alfred Spencer**. He was born in **1979** in **Birmingham**. He grew up on **Hemmingwood** street with his parents and his dog **Spiffy**. Growing up, he wanted to become a cool **programmer** but instead he became a **doctor**. What a disappointment.

Anyway, we have reason to believe he hid the next clue in `secret.zip`. Unfortunately, the file is encrypted and we do not know the password.

We know the password is some permutation of the following characters:
['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

I created password-protected test zip file with `zip -e test.zip test.txt` and created a proof of concept to decrypt it. See `decryptzip.py`.

Building on that, I tried cracking `secret.zip` via brute force (see `bruteforcezip.py`). This did not end up working. It seems that the password is more than 6 characters long so brute force won't be an option here. We are hoping that you can use your superior hacking skills to help us uncover the contents of `secret.zip`.
