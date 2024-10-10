import random

# Leet encryption mapping
leet_mapping = {
    'a': '4',
    'b': '8',
    'e': '3',
    'g': '6',
    'i': '1',
    'l': '1',
    'o': '0',
    's': '5',
    't': '7',
    'z': '2',
}


def generate_leet():
    with open("leetgen/leet.txt", "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()


if __name__ == "__main__":
    # Function to encrypt a word using Leet mapping
    def leet_encrypt(word):
        encrypted_word = ''
        for char in word:
            if char.isalpha():
                encrypted_word += leet_mapping.get(char.lower(), char)
            else:
                encrypted_word += char

        return encrypted_word


    # Read from source file, encrypt words, and write to destination file
    with open('input.txt', 'r') as src, open('leet.txt', 'w') as dst:
        for line in src:
            words = line.strip().split()
            encrypted_line = ' '.join(word.capitalize() if i == 0 else word for i, word in
                                      enumerate(leet_encrypt(word) for word in words)) + '\n'
            dst.write(encrypted_line)
