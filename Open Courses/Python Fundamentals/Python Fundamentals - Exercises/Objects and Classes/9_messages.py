from itertools import zip_longest


class User:
    registered_users = {}
    msg_between_users = {}

    def __init__(self, username, received_messages):
        self.username = username
        self.received_messages = []


class Message:
    registered_messages = {}

    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


user_input = input()
while user_input != "exit":
    args = user_input.split()
    if "register" in args[0]:
        current_user,  User.registered_users[args[1]] = User(args[1], []), []
    elif "send" in args[1]:
        sender, recipient, content = args[0], args[2], args[3]
        if sender not in User.msg_between_users:
            User.msg_between_users[sender] = []
        if recipient not in User.msg_between_users[sender]:
            User.msg_between_users[sender].append(recipient)
        if all([sender in User.registered_users, recipient in User.registered_users]):
            current_message = Message(content, sender)
            if sender not in Message.registered_messages:
                Message.registered_messages[sender] = [0]
            if recipient not in Message.registered_messages:
                Message.registered_messages[recipient] = [0]
            User.registered_users[recipient].append(content)
            Message.registered_messages[sender].append(content)
    user_input = input()

names_to_check = input().split()
check_ = False
for name in User.msg_between_users:
    User.msg_between_users[name].append(name)
    if all([names_to_check[0] in User.msg_between_users[name],
            names_to_check[1] in User.msg_between_users[name]]):
        check_ = True
        break
if check_:
    continue_ = "Empty"
    for sender, recipient in zip_longest(Message.registered_messages[names_to_check[0]],
                                         Message.registered_messages[names_to_check[1]], fillvalue=continue_):
        if all([0 != sender != continue_, 0 != recipient != continue_]):
            print(f'{names_to_check[0]}: {sender}')
            print(f'{recipient} :{names_to_check[1]}')
        elif all([0 != sender != continue_, 0 != recipient == continue_]):
            print(f'{names_to_check[0]}: {sender}')
        elif all([0 != sender == continue_, 0 != recipient != continue_]):
            print(f'{recipient} :{names_to_check[1]}')
else:
    print("No messages")
