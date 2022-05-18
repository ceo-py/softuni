web_info = []
data_input = input()


class Website:
    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = queries

    def __repr__(self):
        if self.queries:
            return f"https://www.{show.host}.{show.domain}/query?=[{']&['.join(show.queries)}]"
        return f"https://www.{show.host}.{show.domain}"


while data_input != "end":
    web_name, domain, *queries = data_input.split(" | ")
    if queries:
        queries = queries[0].split(",")
    web_info.append(Website(web_name, domain, queries))
    data_input = input()

for show in web_info:
    print(show)

