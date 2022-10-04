import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            normas = ord(letter) + shift
            if normas > ord('z') or ord('a') > normas > ord('Z'):
                normas -= 26
            word_ = chr(normas)
            ciphertext += word_
        else:
            ciphertext += letter
            print(ciphertext)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            normas = ord(letter) - shift
            if normas < ord('A') or ord('a') > normas > ord('Z'):
                normas += 26
            word_ = chr(normas)
            plaintext += word_
        else:
            plaintext += letter
            print(plaintext)
    return plaintext



def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:

    best_shift = 0

    return best_shift
