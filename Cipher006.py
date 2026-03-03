alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet + ' ' + alphabet.upper()

def vigenere_header():
    print(' | ', end= " | ")
    for c in alphabet:
        print(c.upper(), end= " | ")
    print()
    print(f'{"|---"*(len(alphabet) + 1)}')

def vigenere_body():
    for i in range(len(alphabet)):
        j = i
        print('| ' + alphabet[j].upper(), end = ' | ')
        for _ in range(len(alphabet)):
            j = j % len(alphabet)
            print(alphabet[j], end=' | ')
            j += 1
        print()

def vigenere_sq():
    vigenere_header()
    vigenere_body()


#vigenere_sq()

def letter_to_index(letter:str, alphabet:str) -> int:
    if letter not in alphabet:
        raise "ERROR"
    for i, c in enumerate(alphabet):
        if c == letter:
            return i
    return -1

def index_to_letter(index, alphabet):
    if not (0 <= index < len(alphabet)):
        raise 'index out of bounds'
    return alphabet[index]

KEY = 'DAVINCI'

def vinegere_index(key_letter:str, plaintext_letter:str, alphabet:str) -> str:
    cipher_index = (letter_to_index(plaintext_letter, alphabet) + letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(cipher_index, alphabet)

def encrypt_vinegere(key, plaintext, alphabet):
    cipher_text = ''
    for i, c in enumerate(plaintext):
        cipher_text += vinegere_index(key[i%len(key)], c, alphabet)
    return cipher_text



print(encrypt_vinegere(KEY, 'the king is a dragon', alphabet))





"""
for i, r in enumerate(alphabet):
    for c in alphabet:
        print(alphabet[i], end=' ')
    i += 1
    print()
"""