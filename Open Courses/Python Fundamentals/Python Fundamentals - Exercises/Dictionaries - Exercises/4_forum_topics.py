forum_topic = input()

forum_information = {}
while forum_topic != "filter":
    topic, tags = forum_topic.split(" -> ")
    if topic not in forum_information:
        forum_information[topic] = []
    [forum_information[topic].append(x) for x in tags.split(", ") if x not in forum_information[topic]]
    forum_topic = input()


def show_result(info):
    for name in forum_information:
        if all(item in forum_information[name] for item in info):
            print(f"{name} | #{', #'.join(forum_information[name])}")


show_result(input().split(", "))
