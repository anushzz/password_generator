import random
import string

def gen_pwd(length, use_upper=True, use_dig=True, use_spec=True):

    l = string.ascii_lowercase
    u = string.ascii_uppercase if use_upper else ''
    d = string.digits if use_dig else ''
    spec = '!@#$%^&*' if use_spec else ''
    all_chars = l + u + d + spec

    password = ''.join(random.choice(all_chars) for i in range(length))

    return password

use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_dig = input("Include digits? (y/n): ").lower() == 'y'
use_spec = input("Include special characters? (y/n): ").lower() == 'y'

password = gen_pwd(8, use_upper, use_dig, use_spec)
print("Generated Password:", password)