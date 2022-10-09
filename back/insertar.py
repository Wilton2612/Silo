
from firebase import firebase
from datetime import datetime



db = firebase.FirebaseApplication('https://sensorprueba-4924b-default-rtdb.firebaseio.com/')




"""
def crear_silo(alturaCilindro, diametro, alturaCono):
    da = {"id":0, "fecha":"23-04-2022", "capacidad":1500, "ocupacion":"23%", "estado": "inactivo", "alturaCilindro":20, "diametro":15,"alturaCono":2 }
    db.post("/silo", da)
"""


"""DATOS DE JUAN"""


"""
da = {"id":0, "fecha":"2022-23-04", "inventario":250, "ocupacion":"16.66%", "estado": "inactivo", "alturaCilindro":20, "diametro":15,"alturaCono":2, "capacidad": 1500 }
db.post("/silo/juan", da)

daa = {"id":1, "fecha":"2021-23-06", "inventario":600, "ocupacion":"40%", "estado": "activo", "alturaCilindro":15, "diametro":10,"alturaCono":1,  "capacidad": 1500 }
db.post("/silo/juan", daa)

da1 = {"id":2, "fecha":"2022-13-08", "inventario":1400, "ocupacion":"70%", "estado": "activo", "alturaCilindro":20, "diametro":15,"alturaCono":2,  "capacidad": 2000 }
db.post("/silo/juan", da1)


da2 = {"id":3, "fecha":"2020-14-06", "inventario":400, "ocupacion":"26.66%", "estado": "inactivo", "alturaCilindro":15, "diametro":10,"alturaCono":1,  "capacidad": 1500 }
db.post("/silo/juan", da2)


da3 = {"id":4, "fecha":"2022-15-03", "inventario":1300, "ocupacion":"72.22%", "estado": "activo", "alturaCilindro":20, "diametro":15,"alturaCono":2,  "capacidad": 1800 }
db.post("/silo/juan", da3)


da4 = {"id":5, "fecha":"2021-19-05", "inventario":1500, "ocupacion":"75%", "estado": "activo", "alturaCilindro":15, "diametro":10,"alturaCono":1,  "capacidad": 2000 }
db.post("/silo/juan", da4)



da5 = {"id":6, "fecha":"2022-21-10", "inventario":1400, "ocupacion":"93.33%", "estado": "activo", "alturaCilindro":20, "diametro":15,"alturaCono":2,  "capacidad": 1500 }
db.post("/silo/juan", da5)


da6 = {"id":7, "fecha":"2022-27-12", "inventario":800, "ocupacion":"53.33%", "estado": "activo", "alturaCilindro":15, "diametro":10,"alturaCono":1,  "capacidad": 1500 }
db.post("/silo/juan", da6)
"""

  

"""DATOS DE ANDRES"""

"""

dass = {"id":0, "fecha":"2019-01-10", "inventario":1700, "ocupacion":"85%", "estado": "activo", "alturaCilindro":20, "diametro":15,"alturaCono":2,  "capacidad": 2000 }
db.post("/silo/andres26", dass)


dossss= {"id":1, "fecha":"2021-22-12", "inventario":1250, "ocupacion":"83.33%", "estado": "activo", "alturaCilindro":15, "diametro":10,"alturaCono":1,  "capacidad": 1500 }
db.post("/silo/andres26", dossss)

print(datetime.today().strftime('%Y-%m-%d'))

"""




def agregar_silo(alturaCilindro, diametro, alturaCono,capacidad, usuario):
        
    try:
    
        datos = db.get("/silo/"+usuario, "")
        fecha = datetime.today().strftime('%Y-%m-%d')

        if len(datos) == 0:
                da_cero = {"id":0,"fecha":fecha, "inventario":0, "ocupacion":"0%", "estado": "activo", "alturaCilindro":alturaCilindro, "diametro":diametro,"alturaCono":alturaCono, "capacidad":capacidad}
                db.post("/silo/"+usuario, da_cero)
        else:
            da_resto = da_cero = {"id":len(datos),"fecha":fecha, "inventario":0, "ocupacion":"0%", "estado": "activo", "alturaCilindro":alturaCilindro, "diametro":diametro,"alturaCono":alturaCono, "capacidad":capacidad}
            db.post("/silo/"+usuario, da_resto)
        return 0
    except:
        return -1

        




"""
    da6 = {"id":0, "fecha":"", "capacidad":0, "ocupacion":"70%", "estado": "activo", "alturaCilindro":alturaCilindro, "diametro":diametro,"alturaCono":alturaCono}
    db.post("/silo/"+usuario, da6)
    """
