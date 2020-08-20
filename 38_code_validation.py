"""
ATM PIN Code Validation
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.

Examples
is_valid_PIN("1234") ➞ True

is_valid_PIN("12345") ➞ False

is_valid_PIN("a234") ➞ False

is_valid_PIN("") ➞ False
Notes
Some test cases contain special characters.
Empty strings must return False.
"""

def is_valid_PIN(pin):
    ln = len(list(pin))
    
    a = "123456789"
    
    if not ln:
        return False
    
    if ln == 4 or ln == 6:
        for i in list(pin):
            if not i in a:
                return False
            return True
        
    return False
    
is_valid_PIN("")