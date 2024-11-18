from registFunc import register_user

# Valid user input
name = "Alice"
email = "alice@example.com"
password = "Password123"

try:
    user = register_user(name, email, password)
    if user:
        print("User successfully registered:", user)
except ValueError as e:
    print("Error:", e)