"""
Outputs all 26 cipher cases.
"""

from caesar_cipher import cipher


def gen_ciphertext(message: str) -> str:
    """
    Yields key and respective ciphertext 26 times
    """
    key = 1
    for i in range(26):
        ciphertext = cipher(key, message)
        yield f"Key #{key}: {ciphertext}"
        key += 1


if __name__ == "__main__":
    print("Enter 'quit' to exit anytime")
    while True:
        print("Enter message:")
        message = input("> ")
        if message.lower().strip() == 'quit':
            break
    
        print()
        # Prints each ciphertext for each generator iteration
        for statement in gen_ciphertext(message):
            print(statement)
        print()
