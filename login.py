import pyrebase
from getpass import getpass


firebaseConfig = {
#put your data here

    "apiKey": "----",
    "authDomain": "---",
    "databaseURL": "---",
    "projectId": "--",
    "storageBucket": "-----",
    "messagingSenderId": "----",
    "appId": "----",
    "measurementId": "----"

}


firebase = pyrebase.initialize_app(firebaseConfig)


auth = firebase.auth()


email = input("Please Enter Your Email Address : \n")
password = input("Please Enter Your Password : \n")

#create users
#user = auth.create_user_with_email_and_password(email, password)
login = auth.sign_in_with_email_and_password(email, password)
auth.send_email_verification(login['idToken'])
#auth.send_password_reset_email(email)

print("Success .... ")


#login = auth.sign_in_with_email_and_password(email, password)

#send email verification
#auth.send_email_verification(login['idToken'])


#reset the password
#auth.send_password_reset_email(email)

#print("Success ... ")