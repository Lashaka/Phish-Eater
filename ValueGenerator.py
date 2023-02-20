# Global Classes
import random
import string

# Project Classes
import RandomValuesLists

def generate_email(length):
    """Generate a random email address with the specified length."""
    username = random.choice(RandomValuesLists.Usernames)
    ending = random.choice(['gmail.com', 'outlook.com', 'yahoo.com','icloud.com', 'aol.com', 'qq.com','naver.com', 'daum.net', 'yandex.com'])
    return f"{username}@{ending}"

def generate_phone():
    """Generate a random phone number in the format XXX-XXX-XXXX."""
    area_code = ''.join(random.choice(string.digits) for _ in range(3))
    first_three = ''.join(random.choice(string.digits) for _ in range(3))
    last_four = ''.join(random.choice(string.digits) for _ in range(4))
    return f"{area_code}{first_three}{last_four}"
