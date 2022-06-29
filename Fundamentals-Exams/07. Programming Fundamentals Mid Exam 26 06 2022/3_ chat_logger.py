command = input()
chat_log = []


def check_msg(msg):
    if msg in chat_log:
        return True


def chat(msg):
    chat_log.append(msg)


def delete_msg(msg):
    if check_msg(msg):
        chat_log.remove(msg)


def edit_msg(msg, edited_version):
    if check_msg(msg):
        chat_log[chat_log.index(msg)] = edited_version


def pin_msg(msg):
    if check_msg(msg):
        chat_log.append(chat_log.pop(chat_log.index(msg)))


def spam_msg(msgs):
    for msg in msgs:
        chat_log.append(msg)
    # or we can use one of this 2 methods to combine two lists also
    #chat_log.extend(msg)
    #global chat_log
    #chat_log = chat_log + msgs


while command != "end":
    command_type, *messages = command.split()
    if "Chat" in command_type:
        chat(messages[0])
    elif "Delete" in command_type:
        delete_msg(messages[0])
    elif "Edit" in command_type:
        edit_msg(messages[0], messages[1])
    elif "Pin" in command_type:
        pin_msg(messages[0])
    elif "Spam" in command_type:
        spam_msg(messages)
    command = input()

for msg in chat_log:
    print(msg)












