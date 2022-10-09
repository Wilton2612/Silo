import pyrebase as bs

config = {
    "apiKey": "AIzaSyAg3Kb0scSwfw8cBSiCioIPEwmJG4qpcHw",
  "authDomain": "sensorprueba-4924b.firebaseapp.com",
  "databaseURL": "https://sensorprueba-4924b-default-rtdb.firebaseio.com",
  "projectId" : "sensorprueba-4924b",
  "storageBucket": "sensorprueba-4924b.appspot.com",
  "messagingSenderId": "44066862233",
  "appId": "1:44066862233:web:d0bad738340d4e039af408"
}


firebase = bs.initialize_app(config)

auth = firebase.auth()

#auth.create_user_with_email_and_password("juan@gmail.com", "1234567")


def login(user, password):
  try:
    login = auth.sign_in_with_email_and_password(user, password)
    print("Usuario admitido")
    return 0
  except:
    return -1