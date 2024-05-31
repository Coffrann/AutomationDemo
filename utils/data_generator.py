import random
from datetime import datetime


# Generate a random first name
def generate_name():
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie"]
    return random.choice(first_names)


# Generate a random last name
def generate_lastname():
    last_names = ["Smith", "Doe", "Brown", "Johnson", "Taylor", "Lee"]
    return random.choice(last_names)


# Generate a random phone number
def generate_phone_number():
    # Format: (XXX) XXX-XXXX
    area_code = random.randint(100, 999)
    central_office_code = random.randint(100, 999)
    station_code = random.randint(1000, 9999)
    return f"({area_code}) {central_office_code}-{station_code}"


# Generate a current timestamp
def generate_timestamp():
    # Current date and time
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
