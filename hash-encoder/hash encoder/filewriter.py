def saltwriter(token):
    with open("salthold.txt", "a") as f:
        f.write("\n" + token)

def userwriter(token):
    with open("username.txt", "a") as f:
        f.write("\n" + token)

def passwriter(token):
    with open("passhold.txt", "a") as f:
        f.write("\n" + token)

