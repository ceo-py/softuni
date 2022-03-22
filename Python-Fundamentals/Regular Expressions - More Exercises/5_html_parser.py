import re

pattern_title = r"(?:<title>)(?P<title>.+)(?:</title>)"
pattern_body = r"(?:<body>)(?P<body>.+)(?:</body>)"
pattern_remove_tags = r"<[^>]*>"
pattern_remove_pseudo_space = r"\\n|\\t"            # "new lines" and "tabs"
pattern_remove_spaces = r"[ ]+"

text = input()

title = re.search(pattern_title, text).group("title")
body = re.search(pattern_body, text).group("body")

title = re.sub(pattern_remove_tags, "", title, re.IGNORECASE | re.UNICODE)
body = re.sub(pattern_remove_tags, "", body, re.IGNORECASE | re.UNICODE)

title = re.sub(pattern_remove_pseudo_space, "", title).strip()
body = re.sub(pattern_remove_pseudo_space, "", body).strip()

title = re.sub(pattern_remove_spaces, " ", title).strip()
body = re.sub(pattern_remove_spaces, " ", body).strip()

print(f"Title: {title}")
print(f"Content: {body}")