alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    global alphabet

    ciphertext = ""

    keylengnt = len(keyword)
    keyword = keyword.upper()

    for ind, symb in enumerate(plaintext):
        num = alphabet.find(symb.upper())
        if num != -1:
            num += alphabet.find(keyword[ind % keylengnt])
            if symb.isupper():
                ciphertext += alphabet[num % 26]
            else:
                ciphertext += alphabet[num % 26].lower()
        else:
            ciphertext += symb
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    global alphabet
    plaintext = ""

    keylengnt = len(keyword)
    keyword = keyword.upper()

    for ind, symb in enumerate(ciphertext):

        num = alphabet.find(symb.upper())
        if num != -1:
            num -= alphabet.find(keyword[ind % keylengnt])

            if symb.isupper():
                plaintext += alphabet[num]

            else:
                plaintext += alphabet[num].lower()

        else:
            plaintext += symb
    return plaintext


