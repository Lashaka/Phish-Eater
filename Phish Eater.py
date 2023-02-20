import random
import string

import RandomValuesLists

# Generate a random 16-digit credit card number
credit_card_number = ''.join(str(random.randint(0, 9)) for _ in range(16))

# Generate a random cardholder name
first_name = random.choice(RandomValuesLists.FirstNamesArray)
last_name = random.choice(RandomValuesLists.LastNamesArray)
cardholder_name = f'{first_name.capitalize()} {last_name.capitalize()}'

# Generate a random expiration date
expiration_month = random.randint(1, 12)
expiration_year = random.randint(2022, 2030)
expiration_date = f'{expiration_month}/{expiration_year}'

# Generate a random security code (3 or 4 digits)
security_code = ''.join(str(random.randint(0, 9)) for _ in range(3))

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
    return f"{area_code}-{first_three}-{last_four}"

# Example usage:
print("Random email address:", generate_email(10))
print("Random phone number:", generate_phone())

# Print the generated credit card information
print(f'Credit Card Number: {credit_card_number}')
print(f'Cardholder Name: {cardholder_name}')
print(f'Expiration Date: {expiration_date}')
print(f'Security Code: {security_code}')
