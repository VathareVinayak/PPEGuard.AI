import bcrypt

def hash_password(plain_password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(plain_password.encode(), salt)
    return hashed_password.decode()  # Convert bytes to string

# Example Usage
plain_text_password = "vinayak@123"
hashed_password = hash_password(plain_text_password)
print("Hashed Password:", hashed_password)
