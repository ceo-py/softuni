adding_information = input()
social_media_info = {}
likes_ = "like"
dislike_ = "dislike"
comment_ = "comment"


def create_post(post_name):
    if post_name not in social_media_info:
        social_media_info[post_name] = {}
        social_media_info[post_name][likes_] = 0
        social_media_info[post_name][dislike_] = 0
        social_media_info[post_name][comment_] = {}


def add_like(post_name):
    social_media_info[post_name][likes_] += 1


def add_dislike(post_name):
    social_media_info[post_name][dislike_] += 1


def add_comment(post_name, name, comment):
    social_media_info[post_name][comment_][name] = " ".join((comment))


while adding_information != "drop the media":
    if "comment" not in adding_information:
        command, post = adding_information.split()
    else:
        command, post, name, *comment = adding_information.split()
    if command == "post":
        create_post(post)
    elif command == "like":
        add_like(post)
    elif command == "dislike":
        add_dislike(post)
    elif command == "comment":
        add_comment(post, name, comment)
    adding_information = input()


def show_result():
    for name in social_media_info:
        print(
            f"Post: {name} | Likes: {social_media_info[name][likes_]} | Dislikes: {social_media_info[name][dislike_]}")
        print("Comments:")
        if social_media_info[name][comment_]:
            [print(f"*  {name}: {comment}") for name, comment in social_media_info[name][comment_].items()]
        else:
            print("None")


show_result()
