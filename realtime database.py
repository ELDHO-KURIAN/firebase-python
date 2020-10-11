from firebase import firebase
data=100

firebase = firebase.FirebaseApplication('--------', None)



result = firebase.post('/testx/data/',data)
print(result)
