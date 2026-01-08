import re
text = "The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. The previous quarter i.e. fy2020 Q4 it was $3 billion."

# pattern = ''
pattern = 'FY(\d{4} Q[1-4])[^\$]+\$([0-9\.]+)'

matches = re.findall(pattern,text,flags=re.IGNORECASE)
print(matches)
