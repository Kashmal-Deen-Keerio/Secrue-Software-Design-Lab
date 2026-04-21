import random

DB_PASSWORD = "123456"   # Hardcoded password (BAD)

def get_user(name):
    query = "SELECT * FROM users WHERE name = '" + name + "'"   # SQL Injection
    print(query)

def generate_otp():
    return random.randint(100000, 999999)   # Not secure

unused_count = 0   # Unused variable
