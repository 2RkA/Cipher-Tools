# About
Collab by: Wesley & Gerard
Play around with encryption and decryption with these handy little ciphers!
Requires an environment that accepts user input.

To know:
- cipher: algorithm used to encrypt or decrypt information
- plaintext: your original, untouched message to be encrypted
- ciphertext: your outputted encrypted message
- key: piece of information used to turn plaintext into ciphertext via an algorithm, vice versa with decryption

What we have:
- Caesar Cipher
- Vigenère Cipher

Possible upcoming:
- Affine Cipher
- The Enigma Machine

# Caesar Cipher
Definition: A simple cipher in which each letter in the word is shifted a certain, fixed amount down the alphabet with how many times being determined by the key (an integer).
EX// If the key was 5, then each letter in "attackatdawn" would shift forward 5 times, resulting in "fyyfhpfyifbs."
Non-alphabetical characters (numbers and special characters) are unaffected. Can be used to both encrypt or decrypt.

# Vigenère Cipher
Definition: a cipher that uses interwoven caesar shifts, where each letter in the word is shifted a certain amount based on each letter of the key's numerical place in the alphabet, which repeats until it matches the length of the original message, if needed.
EX// The key is VINEGAR and our message to be encrypted is ATTACKATDAWN. Take the alphabetical place number for each letter in the key: V, I, N, E, G, A, R = 21, 8, 13, 4, 6, 0, 17. Then, repeat that until it matches the length of ATTACKATDAWN, so it would be VINEGARVINEG. Finally, ceasar shift each letter of the message by the now matched number values of VINEGARVINEG into ATTACKATDAWN (21, 8, 13, 4, 6, 0, 17, 21, 8, 13, 4, 6), which yields VBGEIKROLNAT.
Only takes alphabetical characters (for now). Can be used to both encrypt or decrypt.
