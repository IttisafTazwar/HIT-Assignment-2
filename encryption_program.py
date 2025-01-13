# Function to encrypt the text
def encrypt_text(raw_text, n, m):
    encrypted_text = ""

    for char in raw_text:
        if char.islower():  # For lowercase letters
            if char <= 'm':  # First half of the alphabet (a-m)
                encrypted_text += chr(((ord(char) - ord('a') + n * m) % 26) + ord('a'))
            else:  # Second half of the alphabet (n-z)
                encrypted_text += chr(((ord(char) - ord('a') - (n + m)) % 26) + ord('a'))
        elif char.isupper():  # For uppercase letters
            if char <= 'M':  # First half of the alphabet (A-M)
                encrypted_text += chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
            else:  # Second half of the alphabet (N-Z)
                encrypted_text += chr(((ord(char) - ord('A') + m ** 2) % 26) + ord('A'))
        else:  # For special characters and spaces, keep them unchanged
            encrypted_text += char

    return encrypted_text


# Function to decrypt the text
def decrypt_text(encrypted_text, n, m):
    decrypted_text = ""

    for char in encrypted_text:
        if char.islower():  # For lowercase letters
            if char <= 'm':  # First half of the alphabet (a-m)
                decrypted_text += chr(((ord(char) - ord('a') - n * m) % 26) + ord('a'))
            else:  # Second half of the alphabet (n-z)
                decrypted_text += chr(((ord(char) - ord('a') + (n + m)) % 26) + ord('a'))
        elif char.isupper():  # For uppercase letters
            if char <= 'M':  # First half of the alphabet (A-M)
                decrypted_text += chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
            else:  # Second half of the alphabet (N-Z)
                decrypted_text += chr(((ord(char) - ord('A') - m ** 2) % 26) + ord('A'))
        else:  # For special characters and spaces, keep them unchanged
            decrypted_text += char

    return decrypted_text


# Function to check the correctness of the decrypted text
def check_decryption(raw_text, decrypted_text):
    return raw_text == decrypted_text


# Read raw text from a file
def read_raw_text(filename):
    with open(filename, 'r') as file:
        return file.read()


# Write encrypted text to a new file
def write_encrypted_text(filename, encrypted_text):
    with open(filename, 'w') as file:
        file.write(encrypted_text)


# Main function to execute the program
def main():
    # Get inputs for n and m
    n = int(input("Enter the value of n: "))
    m = int(input("Enter the value of m: "))

    # Read the raw text from file
    raw_text = read_raw_text('raw_text.txt')

    # Encrypt the raw text
    encrypted_text = encrypt_text(raw_text, n, m)

    # Write the encrypted text to file
    write_encrypted_text('encrypted_text.txt', encrypted_text)

    # Print the encrypted text
    print("Encrypted Text:")
    print(encrypted_text)

    # Decrypt the text
    decrypted_text = decrypt_text(encrypted_text, n, m)

    # Check if the decrypted text matches the original raw text
    if check_decryption(raw_text, decrypted_text):
        print("Decryption is successful. The text is correct.")
    else:
        print("Decryption failed. The text is incorrect.")


if __name__ == "__main__":
    main()

