import random
import string


# 随机中文名字
def generate_chinese_name(filename='./data/chinese_names.txt'):
    with open(filename, "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()


# 随机QQ名字
def generate_qq_name(filename='./data/qq_names.txt'):
    with open(filename, "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()


# 随机英文名字
def read_random_line_from_file(filename, excluded_first_letter=None):
    """从文件随机读取并返回一行，可以排除开头字母与指定字母相同的行"""
    with open(filename, 'r') as file:
        lines = file.readlines()
        if len(lines) > 0:
            valid_lines = [line for line in lines if line[0].strip() != excluded_first_letter]
            if valid_lines:
                return random.choice(valid_lines).strip()
            else:
                return ""
        else:
            return ""


def generate_english_name(first_names_file='./data/first_names.txt', middle_names_file='./data/middle_names.txt'):
    """从两个文件分别随机读取一个名字并拼接生成一个名字"""
    first_name = read_random_line_from_file(first_names_file)
    middle_name = read_random_line_from_file(middle_names_file, excluded_first_letter=first_name[0].lower())
    if first_name and middle_name:
        return f"{first_name} {middle_name}"
    else:
        return ""


# 随机日本名字
def generate_japanese_name(filename='./data/japanese_names.txt'):
    with open(filename, "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()


# 随机英文地址位置
def generate_english_place(filename='./data/english_places.txt'):
    with open(filename, "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()


if __name__ == "__main__":
    print(generate_chinese_name('../data/chinese_names.txt'))
    print(generate_qq_name('../data/qq_names.txt'))
    print(generate_japanese_name('../data/japanese_names.txt'))
    print(generate_english_name('../data/first_names.txt', '../data/middle_names.txt'))
    print(generate_english_place('../data/english_places.txt'))
