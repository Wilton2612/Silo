
import openpyxl




book = openpyxl.load_workbook('data/usuario.xlsx')
libro = book.active

usuario = libro['A1']
password = libro['B1']

print(usuario.value, password.value)
"""
hoja = Workbook()

sheet = hoja.active

sheet['A1']=5

encabezado = ["id_silo", "fecha", "inventario", 
                "ocupación","estado" ]

letras = ["A", "B", "C", "D", "E"]


for i in range(len(encabezado)):
    sheet[letras[i]+'1'] = "hola"






hoja.save('datos.xlsx')
"""


"""
s = "juan225@gmail.com"
lista_nombre = list(s)


i = 0
usuario = ""
while i < len(lista_nombre):
    if lista_nombre[i] != "@":
        usuario+=lista_nombre[i]
        i+=1
    else:
        break
print(usuario)    

"""










"""
archivo = xlsxwriter.workbook('datos.xlsx')
hoja = archivo.add_worksheet()

for i in range(len(encabezado)):
    hoja.write(0, i, encabezado[i])
"""