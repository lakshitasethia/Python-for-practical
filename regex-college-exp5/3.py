# Expected Output: ['2024-12-31', '2024-01-15']
import re
def date(text):
    pattern1=r'(\d{2})[/-](\d{2})[/-](\d{4})'
    matches = re.findall(pattern1, text)

    result=[]
    for date,month,year in matches:
        result.append(f"{year}-{month}-{date}")
    return result

print(date("The event is scheduled for 12/31/2024 and the deadline is 01-15-2024."))