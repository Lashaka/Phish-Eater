# Global Classes
import random

# Project Classes
import RandomValuesLists
import ValueGenerator
 
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

# ADD THAT IF ITS A SINGLE NUMBER +0 FROM BEFORE IT??? ^

# Print the generated credit card information
print(f"Email address:", ValueGenerator.generate_email(10))
print(f"Phone number:", ValueGenerator.generate_phone())
print(f'Credit Card Number: {credit_card_number}')
print(f'Cardholder Name: {cardholder_name}')
print(f'Expiration Date: {expiration_date}')
print(f'Security Code: {security_code}')

# Random address
from faker import Faker

fake = Faker()

street_address = fake.street_address()
street_address_line_2 = fake.secondary_address()
city = fake.city()
country = fake.country()
zip_code = fake.zipcode()
region = fake.state()

print("Street Address:", street_address)
print("Street Address Line 2:", street_address_line_2)
print("City:", city)
print("Country:", country)
print("Zip Code:", zip_code)
print("Region:", region)

# Fake company name

company_name = fake.company()

print("Company Name:", company_name)
