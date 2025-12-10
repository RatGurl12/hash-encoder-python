##shouldnt be too much in here just a lot of calling functions and stuff

import encoders
import filewriter
import saltalg
import passhold

##getting user and password
##remov it before implementation
username = input("enter username: ")
password = input("enter password")

##getting salt
salty = saltalg.secretmaker()

##encoder time
angry = encoders.salter(password, salty)
confused = encoders.encode1(angry)
bewildered = encoders.encode2(confused)
perplexed = encoders.encode3(bewildered)

##writing everything to the files
filewriter.saltwriter(salty)
filewriter.userwriter(username)
filewriter.passwriter(perplexed)

##put it all in the csv
passhold.filetime()