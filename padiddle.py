users = {}

#add new user
def add_user():
    while len(users) < 2:
        new_user = input("Enter Name: ")
        users[new_user.lower()] = 0
    return users

def play_padiddle():
    name = ""
    while True:
        name = input("Who called the Padiddle? ")
        if name.lower() == "exit":
            break
        for user in users:
            if user == name.lower():
                users[user] = users[user] + 1
            if name.lower() == "-" + user:
                users[user] = users[user] - 1
            elif name.lower().strip("-") not in users:
                print("There is no player by that name.")
    print(users)

add_user()
play_padiddle()
