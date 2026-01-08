# Expected Output: ['data', 'hello', 'of', 'science', 'the', 'to','welcome', 'world']
import re
def unique(text):
# text="Hello world! Welcome to the world of Data Science." 
  finaltext=text.lower()
  pattern=r'\w+'

  matches=set(re.findall(pattern,finaltext,flags=re.IGNORECASE))
  newMatches=sorted(matches)
  print(newMatches)

unique("Hello world! Welcome to the world of Data Science.")