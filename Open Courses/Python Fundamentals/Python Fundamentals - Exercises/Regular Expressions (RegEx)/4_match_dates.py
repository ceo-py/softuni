import re

dates_match = input()
pattern = re.compile(
    r"(\d{2}-[A-Z]{1}[a-z]{2}-\b\d{4}\b|\d{2}\.[A-Z]{1}[a-z]{2}\.\b\d{4}\b|\d{2}/[A-Z]{1}[a-z]{2}/\b\d{4}\b)")
matches = pattern.finditer(dates_match)
for show in matches:
    if "/" in show[0]:
        show = show[0].split("/")
    elif "-" in show[0]:
        show = show[0].split("-")
    elif "." in show[0]:
        show = show[0].split(".")
    print(f"Day: {show[0]}, Month: {show[1]}, Year: {show[2]}")

