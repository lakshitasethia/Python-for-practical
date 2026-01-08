# Expected Output:
# "Hello World! This is a link."
import re

def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text).strip()    
    return text


input_text = "Hello <b>World</b>! This is a <a href='http://example.com'>link</a>."
output = clean_text(input_text)
print(output)