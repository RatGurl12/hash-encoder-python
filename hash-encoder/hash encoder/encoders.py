##gameplan we take like a few hash encoders and after the password gets saltedwe run it through them

import hashlib

##function to get everything ready to be encoded
def salter(passw, salty):
    salted = passw + salty
    data = salted.encode("utf-8")
    return data

def encode1(data):
    ##makes it all silly
    sha256ob = hashlib.sha256()

    ##updating data with the hash library
    sha256ob.update(data)

    ##put it in the hex
    hexdata = sha256ob.hexdigest()

    return hexdata

def encode2(data):
    sha1 = hashlib.sha1()
    data2 = data.encode("utf-8")
    sha1.update(data2)
    hexdata = sha1.hexdigest()
    return hexdata

def encode3(data):
    sha224 = hashlib.sha224()
    sha224.update(data.encode("utf-8"))
    hexdata = sha224.hexdigest()
    return hexdata
