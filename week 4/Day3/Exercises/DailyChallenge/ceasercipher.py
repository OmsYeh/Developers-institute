def caesar_cipher(user_text, step):
    encrypted_text = []
    crypt_text = []

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

    for each_letter in user_text:
        if each_letter in uppercase:
            index = uppercase.index(each_letter)
            cryption = (index + step) % 26
            crypt_text.append(cryption)
            new_letter = uppercase[cryption]
            encrypted_text.append(new_letter)
        elif each_letter in lowercase:
            index = lowercase.index(each_letter)
            cryption = (index + step) % 26
            crypt_text.append(cryption)
            new_letter = lowercase[cryption]
            encrypted_text.append(new_letter)
    return encrypted_text


code = caesar_cipher('Hello', 2)
print()
print(code)
print()
