### Common Regex

A python package that provides commonly used regular expressions for validating various types of data.

#### Installation

`pip install pycommonregex`

#### Usage

```python
import re
from pycommonregex import *

print(is_int(5)) # True
print(is_positive_int('5')) # True
print(is_decimal_num('5.5')) # True
print(is_num('-5.5')) # True
print(is_alpha_numeric('abc123')) # True
print(is_alpha_numeric_with_space('abc 123')) # True
print(is_email('email@example.com')) # True
print(is_good_password('Abc123#')) # True
print(is_username('abc_123')) # True
print(is_url('https://www.example.com')) # True
print(is_ipv4('127.0.0.1')) # True
print(is_ipv6('::1')) # True

```

#### Functions

- 'is_int(num)': Check if the given input is an integer.
- 'is_positive_int(s)': Check if the given input is a positive integer.
- 'is_decimal_num(s)': Check if the given input is a decimal number.
- 'is_num(s)': Check if the given input is a number (positive or negative).
- 'is_alpha_numeric(s)': Check if the given input is alphanumeric (only contains letters and numbers).
- 'is_alpha_numeric_with_space(s)': Check if the given input is alphanumeric (only contains letters, numbers, and spaces).
- 'is_email(email)': Check if the given input is a valid email address.
- 'is_good_password(password)': Check if the given input is a strong password (contains at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character, and is at least 8 characters long).
- 'is_username(username)': Check if the given input is a valid username (contains only letters, numbers, and certain special characters, and is between 4 and 20 characters long).
- 'is_url(url)': Check if the given input is a valid URL.
- 'is_ipv4(IPv4)': Check if the given input is a valid IPv4 address.
- 'is_ipv6(address)': Check if the given input is a valid IPv6 address.
