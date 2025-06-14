import re

def is_valid_email(email):
    if not email or not isinstance(email, str):
        return False
    
    pattern = r"""
        ^                       # Start of string
        [a-zA-Z0-9_.+-]+        # Local part (username)
        @                       # @ symbol
        [a-zA-Z0-9-]+           # Domain name
        \.                      # Dot
        [a-zA-Z0-9-.]+          # Top-level domain
        $                       # End of string
    """
    
    if not re.match(pattern, email, re.VERBOSE):
        return False
    
    if email.count('@') != 1:
        return False
    
    local_part, domain_part = email.split('@')
    
    if not local_part or len(local_part) > 64:
        return False
    
    if not domain_part or len(domain_part) > 255:
        return False
    
    if '..' in local_part or '..' in domain_part:
        return False
    
    if domain_part.count('.') < 1:
        return False
    
    tld = domain_part.split('.')[-1]
    if len(tld) < 2:  
        return False
    
    return True

test_emails = [
    ("user@example.com", True),
    ("firstname.lastname@domain.co", True),
    ("user+tag@domain.org", True),
    ("user@sub.domain.com", True),
    ("user@123.123.123.123", False),  
    ("user@domain..com", False),
    ("user@.com", False),
    ("@domain.com", False),
    ("user@domain", False),
    ("user@domain.c", False),  
    ("user@domain.com.", False),
    ("", False),
    (None, False)
]

for email, expected in test_emails:
    result = is_valid_email(email)
    print(f"'{email}': {'Valid' if result == expected else 'INVALID'} (Expected: {'Valid' if expected else 'Invalid'})")


    # Example usage
email = input("Enter an email address: ")
if is_valid_email(email):
    print(f"'{email}' is a valid email address")
else:
    print(f"'{email}' is NOT a valid email address")