import re

html_content = input()
pattern = re.compile(r"(?:<title>)(?P<title_html>.+)(?:</title>).*(?:<body>)(?P<body_html>.+)(?:</body>)")
m_space, tabs_n, between = r"[ ]+", r"\\n|\\t", r"<[^>]*>"
result = re.finditer(pattern, html_content)
for show in result:
    print(f'Title: {re.sub(m_space, " ", re.sub(tabs_n, "", re.sub(between, "", show["title_html"])))}')
    print(f'Content: {re.sub(m_space, " ", re.sub(tabs_n, "", re.sub(between, "", show["body_html"])))}')


#
# import re
#
# text = input()
#
# pattern_title = r"(?:<title>)(?P<title>.+)(?:</title>)"
# pattern_body = r"(?:<body>)(?P<body>.+)(?:</body>)"
# title = re.search(pattern_title, text).group("title")
# body = re.search(pattern_body, text).group("body")
# title = re.sub(r"[ ]+", " ", re.sub(r"\\n|\\t", "", re.sub(r"<[^>]*>", "", title)))
# body = re.sub(r"[ ]+", " ", re.sub(r"\\n|\\t", "", re.sub(r"<[^>]*>", "", body)))
# print(f"Title: {title}")
# print(f"Content: {body}")
#
#
#




#
#
#
# import re
#
# pattern_title = r"(?:<title>)(?P<title>.+)(?:</title>)"
# pattern_body = r"(?:<body>)(?P<body>.+)(?:</body>)"
# pattern_remove_tags = r"<[^>]*>"
# pattern_remove_pseudo_space = r"\\n|\\t"            # "new lines" and "tabs"
# pattern_remove_spaces = r"[ ]+"
#
# text = input()
#
# title = re.search(pattern_title, text).group("title")
# body = re.search(pattern_body, text).group("body")
#
# title = re.sub(pattern_remove_tags, "", title, re.IGNORECASE | re.UNICODE)
# body = re.sub(pattern_remove_tags, "", body, re.IGNORECASE | re.UNICODE)
#
# title = re.sub(pattern_remove_pseudo_space, "", title).strip()
# body = re.sub(pattern_remove_pseudo_space, "", body).strip()
#
# title = re.sub(pattern_remove_spaces, " ", title).strip()
# body = re.sub(pattern_remove_spaces, " ", body).strip()
#
# print(f"Title: {title}")
# print(f"Content: {body}")