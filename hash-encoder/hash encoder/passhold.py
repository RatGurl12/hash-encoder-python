##make a dataframe that will hold the password, salt, and user
import csv

def filetime():
    with open("username.txt") as f:
        usernames = [line.strip() for line in f if line.strip()]
    with open("salthold.txt", "r") as f:
        salts = [line.strip() for line in f if line.strip()]
    with open("passhold.txt", "r") as f:
        passw = [line.strip() for line in f if line.strip()]

    if not (len(usernames) == len(salts) == len(passw)):
        raise ValueError("lines are wrong")

    header = ['user', 'salt', 'pass']
    filename = "infoholder.csv"

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=header)

        csv_writer.writeheader()
    
        for user, salt, pw in zip(usernames,salts, passw):
            csv_writer.writerow({
                'user': user,
                'salt': salt,
                'pass':pw
        })
