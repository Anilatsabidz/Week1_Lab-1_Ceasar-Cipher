def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    return decrypted_text


def brute_force_caesar(ciphertext):
    print("Trying all possible shifts:")
    for shift in range(1, 26):
        decrypted = caesar_cipher_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted}")


# Input Ciphertext
ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
brute_force_caesar(ciphertext)
