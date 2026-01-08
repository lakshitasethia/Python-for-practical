# Input:"Check out #DataScience and @JohnDoe's post at http://example.com! #AI" Expected Output: {'hashtags': ['#DataScience', '#AI'], 'mentions':['@JohnDoe'], 'urls': ['http://example.com']}
import re


def mixture(text):

    hashtags = re.findall(r"#\w+", text)
    mentions = re.findall(r"@\w+", text)
    urls = re.findall(r"http:\/\/\w+\.\w+", text)
    return {"hashtags": hashtags, "mentions": mentions, "urls": urls}

print(mixture("Check out #DataScience and @JohnDoe's post at http://example.com! #AI"))
