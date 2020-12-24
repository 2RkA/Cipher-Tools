"""
Caesar Cipher
by Wesley Jiang and Gerard Gandionco
12/22/2020
"""

def cipher(key: int, message: str) -> str:
    """
    Returns a coded message
    - also able to decode messages with negative key
    - going above 26 will wrap it back to 1 
    """

    alpha_list = "abcdefghijklmnopqrstuvwxyz"
    alpha_list2 = alpha_list

    new_list = alpha_list2[key%26:] + alpha_list2[:key%26]  # Shifts cipher key amount

    new_message = []
    
    for char in message:
        if not char.isalpha():  # If the char is a anything but an alphabetical letter
            new_message.append(char)
        for i in range(len(alpha_list)):  # Matches cipher to corresponding letter
            if alpha_list[i] == char:
                new_message.append(new_list[i])

    new_new_message = "".join(new_message)  # Turns list into single string
    return new_new_message

if __name__ == "__main__":

    # Takes user input for key (an int) and a message (a str)
    print("Enter 'quit' to exit out anytime")
    while True:
        try:
            print("Enter your key")
            key1 = input("> ")
            if key1.lower().strip() == "quit":
                break
            key2 = int(key1)

            print("Enter your message")
            plaintext = input("> ")
            if plaintext.lower().strip() == 'quit':
                break

        except ValueError:
            print("Please enter an integer\n")
        else:
            # Calls cipher function and returns new encrypted message
            new_message = cipher(key2, plaintext)
            print(f"\nYour new message is: {new_message}\n")
