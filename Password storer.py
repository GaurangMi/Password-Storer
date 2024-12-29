#Password will be stored and encrypted
def __main__():
    print("password storer")
    from tinydb import TinyDB, Query
    from cryptography.fernet import Fernet
    db = TinyDB('encryptedpasses.json')
    fernet = Fernet(#GENERATE YOUR OWN KEY using using Fernet.generate_key()) #SAVE THIS KEY OTHERWISE UR PASSWORDS WILL BE UNDECEYPRABLE   
                                                                        #Do not change THIS if you are not remaking your db. Otherwise your previousely used passwords will be undecrptable
    doing = int(input("Enter\n1 - New password\n2 - Find password\n3 - Print all passwords\n4 - Quit\n= "))
    if doing == 1:
        Website = input("Enter what the password is for: ")
        User = input("Enter Username: ")
        Password = input("Enter password: ")
        Website = Website.lower()
        encWebsite  = fernet.encrypt(Website.encode())
        encUser     = fernet.encrypt(User.encode())
        encPassword = fernet.encrypt(Password.encode())
        db.insert({"Website" : encWebsite.decode(encoding="utf-8"), "Credentials": [encUser.decode(encoding="utf-8"), encPassword.decode(encoding="utf-8")]})
    elif doing == 2:
        querykeyword = input("Enter what the password you want to find is for: ")
        for element in db:
            byteswebsite = element['Website'].encode('utf-8')
            strwebsite = fernet.decrypt(byteswebsite).decode()
            #####
            bytesuser = element['Credentials'][0].encode('utf-8')
            struser = fernet.decrypt(bytesuser).decode()
            #####
            bytespassword = element['Credentials'][1].encode('utf-8')
            strpassword = fernet.decrypt(bytespassword).decode()
            localdb = {"Website": strwebsite, "Credentials":[struser, strpassword]}
            if localdb["Website"] == querykeyword:
                print(localdb["Credentials"])
    elif doing == 3:
        for element in db:
            byteswebsite = element['Website'].encode('utf-8')
            strwebsite = fernet.decrypt(byteswebsite).decode()
            #####
            bytesuser = element['Credentials'][0].encode('utf-8')
            struser = fernet.decrypt(bytesuser).decode()
            #####
            bytespassword = element['Credentials'][1].encode('utf-8')
            strpassword = fernet.decrypt(bytespassword).decode()
            localdb = {"Website": strwebsite, "Credentials":[struser, strpassword]}
            print(localdb)
    elif doing == 4:
        pass
    #print(db.all())

__main__()


