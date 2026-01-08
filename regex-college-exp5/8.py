# Expected Output: ['978-3-16-148410-0', '978-0-306-40615-7']
import re

def isbn(text):
    pattern = r'\d{3}-\d{1}-\d{2}-\d{6}-\d{1}|\d{3}-\d{1}-\d{3}-\d{5}-\d{1}'
    matches = re.findall(pattern, text)
    print(matches)

isbn("The books have ISBN numbers like 978-3-16-148410-0 and 978-0-306-40615-7")
