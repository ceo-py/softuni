import re

data = {}
pattern = r"(?P<username>[A-Za-z]{5,})@(?P<domain>[a-z]{3,}(\.com|\.bg|\.org))$"
count_of_mails = int(input())

for _ in range(count_of_mails):
    current_email = input()
    match = re.match(pattern, current_email)

    if match:
        username = match.group('username')
        domain = match.group('domain')

        if domain not in data:
            data[domain] = []
        if username not in data[domain]:
            data[domain].append(username)

for domain, usernames in sorted(data.items(), key=lambda x: -len(x[1])):
    print(f"{domain}:")
    for name in usernames:
        print(f"### {name}")