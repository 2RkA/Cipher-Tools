"""
Vigenere Cipher
by: Wesley Jiang & Gerard Gandionco
12/30/2020
"""


def vigenere_cipher(choose, key, plaintext):
    # Used for indexing into alphabet.
    lookup = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13,
        "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
            }
    
    alpha_list = "abcdefghijklmnopqrstuvwxyz"
    key_indices = []  # VINEGAR -> [21, 8, 13, 4, 6, 0, 17]
    message = []
    enumerated_list = [(index, value) for index, value in enumerate(alpha_list)]
    replacement = None

    for letter in key:  # Find the indices of the key word
        for i in enumerated_list:
            if i[1] == letter.lower():
                key_indices.append(i[0])
    
    if choose is True:  # Encrypt or decrypt?
        replacement = key_indices
    else:
        replacement = [ -1 * i for i in key_indices]

    key_index = 0
    i = 0
    while i < len(plaintext):
        if plaintext[i].lower() not in alpha_list:  # If the character is not in alphabet
            message.append(plaintext[i])
        else:
            proper_shift = alpha_list[lookup[plaintext[i].upper()]:] + alpha_list[:lookup[plaintext[i].upper()]] #properly shifts cipher to correct index
            message.append(proper_shift[replacement[key_index]])
            key_index = (key_index + 1) % len(key_indices)
        i += 1

    return ''.join(message)  # Returns encrypted/decrypted message

if __name__ == "__main__":
    """
    Sample:
    - Decrypt:
    - Key: vinegar
    - Message: hmeve cymqfxsaj
    - Output: ???
    """
    print("Welcome to the Vigenere Cipher!")
    print("You will need: a key (a word) and a message")

    while True:
        print("Enter 'e' to encrypt and 'd' to decrypt")
        choose = input("> ")
        if choose == 'e' or choose == 'd':
            break
        else:
            print("\nInvalid input")

    while True:
        print("\nEnter key:")
        key = input("> ")

        print("\nEnter message:")
        message = input("> ")

        break

    print()
    # Encrypt.
    if choose == 'e':
        cipher = vigenere_cipher(True, key, message)
        print(f"\nPlaintext: {message}\nCiphertext: {cipher}")
    # Decrypt.
    elif choose == 'd':
        cipher = vigenere_cipher(False, key, message)
        print(f"\nCiphertext: {message}\nOriginal/Decrypted text: {cipher}")
