
import csv
import pandas as pd
import encoders

##remove this before implementation
userpass = input("entr your user: ")
passpass = input("enter your password")

def grabber():
    df = pd.read_csv("infoholder.csv", sep = ",")

    return df

def grabber2(df, userpass):
    ##CHANGE IT TO BE USER INPUT
    user = df[df["user"]== userpass]
    return user

def passhunt(simpler):
    passval = simpler["pass"]
    return passval

def salthunt(simpler):
    saltval = simpler["salt"]
    return saltval

def decoder(saltval, passpass, passval):
    ##making the entered password match the original one
    counter = 0
    passcount = 0
    for row in saltval:
        salts = saltval.iloc[counter]
        salty = encoders.salter(passpass, salts)
        ## encoding time

        strange = encoders.encode1(salty)
        clarity = encoders.encode2(strange)
        normalcy = encoders.encode3(clarity)

        for row in passval:
            passw = passval.iloc[passcount]

            if normalcy == passw :
                print("hases match!")

simp = grabber()
simpler = grabber2(simp, userpass)
passval = passhunt(simpler)
saltval = salthunt(simpler)

decoder(saltval, passpass, passval)
