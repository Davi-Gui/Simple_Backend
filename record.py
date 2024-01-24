import hashlib as hl
import json as js

def db(user):
    with open("data.txt", "w") as data:
        data.write(user)

def init():
    users = {}
    user = hl.sha256(str(input("Username: ")).encode()).hexdigest()
    password = hl.sha256(str(input("Password: ")).encode()).hexdigest()

    users[user] = password

    d = js.dumps(users, indent=2)
    return d

def main():
    d = init()
    db(d)
    

if __name__ == "__main__":
    main()