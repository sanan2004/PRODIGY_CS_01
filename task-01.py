# Caesar Cipher implementation in Python

def encrypt(text, shift):
    result = ""
    
    # Traverse the text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep other characters unchanged (spaces, punctuation)
        else:
            result += char
    return result

def decrypt(text, shift):
    # Decryption is simply encryption with the inverse shift
    return encrypt(text, -shift)

def main():
    while True:
        # User input
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (Q to quit): ").upper()
        
        if choice == 'Q':
            print("Goodbye!")
            break

        if choice not in ['E', 'D']:
            print("Invalid choice! Please enter 'E' to encrypt or 'D' to decrypt.")
            continue
        
        message = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value (a number): "))
        except ValueError:
            print("Please enter a valid integer for the shift value.")
            continue
        
        if choice == 'E':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == 'D':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")

# Run the program
if __name__ == "__main__":
    main()
