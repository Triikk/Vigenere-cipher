ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]


def get_index(letter: str) -> int:
    """
    :param letter: the letter (case insensitive)
    :return: the position of the letter in the alphabet
    """
    return ALPHABET.index(letter.upper(), 0, len(ALPHABET))


def adapt_key(key: str, text: str) -> str:
    """
    :param text: the text (with no empty spaces) you want to encrypt
    :param key: the key
    :return: a repetition of the key as long as the text
    """
    key = key.upper()
    if len(key) >= len(text):
        return key[:len(text)]

    length = len(key)
    for i in range(len(key), len(text)):
        key += key[i % length]
    return key


def adapt_text(text: str) -> str:
    """
    Adapt the text by removing empty spaces and using upper cases
    :param text:
    :return:
    """
    return text.upper().replace(" ", "")


def encrypt(text: str, key: str) -> str:
    """
    Encrypt the message
    :param text: the text
    :param key: the key
    :return: the encrypted text
    """
    assert len(text) == len(key), "The text and the key must have the same length"
    encrypted_text = ""

    for i in range(len(text)):
        text_index = get_index(text[i])
        key_index = get_index(key[i])
        encrypted_text += ALPHABET[(text_index + key_index) % len(ALPHABET)]

    return encrypted_text


def decrypt(text: str, key: str):
    """
    Decrypt a given text with a key
    :param text: the text you want to decrypt
    :param key: the key
    :return: the decrypted text
    """
    assert len(text) == len(key), "The text and the key must have the same length"
    decrypted_text = ""

    for i in range(len(text)):
        text_index = get_index(text[i])
        key_index = get_index(key[i])
        decrypted_text += ALPHABET[(text_index - key_index) % len(ALPHABET)]

    return decrypted_text


def main():
    while True:
        try:
            choice = int(input("Welcome to a Vigènere calculator! \nType \"1\" if you want do encrypt a message \nType "
                               "\"2\" if you want to decrypt a  \n\n> "))

            if choice == 1 or choice == 2:
                break
        except ValueError:
            continue

    key = input("Type the key:\n> ")
    text = input("Type the text:\n> ")
    text = adapt_text(text)
    key = adapt_key(key, text)
    print("Your initial message: " + text)

    if choice == 1:
        encrypted_text = encrypt(text, key)
        print("Your encrypted message: " + encrypted_text)
    else:
        decrypted_text = decrypt(text, key)
        print("Your decrypted message: " + decrypted_text)
        
    exit(0)


if __name__ == "__main__":
    main()
