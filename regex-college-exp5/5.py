# Expected Output: ['(123) 456-7890', '(987) 654-3210']
import re

def phone(text):  
    matches = re.findall(r'(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})', text)
    result = [f"({first}) {second}-{third}" for first, second, third in matches]
    print(result)
phone("Contact me at 1234567890 or 987-654-3210.")