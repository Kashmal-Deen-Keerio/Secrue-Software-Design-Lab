import os
import secrets

# Fix 1: Environment variable for password
DB_PASSWORD = os.environ.get('DB_PASSWORD')

# Fix 2: Secure query
def get_user(cursor, name):
    query = "SELECT * FROM users WHERE name = %s"
    cursor.execute(query, (name,))
    return cursor.fetchall()

# Fix 3: Secure OTP
def generate_otp():
    return secrets.randbelow(900000) + 100000

# Fix 4: Removed unused variable
