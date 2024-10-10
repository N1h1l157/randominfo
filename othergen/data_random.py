from datetime import datetime, timedelta
import random
import string


def generate_random_email():
    # 随机选择一个名字和一个域名
    name_pre_length = random.randint(2, 10)
    name_suf_length = random.randint(2, 10)
    name_pre = ''.join(random.choice(string.ascii_lowercase) for _ in range(name_pre_length))
    name_suf = ''.join(random.choice(string.digits) for _ in range(name_suf_length))
    name = name_pre + name_suf
    domain = random.choice(['gmail.com', 'hotmail.com', 'yahoo.com', 'qq.com', '163.com', 'outlook.com', 'icloud.com', 'sina.com', 'foxmail.com'])

    # 生成邮箱地址
    email = f"{name}@{domain}"

    return email


def generate_random_phone(length=10):
    # 创建一个包含数字的字符串
    digits = string.digits

    # 随机选择 `length` 个数字
    phone_number = ''.join(random.choice(digits) for _ in range(length))

    return '1' + phone_number


def generate_random_birth():
    start_year = 1950
    end_year = 2025

    # 计算天数
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    days = (end_date - start_date).days

    # 随机选择一个天数
    random_day = random.randint(0, days)

    # 添加到开始日期上
    random_date = start_date + timedelta(days=random_day)

    return random_date.strftime("%Y-%m-%d")


if __name__ == "__main__":
    email = generate_random_email()
    print(f"随机生成的邮箱是：{email}")

    phone_number = generate_random_phone(10)
    print(f"随机生成的手机号是：{phone_number}")

    random_day = generate_random_birth()
    print(f"随机生成的日期是：{random_day}")
