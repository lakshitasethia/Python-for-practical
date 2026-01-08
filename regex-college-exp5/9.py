# Expected  Output:  ['http://example.com',  'https://secure-site.org','ftp://files.example.net']
import re

def url(text):
    pattern = r'https?://[^\s,]+|ftp://[^\s,]+'
    matches = re.findall(pattern, text)
    return matches

text = "Visit our sites at http://example.com, https://secure-site.org, and ftp://files.example.net."

result = url(text)
print(result)