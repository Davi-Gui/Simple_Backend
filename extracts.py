import record

def recover():
    with open("data.txt", "r") as data:
        d = data.read()

    return d

def main():
    u = record.init()
    d = recover()

    if u == d:
        print("\033[32mAccess granted!\033[m")
    else:
        print("\033[31mInvalid access!\033[m")

if __name__ == "__main__":
    main()