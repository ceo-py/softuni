login_dic = {}

add_user = input()
uns_logins = 0
while add_user != "login":
    add_user = add_user.split(" -> ")
    if add_user[0] not in login_dic:
        login_dic[add_user[0]] = ""
    login_dic[add_user[0]] = add_user[-1]
    add_user = input()

login_check = input()

while login_check != "end":
    log_success = False
    login_check = login_check.split(" -> ")
    if login_check[0] in login_dic:
        if login_dic[login_check[0]] == login_check[-1]:
            print(f"{login_check[0]}: logged in successfully")
            log_success = True
    if not log_success:
        uns_logins += 1
        print(f"{login_check[0]}: login failed")

    login_check = input()

if uns_logins:
    print(f"unsuccessful login attempts: {uns_logins}")
