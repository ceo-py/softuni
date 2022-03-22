class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
line = input()

while line != "Stop":
    line = line.split()
    email = Email(line[0], line[1], line[2])
    emails.append(email)
    line = input()

send_emails = [int(n) for n in input().split(", ")]

for index, email in enumerate(emails):
    if index in send_emails:
        emails[index].send()
    print(email.get_info())
