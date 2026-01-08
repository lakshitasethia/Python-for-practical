# 11.	Define a function to extract and sort all numerical values from a text, including handling numbers embedded in words or mixed with text.
# Input: "The quantities are 12 apples, 2 oranges, and 25 bananas."
# Expected Output: [2, 12, 25]
import re
def sort(text):
    pattern=r'\d+'
    matches=list(re.findall(pattern,text))
    result=[]
    for match in matches:
        result.append((int(match)))
    print(sorted(result))
sort("The quantities are 12 apples, 2 oranges, and 25 bananas.")