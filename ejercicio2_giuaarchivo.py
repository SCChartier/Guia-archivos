d ={}
arch = open("productos.txt")
for linea in arch:
    datos = linea.strip().split(":")
    producto = datos[0]
    precio = int(datos[1])
    d[producto] = precio
arch.close()
suma = 0
while True:
    prod = input("Ingrese producto: ")
    if prod == "FIN":
        break
    else:
        valor = d[prod]
        suma = suma + valor
print("la suma total es:",suma)