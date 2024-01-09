import re

phone_number = "The phone number is 123-456-7890"
match = re.search(r'(\d+)-\d+-\d+', phone_number)
if match:
    area_code = match.group(0)
    print(area_code)

phone_number = "The phone number is 123-456-7890"
match = re.search(r'(\d+)-\d+-\d+', phone_number)
if match:
    area_code = match.group(1)
    print(area_code)

phone_number = "The phone number is 123-456-7890"
match = re.search(r'(\d+)-(\d+)-\d+', phone_number)
if match:
    middle_digits = match.group(2)
    print(middle_digits)

phone_number = "The phone number is 123-456-7890"
match = re.search(r'(\d+)-(\d+)-(\d+)+', phone_number)
if match:
    middle_digits = match.group(3)
    print(middle_digits)
