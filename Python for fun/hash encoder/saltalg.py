##ok game plan this will be the salt algorithm to add salt to  the inputed passwords
import secrets

##making token which will be the unique salt
def secretmaker():
    token = secrets.token_hex(16)
    return token

##writing token to file
def tokenwriter(token):
    with open("salthold.txt", "a") as f:
        f.write("\n" + token)

