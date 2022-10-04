import random
import typing as tp


def is_prime(n: int) -> bool:
    num = 2
    while num ** 2 <= n:
        if n % num == 0:
            return False
        num += 1
    return True if n != 1 else False


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a >=b:
            return gcd(b, a%b)
        else:
            return gcd(a, b%a)


def multiplicative_inverse(e: int, phi: int) -> int:
    a, b = (e, phi) if e > phi else (phi, e)
    x1, x2, y1, y2 = 1, 0, 0, 1
    i = 0
    while b:
        d = a // b
        a, b = b, a % b
        x1, x2 = x2, x1 - x2 * d
        y1, y2 = y2, y1 - y2 * d
        i += 1
    return y1 % max(e, phi) if i > 1 else 0


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")
    n = p * q

    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))




def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
