
#Hardcore Username
users = { "admin": "admin privilege",   "user": "No privilege"}


#Login
username = input("Enter your username: ")

if username in users:
    current_user = {
        "username": username,
        "role": users[username]
    }
    print(f"\nLogged in as: {current_user['username']} ({current_user['role']})\n")
else:
    print("/n User not found")
    exit()


#Protected actions
def admin_role(user):
    if user["role"] == "admin":   
        print("Trying admin action:")
        admin_role(current_user)
        print("Admin access granted: You now have admin privilege")


def user_role(user):
    if user["role"] == "user":   
         print("Trying admin action:")
         admin_role(current_user)
         print("User access granted: You now have no privilege")


