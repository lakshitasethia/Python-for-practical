# Expected Output: {'name': 'John Doe', 'age': '30', 'profession':'Data Scientist'}
import re

def regex_dict(text):
    pattern = r"(\w+):\s*([^;]+)"
    matches = dict(re.findall(pattern, text))
    print(matches)

regex_dict("name: John Doe; age: 30; profession: Data Scientist")
