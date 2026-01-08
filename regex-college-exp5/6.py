# Expected Output: [1234.56, 789.00]
import re

def price(text):
    pattern=r'\$[\d,]+\.?\d+'
    matches = re.findall(pattern,text)

    result=[]
    for match in matches:
        result.append((match.replace('$','').replace(',','')))
    print(result)

price("The price is $1,234.56 and $789.00 for the additional items.")
