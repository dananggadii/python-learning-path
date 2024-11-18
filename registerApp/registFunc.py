# List of approved top-level domains for email validation
top_level_domains = [".com", ".org", ".net", ".edu"]

def validate_name(name):
    """
    Validate a user's name.

    Args:
        name (str): The name to validate.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    return len(name) > 2 and name.isalpha()


def validate_email(email):
    """
    Validate a user's email address.

    Args:
        email (str): The email to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    import re
    # Regular expression to validate email
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_regex, email):
        # Check for approved top-level domains
        for domain in top_level_domains:
            if email.endswith(domain):
                return True
    return False


def validate_password(password):
    """
    Validate a user's password.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    import re
    # Check if password is at least 8 characters, contains an uppercase letter, and a number
    if len(password) >= 8 and re.search(r"[A-Z]", password) and re.search(r"\d", password):
        return True
    return False

def validate_user(name, email, password):
    """
    Validate the user name, email, and password.

    Args:
        name (str): Name to validate.
        email (str): Email address to validate.
        password (str): Password to validate.

    Returns:
        bool: True if all validations pass, raises ValueError if any validation fails.
    """
    if not validate_name(name):
        raise ValueError("Please make sure your name is greater than 2 characters!")
    
    if not validate_email(email):
        raise ValueError("Your email address is in the incorrect format, please enter a valid email.")
    
    if not validate_password(password):
        raise ValueError(
            "Your password is too weak. Ensure it is at least 8 characters, "
            "contains a capital letter, and a number."
        )
    
    return True


def register_user(name, email, password):
    """
    Register a user if they pass validation.

    Args:
        name (str): Name of the user.
        email (str): Email address of the user.
        password (str): Password of the user.

    Returns:
        dict: A dictionary containing the user's details if successful.

    Raises:
        ValueError: If validation fails or arguments are invalid.
    """
    if validate_user(name, email, password):
        user = {
            "name": name,
            "email": email,
            "password": password  # In real-world applications, passwords should be hashed!
        }
        return user
    return False