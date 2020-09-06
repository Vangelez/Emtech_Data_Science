
"""
Autor: Victoria Díaz Solís
Fecha: Septiembre 04, 2020
Descripción: Gerencia de Ventas solicita que se realice un análisis de la rotación de productos.

Listas utilizadas:

lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore-products = [id_product, name, price, category, stock]
"""

# Administradores
administradores = [['A1', 123]]

# Entrada al programa
print("Bienvenido a LifeStore \n")

tipo_usuario = input("Elije una opción para ingresar: Administrador/Invitado: ")

while tipo_usuario == "Invitado" or "Administrador":

  if tipo_usuario == "Invitado":
    print("Bienvenido a LifeStore, no puedes acceder al siguiente contenido.")
    print("Gracias por visitar LifeStore. ¡Hasta pronto!")
    break

  if tipo_usuario == "Administrador":
    administrador = input("Ingresa tu usuario: ")
    contrasena = int(input("Ingresa su contraseña numérica: "))

    for i in administradores:
      if i[0] != administrador or i[1] != contrasena:
        print("Ususario y/o contraseña incorrectos. Intente nuevamente.")
        administrador = input("Ingresa tu usuario: ")
        contrasena = int(input("Ingresa su contraseña numérica: "))

      if i[0] == administrador and i[1] == contrasena:
        print()
        print("Bienvenido a LifeStore: \n" )

        print("Recursos disponibles: \n")
        print(" 1. Productos con mayores ventas")
        print(" 2. Productos con mayor búsquedas")
        print(" 3. Productos con menores ventas (por categoría)")
        print(" 4. Productos con menores búsquedas (por categoría)")
        print(" 5. Productos con las mejores reseñas")
        print(" 6. Productos con las peores reseñas")
        print(" 7. Ingresos por producto")
        print(" 8. Ingreso total anual")
        print(" 9. Ingresos totales (todos los años)")
        print(" 10. Ventas mensuales")
        print(" 11. Meses con más ventas al año")
    break

  else:    
    print("Tipo de usuario inválido. Intente nuevamente.")
    tipo_usuario = input("Elije una opción para ingresar: Administrador/Invitado: ")
print()
print("*************************************************")

print("----------------------")
print("IMPORTACIÓN DE LISTAS:")
print("----------------------")

# Importación de la lista de productos:
from lifestore_file import lifestore_products

# Importación de la lista de ventas:
from lifestore_file import lifestore_sales

# Importación de la lista de búsquedaa:
from lifestore_file import lifestore_searches

print("------------------------------------------------")
print("1. PRODUCTOS MÁS VENDIDOS Y PRODUCTOS REZAGADOS")
print("------------------------------------------------ \n")

print("a) Lista con los productos con mayores ventas: \n")

# Loop para extraer el nombre de los productos:
nombres_productos=[]
for producto in lifestore_products:
    nombres=[producto[0:2]]
    nombres_productos.append(nombres)

# Loop para extraer los productos vendidos en lifestore_sales:
id_producto=[]
for producto in lifestore_sales:
  id_producto.append(producto[1])

#Loop para contabilizar el número de ventas por producto:
contador_ventas=[]
for i in range(1,len(lifestore_products)+1):
    count = 0
    for k in id_producto:
        if k == i:
            count+= 1
    contador_ventas.append([i,count])

# Loop para agregar el nombre del producto al contador de ventas:
contador_ventas_n=[]
for i in range(len(contador_ventas)):
  m=nombres_productos[i][0]
  n=contador_ventas[i][1]
  contador_ventas_n.append([m,n])

# Loop para borrar los productos con cero ventas:
ventas_productos=[]
for i in contador_ventas:
    if i[1]!=0:
        ventas_productos.append(i)

# Loop para ordenar las ventas de mayor a menor:
venta_descendente=[]
while ventas_productos:
    maximo=ventas_productos[0][1]
    lista_actual=ventas_productos[0]
    for producto in ventas_productos:
        if producto[1]>maximo:
            maximo=producto[1]
            lista_actual=producto
    venta_descendente.append(lista_actual)
    ventas_productos.remove(lista_actual)

# Para mostrar la lista:
row_format = "{:>8}  {:>8}"
headers_ventas = ['Producto', 'Número de ventas']
header_row = row_format.format(*headers_ventas) 
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))  
for producto in venta_descendente:
  print(row_format.format(*producto))
print("." * (len(header_row) + 1))
print()

#--------------------------------------------------------------#

print("b) Lista con los productos con mayores búsquedas:\n ")

# Loop para extraer los productos buscados en lifestore_searches:
id_producto=[]
for producto in lifestore_searches:
  id_producto.append(producto[1])

#Loop para contabilizar el número de búsquedas por producto:
contador_busquedas=[]
for i in range(1,len(lifestore_products)+1):
    count = 0
    for k in id_producto:
        if k == i:
            count+= 1
    contador_busquedas.append([i,count])

# Loop para borrar los productos con cero búsquedas:
busquedas_productos=[]
for i in contador_busquedas:
    if i[1]!=0:
        busquedas_productos.append(i)

# Loop para ordenar las búsquedas de mayor a menor:
busquedas_descendente=[]
while busquedas_productos:
    maximo=busquedas_productos[0][1]
    lista_actual=busquedas_productos[0]
    for producto in busquedas_productos:
        if producto[1]>maximo:
            maximo=producto[1]
            lista_actual=producto
    busquedas_descendente.append(lista_actual)
    busquedas_productos.remove(lista_actual)

# Para mostrar la lista:
row_format = "{:>8}  {:>8}"
headers_busquedas = ['Producto', 'Número de búsquedas']
header_row = row_format.format(*headers_busquedas) 
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))  
for producto in busquedas_descendente:
  print(row_format.format(*producto))
print("." * (len(header_row) + 1))
print()
#--------------------------------------------------------------#

print("c) Lista con los productos con menores ventas (por cada categoría): \n")

# Loop para extraer los productos vendidos en lifestore_sales:
id_producto=[]
for producto in lifestore_sales:
  id_producto.append(producto[1])

#Loop para contabilizar el número de ventas por producto (por categoría):
contador_ventas_c=[]
for i in range(1,len(lifestore_products)+1):
  count = 0
  for k in id_producto:
    if k == i:
      count+= 1
  if 1 <= i <= 9:
    categorias=['procesadores', i, count]
  elif 10 <= i <= 28:
    categorias = ['tarjetas de video', i, count]
  elif 29 <= i <= 46:
    categorias = ['tarjetas madre', i, count]
  elif 47 <= i <= 59:
    categorias = ['discos duros', i, count]
  elif 60 <= i <= 61:
    categorias = ['memorias usb', i, count]
  elif 62 <= i <= 73:
    categorias = ['pantallas', i, count]
  elif 74 <= i <= 83:
    categorias = ['bocinas', i, count]
  elif 84 <= i <= 96:
    categorias = ['audifonos', i, count]
  contador_ventas_c.append(categorias)

# Loop para borrar los productos con cero ventas:
ventas_productos_c=[]
for i in contador_ventas_c:
    if i[2]!=0:
        ventas_productos_c.append(i)

# Loop para ordenar las ventas de menor a mayor:
l = len(ventas_productos_c)
for i in range(0, l):
    for j in range(0, l-i-1):
        if (ventas_productos_c[j][2] > ventas_productos_c[j + 1][2]):
            tempo = ventas_productos_c[j]
            ventas_productos_c[j]= ventas_productos_c[j + 1]
            ventas_productos_c[j + 1]= tempo

# Loop para ordenar las ventas de menor a mayor (por categoría):
ventas_ascendente_c1=[]
ventas_ascendente_c2=[]
ventas_ascendente_c3=[]
ventas_ascendente_c4=[]
ventas_ascendente_c5=[]
ventas_ascendente_c6=[]
ventas_ascendente_c7=[]
ventas_ascendente_c8=[]

for i in ventas_productos_c:
    if i[0]=='procesadores':
        ventas_ascendente_c1.append(i)
    if i[0] == 'tarjetas de video':
        ventas_ascendente_c2.append(i)
    if i[0] == 'tarjetas madre':
        ventas_ascendente_c3.append(i)
    if i[0] == 'discos duros':
        ventas_ascendente_c4.append(i)
    if i[0] == 'memorias usb':
        ventas_ascendente_c5.append(i)
    if i[0] == 'pantallas':
        ventas_ascendente_c6.append(i)
    if i[0] == 'bocinas':
        ventas_ascendente_c7.append(i)
    if i[0] == 'audifonos':
        ventas_ascendente_c8.append(i)

# Lista anidada de las ventas por categoría:
ventas_productos_c=[ventas_ascendente_c1, ventas_ascendente_c2, ventas_ascendente_c3,ventas_ascendente_c4,ventas_ascendente_c5,ventas_ascendente_c6,ventas_ascendente_c7,ventas_ascendente_c8]

# Para mostrar la lista de los productos con menos ventas por categoría:
row_format = "{:>18}  {:>12} {:>10}"
headers_ventas = ['Categoria','Producto', 'Número de ventas']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_productos_c:
    for k in i:
        print(row_format.format(*k))
print("." * (len(header_row) + 1))
print()

#--------------------------------------------------------------#

print("d) Lista con los productos con menores búsquedas (por categorías): \n")

# Loop para extraer los productos vendidos en lifestore_sales:
id_product=[]
for producto in lifestore_searches:
  id_product.append(producto[1])

# Se contabilizan las busquedas por producto y categoría
contador_busquedas=[]
for i in range(1,len(lifestore_products)+1):
    count = 0
    for k in id_product:
        if k == i:
            count+= 1
    if 1 <= i <= 9:
        categorias=['procesadores', i, count]
    elif 10 <= i <= 28:
        categorias = ['tarjetas de video', i, count]
    elif 29 <= i <= 46:
        categorias = ['tarjetas madre', i, count]
    elif 47 <= i <= 59:
        categorias = ['discos duros', i, count]
    elif 60 <= i <= 61:
        categorias = ['memorias usb', i, count]
    elif 62 <= i <= 73:
        categorias = ['pantallas', i, count]
    elif 74 <= i <= 83:
        categorias = ['bocinas', i, count]
    elif 84 <= i <= 96:
        categorias = ['audifonos', i, count]
    contador_busquedas.append(categorias)

# Loop para borrar los productos con cero busquedas:
busquedas_productos_c=[]
for i in contador_busquedas:
    if i[2]!=0:
        busquedas_productos_c.append(i)

# Loop para ordenar las busquedas de menor a mayor:
l = len(busquedas_productos_c)
for i in range(0, l):
    for j in range(0, l-i-1):
        if (busquedas_productos_c[j][2] > busquedas_productos_c[j + 1][2]):
            tempo = busquedas_productos_c[j]
            busquedas_productos_c[j]= busquedas_productos_c[j + 1]
            busquedas_productos_c[j + 1]= tempo

# Loop para ordenar las búsquedas de menor a mayor (por categoría):
busquedas_ascendente_c1=[]
busquedas_ascendente_c2=[]
busquedas_ascendente_c3=[]
busquedas_ascendente_c4=[]
busquedas_ascendente_c5=[]
busquedas_ascendente_c6=[]
busquedas_ascendente_c7=[]
busquedas_ascendente_c8=[]

for i in busquedas_productos_c:
    if i[0]=='procesadores':
        busquedas_ascendente_c1.append(i)
    if i[0] == 'tarjetas de video':
        busquedas_ascendente_c2.append(i)
    if i[0] == 'tarjetas madre':
        busquedas_ascendente_c3.append(i)
    if i[0] == 'discos duros':
        busquedas_ascendente_c4.append(i)
    if i[0] == 'memorias usb':
        busquedas_ascendente_c5.append(i)
    if i[0] == 'pantallas':
        busquedas_ascendente_c6.append(i)
    if i[0] == 'bocinas':
        busquedas_ascendente_c7.append(i)
    if i[0] == 'audifonos':
        busquedas_ascendente_c8.append(i)

# Lista anidada de las busquedas por categoría:
busquedas_productos_c=[busquedas_ascendente_c1, busquedas_ascendente_c2, busquedas_ascendente_c3,busquedas_ascendente_c4,busquedas_ascendente_c5,busquedas_ascendente_c6,busquedas_ascendente_c7,busquedas_ascendente_c8]

# Para mostrar la lista de los productos con menos búsquedas por categoría:
row_format = "{:>18}  {:>12} {:>10}"
headers_ventas = ['Categoria','Producto', 'Número de búsquedas']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in busquedas_productos_c:
    for k in i:
        print(row_format.format(*k))
print("." * (len(header_row) + 1))
print()

print("* - * - * - * - * - * - * - * - * - * - * - * - * - * \n")


print("--------------------------------------")
print("2. PRODUCTOS POR RESEÑA EN EL SERVICIO")
print("--------------------------------------\n")

print("a) Lista con 20 productos con las mejores reseñas \n")

# Loop para extraer los productos vendidos y los scores que obtieron en lifestore_sales:
id_product=[]
for producto in lifestore_sales:
  id_product.append(producto[1:3])

# Loop para promediar las calificaciones por casa producto:
contador_scores=[]
for i in range(1,len(lifestore_products)+1):
    sum = 0
    c=0
    for k in id_product:
        if k[0] == i:
            sum += k[1]
            c += 1
            avg = sum / c
    contador_scores.append([i,round(avg, 2)])

# Loop para ordenar las reseñas de manera descendente:
mejores_resenas=[]
l = len(contador_scores)
for i in range(0, l):
    for j in range(0, l-i-1):
        if (contador_scores[j][1] < contador_scores[j + 1][1]):
            tempo = contador_scores[j]
            contador_scores[j]= contador_scores[j + 1]
            contador_scores[j + 1]= tempo
            mejores_resenas=contador_scores

# Para mostrar la lista de los productos con mejores reseñas:
row_format = "{:>8} {:>8}"
headers_ventas = ['Producto', 'Reseñas']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in mejores_resenas[0:21]:
        print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

#--------------------------------------------------------------#

print("b) Lista con 20 productos con las peores reseñas \n")

# Loop para ordenar las reseñas de manera descendente:
peores_resenas=[]
l = len(contador_scores)
for i in range(0, l):
    for j in range(0, l-i-1):
        if (contador_scores[j][1] > contador_scores[j + 1][1]):
            tempo = contador_scores[j]
            contador_scores[j]= contador_scores[j + 1]
            contador_scores[j + 1]= tempo
            peores_resenas=contador_scores

# Para mostrar la lista de los productos con peores reseñas:
row_format = "{:>8} {:>8}"
headers_ventas = ['Producto', 'Reseñas']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in peores_resenas[0:21]:
        print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

print("* - * - * - * - * - * - * - * - * - * - * - * - * - * \n")

print("------------------------------------------")
print("3. INGRESOS Y VENTAS (MENSUALES Y ANUALES)")
print("------------------------------------------\n")

print("a) Ingresos por producto: \n")

# Loop para extraer los productos vendidos en lifestore_sales:
id_producto=[]
for producto in lifestore_sales:
  id_producto.append(producto[1])

#Loop para contabilizar el número de ventas por producto:
contador_ventas=[]
for i in range(1,len(lifestore_products)+1):
    count = 0
    for k in id_producto:
        if k == i:
            count+= 1
    contador_ventas.append([i,count])

# Loop para extraer los productos y sus precios de lifestore_products :
precio_producto=[]
for producto in lifestore_products:
  precio_producto.append([producto[0],producto[2]])

# Loop para calcular los ingresos por producto:
ingresos_por_producto=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(contador_ventas[i][j] * precio_producto[i][j])
    ingresos_por_producto.append([i+1,contador_ventas[i][1],precio_producto[i][1], m])

# Para mostrar la lista de los productos con mejores reseñas:
row_format = "{:>8} {:>15}  {:>15}  {:>18}"
headers_ventas = ['Producto', 'Productos vendidos', 'Precio del producto',  'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ingresos_por_producto:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

#--------------------------------------------------------------#

print("b) Ingreso total anual: \n")

# Loop para extraer los productos vendidos por año en lifestore_sales:
id_producto=[]
for producto in lifestore_sales:
  id_producto.append([producto[1],producto[3][6:10]])

# Loop para crear listas de ventas de producto por año:
ventas_2020=[]
ventas_2019=[]
ventas_2002=[]

for i in id_producto:
    if i[1]=='2020':
        ventas_2020.append(i)
    if i[1]=='2019':
        ventas_2019.append(i)
    if i[1]=='2002':
        ventas_2002.append(i)

# Se crea una lista con las listas de ventas de productos en el año:
ventas_por_ano=[ventas_2002,ventas_2019,ventas_2020]

# Loop para contabilizar las ventas de productos por año:
contador_ventas_anuales=[]

for i in range(1,len(lifestore_products)+1):
    # count=0
    for k in ventas_por_ano:
        count = 0
        for j in k:
            if j[0] == i:
                count += 1
        contador_ventas_anuales.append([j[1],i,count])

# Loop para extraer las listas de ventas por producto por año ya contabilizadas:
contador_ventas_2020=[]
contador_ventas_2019=[]
contador_ventas_2002=[]

for i in contador_ventas_anuales:
    if i[0]=='2020':
        contador_ventas_2020.append(i)
    if i[0]=='2019':
        contador_ventas_2019.append(i)
    if i[0]=='2002':
        contador_ventas_2002.append(i)

# 2002

# Loop para calcular los ingresos por producto vendidos en año 2002:
ingresos_por_producto_2002=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(contador_ventas_2002[i][2] * precio_producto[i][j])
    ingresos_por_producto_2002.append([contador_ventas_2002[i][0],i+1,contador_ventas_2002[i][2],precio_producto[i][1], m])
# print(ingresos_por_producto_2002) # Por si se quiere ver el desglose de productos vendidos con su respectivo aporte.

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en el 2002:
ingresos_anual_2002 = 0
for i in ingresos_por_producto_2002:
    ingresos_anual_2002 += i[4]
print("Ingresos totales percibidos en el 2002:", ingresos_anual_2002)

# 2019

# Loop para calcular los ingresos por producto vendidos en año 2019:
ingresos_por_producto_2019=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(contador_ventas_2019[i][2] * precio_producto[i][j])
    ingresos_por_producto_2019.append([contador_ventas_2019[i][0],i+1,contador_ventas_2019[i][2],precio_producto[i][1], m])
# print(ingresos_por_producto_2019) # Por si se quiere ver el desglose de productos vendidos con su respectivo aporte.

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en el 2019:
ingresos_anual_2019 = 0
for i in ingresos_por_producto_2019:
    ingresos_anual_2019 += i[4]
print("Ingresos totales percibidos en el 2019:", ingresos_anual_2019)

# 2020

# Loop para calcular los ingresos por producto vendidos en año 2020:
ingresos_por_producto_2020=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(contador_ventas_2020[i][2] * precio_producto[i][j])
    ingresos_por_producto_2020.append([contador_ventas_2020[i][0],i+1,contador_ventas_2020[i][2],precio_producto[i][1], m])
# print(ingresos_por_producto_2020) # Por si se quiere ver el desglose de productos vendidos con su respectivo aporte.

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en el 2020:
ingresos_anual_2020 = 0
for i in ingresos_por_producto_2020:
    ingresos_anual_2020 += i[4]
print("Ingresos totales percibidos en el 2020:", ingresos_anual_2020)
print()

#--------------------------------------------------------------#

print("c) Total de ingresos (todos los años): \n")

ingresos_totales=ingresos_anual_2002+ingresos_anual_2019+ingresos_anual_2020
print("Ingresos totales (todos los años): ",ingresos_totales)
print()
#--------------------------------------------------------------#

print("d) Ventas e ingresos  mensuales: \n")

# Loop para extraer los productos vendidos en lifestore_sales:
id_producto=[]
for producto in lifestore_sales:
  id_producto.append([producto[1],producto[3][3:5],producto[3][6:10]])

# Loop para crear listas de ventas de producto por año:
ventas_2020=[]
ventas_2019=[]
ventas_2002=[]

for i in id_producto:
    if i[2]=='2020':
        ventas_2020.append(i)
    if i[2]=='2019':
        ventas_2019.append(i)
    if i[2]=='2002':
        ventas_2002.append(i)

# Se decidió utilizar únicamente el año 2020:

# Loop para crear listas de ventas de producto por mes de 2020:
ventas_2020_ene=[]
ventas_2020_feb=[]
ventas_2020_mar=[]
ventas_2020_abr=[]
ventas_2020_may=[]
ventas_2020_jun=[]
ventas_2020_jul=[]
ventas_2020_ago=[]
ventas_2020_sep=[]
ventas_2020_oct=[]
ventas_2020_nov=[]
ventas_2020_dic=[]

for i in ventas_2020:
    if i[1]=='01':
        ventas_2020_ene.append(i)
    if i[1]=='02':
        ventas_2020_feb.append(i)
    if i[1]=='03':
        ventas_2020_mar.append(i)
    if i[1]=='04':
        ventas_2020_abr.append(i)
    if i[1]=='05':
        ventas_2020_may.append(i)
    if i[1]=='06':
        ventas_2020_jun.append(i)
    if i[1]=='07':
        ventas_2020_jul.append(i)
    if i[1]=='08':
        ventas_2020_ago.append(i)
    if i[1]=='09':
        ventas_2020_sep.append(i)
    if i[1]=='10':
        ventas_2020_oct.append(i)
    if i[1]=='11':
        ventas_2020_nov.append(i)
    if i[1]=='12':
        ventas_2020_dic.append(i)

# Se crea una lista con las listas de ventas de prodcutos en el mes:
ventas_2020_meses=[ventas_2020_ene,ventas_2020_feb,ventas_2020_mar,ventas_2020_abr,
                ventas_2020_may,ventas_2020_jun,ventas_2020_jul,ventas_2020_ago,
                ventas_2020_sep,ventas_2020_oct,ventas_2020_nov,ventas_2020_dic]

# Loop para contabilizar las ventas de productos por mes:
contador_ventas_mensuales=[]

for i in range(1,len(lifestore_products)+1):
    for k in ventas_2020_meses:
        count = 0
        for j in k:
            if j[0] == i:
                count += 1
        contador_ventas_mensuales.append([j[1],i,count])

# Loop para extraer las listas de productos vendidos por mes ya contabilizadas:
ventas_2020_ene=[]
ventas_2020_feb=[]
ventas_2020_mar=[]
ventas_2020_abr=[]
ventas_2020_may=[]
ventas_2020_jun=[]
ventas_2020_jul=[]
ventas_2020_ago=[]
ventas_2020_sep=[]
ventas_2020_oct=[]
ventas_2020_nov=[]
ventas_2020_dic=[]

for i in contador_ventas_mensuales:
    if i[0]=='01':
        ventas_2020_ene.append(i)
    if i[0]=='02':
        ventas_2020_feb.append(i)
    if i[0]=='03':
        ventas_2020_mar.append(i)
    if i[0]=='04':
        ventas_2020_abr.append(i)
    if i[0]=='05':
        ventas_2020_may.append(i)
    if i[0]=='06':
        ventas_2020_jun.append(i)
    if i[0]=='07':
        ventas_2020_jul.append(i)
    if i[0]=='08':
        ventas_2020_ago.append(i)
    if i[0]=='09':
        ventas_2020_sep.append(i)
    if i[0]=='10':
        ventas_2020_oct.append(i)
    if i[0]=='11':
        ventas_2020_nov.append(i)
    if i[0]=='12':
        ventas_2020_dic.append(i)

# ENERO 2020

# Loop para 
ventas_productos_2020_ene=[]
for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(ventas_2020_ene[i][2] * precio_producto[i][j])
    ventas_productos_2020_ene.append([ventas_2020_ene[i][0],i+1,ventas_2020_ene[i][2],precio_producto[i][1], m])

# Loop para borrar los productos con cero ventas en el mes de enero:
ventas_promedio_2020_ene=[]
for i in ventas_productos_2020_ene:
    if i[2] != 0:
        ventas_promedio_2020_ene.append(i)
    if i[0] == '01':
        i[0]='Enero'

# Loop para sumar los productos vendidos en enero de 2020:
productos_enero_2020 = 0
for i in ventas_promedio_2020_ene:
    productos_enero_2020 += i[2]
print("Productos vendidos en enero de 2020:", productos_enero_2020)

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en enero de 2020:
ingresos_enero_2020 = 0
for i in ventas_promedio_2020_ene:
    ingresos_enero_2020 += i[4]
print("Ingresos totales percibidos en enero de 2020:", ingresos_enero_2020)
print()

# Para mostrar la lista de los productos vendidos en enero:
row_format = "{:>8} {:>8}  {:>13}  {:>16}  {:>16}"
headers_ventas = ['Mes','Producto',  'Productos vendidos', 'Precio del producto', 'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_promedio_2020_ene:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

# FEBRERO 2020

ventas_productos_2020_feb=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(ventas_2020_feb[i][2] * precio_producto[i][j])
    ventas_productos_2020_feb.append([ventas_2020_feb[i][0],i+1,ventas_2020_feb[i][2],precio_producto[i][1], m])

# Loop para borrar los productos con cero ventas en el mes de febrero:
ventas_promedio_2020_feb=[]
for i in ventas_productos_2020_feb:
    if i[2] != 0:
        ventas_promedio_2020_feb.append(i)
    if i[0] == '02':
        i[0]='Febrero'

# Loop para sumar los productos vendidos en febrero de 2020:
productos_febrero_2020 = 0
for i in ventas_promedio_2020_feb:
    productos_febrero_2020 += i[2]
print("Productos vendidos en febrero de 2020:", productos_febrero_2020)

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en febrero de 2020:
ingresos_febrero_2020 = 0
for i in ventas_promedio_2020_feb:
    ingresos_febrero_2020 += i[4]
print("Ingresos totales percibidos en febrero de 2020:", ingresos_febrero_2020)
print()

# Para mostrar la lista de los productos vendidos en febrero:
row_format = "{:>8} {:>8}  {:>13}  {:>16}  {:>16}"
headers_ventas = ['Mes','Producto',  'Productos vendidos', 'Precio del producto', 'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_promedio_2020_feb:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

# MARZO 2020

ventas_productos_2020_mar=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(ventas_2020_mar[i][2] * precio_producto[i][j])
    ventas_productos_2020_mar.append([ventas_2020_mar[i][0],i+1,ventas_2020_mar[i][2],precio_producto[i][1], m])

# Loop para borrar los productos con cero ventas en el mes de marzo:
ventas_promedio_2020_mar=[]
for i in ventas_productos_2020_mar:
    if i[2] != 0:
        ventas_promedio_2020_mar.append(i)
    if i[0] == '03':
        i[0]='Marzo'

# Loop para sumar los productos vendidos en marzo de 2020:
productos_marzo_2020 = 0
for i in ventas_promedio_2020_mar:
    productos_marzo_2020 += i[2]
print("Productos vendidos en marzo de 2020:", productos_marzo_2020)

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en marzo de 2020:
ingresos_marzo_2020 = 0
for i in ventas_promedio_2020_mar:
    ingresos_marzo_2020 += i[4]
print("Ingresos totales percibidos en marzo de 2020:", ingresos_marzo_2020)
print()

# Para mostrar la lista de los productos vendidos en marzo:
row_format = "{:>8} {:>8}  {:>13}  {:>16}  {:>16}"
headers_ventas = ['Mes','Producto',  'Productos vendidos', 'Precio del producto', 'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_promedio_2020_mar:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

# ABRIL 2020

ventas_productos_2020_abr=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(ventas_2020_abr[i][2] * precio_producto[i][j])
    ventas_productos_2020_abr.append([ventas_2020_abr[i][0],i+1,ventas_2020_abr[i][2],precio_producto[i][1], m])

# Loop para borrar los productos con cero ventas en el mes de abril:
ventas_promedio_2020_abr=[]
for i in ventas_productos_2020_abr:
    if i[2] != 0:
        ventas_promedio_2020_abr.append(i)
    if i[0] == '04':
        i[0]='Abril'

# Loop para sumar los productos vendidos en abril de 2020:
productos_abril_2020 = 0
for i in ventas_promedio_2020_abr:
    productos_abril_2020 += i[2]
print("Productos vendidos en abril de 2020:", productos_abril_2020)

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en abril de 2020:
ingresos_abril_2020 = 0
for i in ventas_promedio_2020_abr:
    ingresos_abril_2020 += i[4]
print("Ingresos totales percibidos en abril de 2020:", ingresos_abril_2020)
print()

# Para mostrar la lista de los productos vendidos en abril:
row_format = "{:>8} {:>8}  {:>13}  {:>16}  {:>16}"
headers_ventas = ['Mes','Producto',  'Productos vendidos', 'Precio del producto', 'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_promedio_2020_abr:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

# MAYO 2020

ventas_productos_2020_may=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(ventas_2020_may[i][2] * precio_producto[i][j])
    ventas_productos_2020_may.append([ventas_2020_may[i][0],i+1,ventas_2020_may[i][2],precio_producto[i][1], m])

# Loop para borrar los productos con cero ventas en el mes de mayo:
ventas_promedio_2020_may=[]
for i in ventas_productos_2020_may:
    if i[2] != 0:
        ventas_promedio_2020_may.append(i)
    if i[0] == '05':
        i[0]='Mayo'

# Loop para sumar los productos vendidos en mayo de 2020:
productos_mayo_2020 = 0
for i in ventas_promedio_2020_may:
    productos_mayo_2020 += i[2]
print("Productos vendidos en mayo de 2020:", productos_mayo_2020)

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en mayo de 2020:
ingresos_mayo_2020 = 0
for i in ventas_promedio_2020_may:
    ingresos_mayo_2020 += i[4]
print("Ingresos totales percibidos en mayo de 2020:", ingresos_mayo_2020)
print()

# Para mostrar la lista de los productos vendidos en mayo:
row_format = "{:>8} {:>8}  {:>13}  {:>16}  {:>16}"
headers_ventas = ['Mes','Producto',  'Productos vendidos', 'Precio del producto', 'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_promedio_2020_may:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

# JUNIO 2020

ventas_productos_2020_jun=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(ventas_2020_jun[i][2] * precio_producto[i][j])
    ventas_productos_2020_jun.append([ventas_2020_jun[i][0],i+1,ventas_2020_jun[i][2],precio_producto[i][1], m])

# Loop para borrar los productos con cero ventas en el mes de junio:
ventas_promedio_2020_jun=[]
for i in ventas_productos_2020_jun:
    if i[2] != 0:
        ventas_promedio_2020_jun.append(i)
    if i[0] == '06':
        i[0]='Junio'

# Loop para sumar los productos vendidos en junio de 2020:
productos_junio_2020 = 0
for i in ventas_promedio_2020_jun:
    productos_junio_2020 += i[2]
print("Productos vendidos en junio de 2020:", productos_junio_2020)

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en junio de 2020:
ingresos_junio_2020 = 0
for i in ventas_promedio_2020_jun:
    ingresos_junio_2020 += i[4]
print("Ingresos totales percibidos en junio de 2020:", ingresos_junio_2020)
print()

# Para mostrar la lista de los productos vendidos en junio:
row_format = "{:>8} {:>8}  {:>13}  {:>16}  {:>16}"
headers_ventas = ['Mes','Producto',  'Productos vendidos', 'Precio del producto', 'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_promedio_2020_jun:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

# JULIO 2020

ventas_productos_2020_jul=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(ventas_2020_jul[i][2] * precio_producto[i][j])
    ventas_productos_2020_jul.append([ventas_2020_jul[i][0],i+1,ventas_2020_jul[i][2],precio_producto[i][1], m])

# Loop para borrar los productos con cero ventas en el mes de julio:
ventas_promedio_2020_jul=[]
for i in ventas_productos_2020_jul:
    if i[2] != 0:
        ventas_promedio_2020_jul.append(i)
    if i[0] == '07':
        i[0]='Julio'

# Loop para sumar los productos vendidos en julio de 2020:
productos_julio_2020 = 0
for i in ventas_promedio_2020_jul:
    productos_julio_2020 += i[2]
print("Productos vendidos en julio de 2020:", productos_julio_2020)

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en julio de 2020:
ingresos_julio_2020 = 0
for i in ventas_promedio_2020_jul:
    ingresos_julio_2020 += i[4]
print("Ingresos totales percibidos en julio de 2020:", ingresos_julio_2020)
print()

# Para mostrar la lista de los productos vendidos en el mes de julio:
row_format = "{:>8} {:>8}  {:>13}  {:>16}  {:>16}"
headers_ventas = ['Mes','Producto',  'Productos vendidos', 'Precio del producto', 'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_promedio_2020_jul:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

# AGOSTO 2020

ventas_productos_2020_ago=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(ventas_2020_ago[i][2] * precio_producto[i][j])
    ventas_productos_2020_ago.append([ventas_2020_ago[i][0],i+1,ventas_2020_ago[i][2],precio_producto[i][1], m])

# Loop para borrar los productos con cero ventas en el mes de agosto:
ventas_promedio_2020_ago=[]
for i in ventas_productos_2020_ago:
    if i[2] != 0:
        ventas_promedio_2020_ago.append(i)
    if i[0] == '08':
        i[0]='Agosto'

# Loop para sumar los productos vendidos en el mes de agosto:
productos_agosto_2020 = 0
for i in ventas_promedio_2020_ago:
    productos_agosto_2020 += i[2]
print("Productos vendidos en agosto de 2020:", productos_agosto_2020)

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en agosto de 2020:
ingresos_agosto_2020 = 0
for i in ventas_promedio_2020_ago:
    ingresos_agosto_2020 += i[4]
print("Ingresos totales percibidos en agosto de 2020:", ingresos_agosto_2020)
print()

# Para mostrar la lista de los productos vendidos en el mes de agosto:
row_format = "{:>8} {:>8}  {:>13}  {:>16}  {:>16}"
headers_ventas = ['Mes','Producto',  'Productos vendidos', 'Precio del producto', 'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_promedio_2020_ago:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

# SEPTIEMBRE 2020

# Loop para eliminar las listas repetidas:
lista_nueva = []
for i in ventas_2020_sep:
    if i not in lista_nueva:
         lista_nueva.append(i)

ventas_2020_sep=lista_nueva

ventas_productos_2020_sep=[]

for i in range(len(precio_producto)):
    m = 0
    for j in range(2):
        m=(ventas_2020_sep[i][2] * precio_producto[i][j])
    ventas_productos_2020_sep.append([ventas_2020_sep[i][0],i+1,ventas_2020_sep[i][2],precio_producto[i][1], m])

# Loop para borrar los productos con cero ventas en el mes de septiembre:
ventas_promedio_2020_sep=[]
for i in ventas_productos_2020_sep:
    if i[2] != 0:
        ventas_promedio_2020_sep.append(i)
    if i[0] == '09':
        i[0]='Septiembre'

# Loop para sumar los productos vendidos en el mes de septiembre:
productos_septiembre_2020 = 0
for i in ventas_promedio_2020_sep:
    productos_septiembre_2020 += i[2]
print("Productos vendidos en septiembre de 2020:", productos_septiembre_2020)

# Loop para sumar los ingresos por productos vendidos y obtener el ingreo total en septiembre de 2020:
ingresos_septiembre_2020 = 0
for i in ventas_promedio_2020_sep:
    ingresos_septiembre_2020 += i[4]
print("Ingresos totales percibidos en septiembrede 2020:", ingresos_septiembre_2020)
print()

# Para mostrar la lista de los productos vendidos en septiembre:
row_format = "{:>8} {:>8}  {:>13}  {:>16}  {:>16}"
headers_ventas = ['Mes','Producto',  'Productos vendidos', 'Precio del producto', 'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_promedio_2020_sep:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

# OCTUBRE 2020
print("Octubre: sin ventas \n")

# NOVIEMBRE 2020

print("Noviembre: sin ventas \n")

# DICIEMBRE 2020
print("Diciembre: sin ventas \n")

productos_vendidos_2020=productos_enero_2020+productos_febrero_2020+productos_marzo_2020\
                        +productos_abril_2020+productos_mayo_2020+productos_junio_2020\
                        +productos_julio_2020+productos_agosto_2020+productos_septiembre_2020

print("Productos totales vendidos en 2020: ", productos_vendidos_2020)

ingresos_totales_2020=ingresos_enero_2020+ingresos_febrero_2020+ingresos_marzo_2020\
                        +ingresos_abril_2020+ingresos_mayo_2020+ingresos_junio_2020\
                        +ingresos_julio_2020+ingresos_agosto_2020+ingresos_septiembre_2020

print("Ingresos totales percibidos en 2020: ", ingresos_totales_2020)
print()

#--------------------------------------------------------------#

print("e) Meses con mayores ventas \n")

# Se crea una lista con las ventas y los ingresos por mes:
ventas_ing_men_2020=[['Enero',productos_enero_2020,ingresos_enero_2020],
                      ['Febrero',productos_febrero_2020,ingresos_febrero_2020],
                      ['Marzo',productos_marzo_2020,ingresos_marzo_2020],
                      ['Abril', productos_abril_2020, ingresos_abril_2020],
                      ['Mayo', productos_mayo_2020,ingresos_mayo_2020],
                      ['Junio',productos_junio_2020,ingresos_junio_2020],
                      ['Julio',productos_julio_2020,ingresos_julio_2020],
                      ['Agosto',productos_agosto_2020,ingresos_agosto_2020],
                      ['Septiembre',productos_septiembre_2020,ingresos_septiembre_2020],
                      ['Octubre', 0, 0],
                      ['Noviembre',0,0],
                      ['Diciembre', 0, 0]]

# Loop para ordenar las ventas de menor a mayor:
l = len(ventas_ing_men_2020)
for i in range(0, l):
    for j in range(0, l-i-1):
        if (ventas_ing_men_2020[j][2] < ventas_ing_men_2020[j + 1][2]):
            tempo = ventas_ing_men_2020[j]
            ventas_ing_men_2020[j]= ventas_ing_men_2020[j + 1]
            ventas_ing_men_2020[j + 1]= tempo

# Para mostrar la lista de los productos vendidos:
row_format = "{:>10} {:>15}  {:>15} "
headers_ventas = ['Mes','Productos vendidos', 'Ingresos por producto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in ventas_ing_men_2020:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

#--------------------------------------------------------------#

print("f) Devoluciones: \n")

# Loop para extraer los productos vendidos en lifestore_sales:
id_producto=[]
for producto in lifestore_sales:
  id_producto.append([producto[1],producto[3][3:5],producto[3][6:10],producto[4]])

productos_devueltos=[]
for i in id_producto:
    if i[3] != 0:
        productos_devueltos.append(i)

# Para mostrar la lista de los productos devueltos:
row_format = "{:>10} {:>10} {:>15}  {:>15} "
headers_ventas = ['Producto devuelto','Mes', 'Año', '1=devuelto']
header_row = row_format.format(*headers_ventas)
print("." * (len(header_row) + 1))
print(header_row)
print("." * (len(header_row) + 1))
for i in productos_devueltos:
    print(row_format.format(*i))
print("." * (len(header_row) + 1))
print()

# THE END
