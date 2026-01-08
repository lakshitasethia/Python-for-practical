import re
def email(text):
  pattern=r'@\w+\.\w+'
  matches=re.findall(pattern,text)
  print(matches)
  
email('Please contact us at support@example.com or sales@otherdomain.com')