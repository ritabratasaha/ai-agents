import pyrebase
from flask import Flask, jsonify, request, session

config = {
  'apiKey': "",
  'authDomain': "agentauth-5906c..com",
  'projectId': "agentauth-5906c",
  'storageBucket': "agentauth-5906c..app",
  'messagingSenderId': "",
  'appId': "",
  'databaseURL' : ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def login(username:str,passw:str) -> str:
    try:
        login = auth.sign_in_with_email_and_password(email=username, password=passw)
        if login:
            token = login['idToken']
            login_user = login['email']
            session["my_user"] = login_user
            session["my_token"] = token
        return "Success"
    except Exception as e:
        error_message = str(e)
        print("error_message")
        return("Failure")


# login()