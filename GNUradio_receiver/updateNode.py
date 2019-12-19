def setNode2():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://iotbel.firebaseio.com/test1/UQaRxn8NiGY40wxDReT5', None)
    firebase.put('/Nodes/',"Node2","true")

def resetNode2():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://iotbel.firebaseio.com/test1/UQaRxn8NiGY40wxDReT5', None)
    firebase.put('/Nodes/',"Node2","false")

def resetNode1():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://iotbel.firebaseio.com/test1/UQaRxn8NiGY40wxDReT5', None)
    firebase.put('/Nodes/',"Node1","false")


def setNode1():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://iotbel.firebaseio.com/test1/UQaRxn8NiGY40wxDReT5', None)
    firebase.put('/Nodes/',"Node1","true")
