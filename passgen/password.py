import random
import string


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def save_strings_to_file(file_path, num_strings):
    with open(file_path, 'w') as file:
        for _ in range(num_strings):
            random_string = generate_random_string()
            file.write(f'{random_string}\n')


def generate_password_1(length=10):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def generate_password_2(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    file_path = "pass.txt"
    num_strings = 10000
    save_strings_to_file(file_path, num_strings)
