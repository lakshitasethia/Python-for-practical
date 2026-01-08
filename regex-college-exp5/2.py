# Expected Output: {'Barack Obama': 1, 'Hawaii': 1, 'Google': 1}
import re
from collections import Counter

def count_named_entities(text):
    # Match consecutive capitalized words
    pattern = r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b'
    matches = re.findall(pattern, text)
    return dict(Counter(matches))

# Test
text = "Barack Obama was born in Hawaii.Google is a major techcompany."
print(count_named_entities(text))