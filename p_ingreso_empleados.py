libro_inventario = {}
iva_constante = (1.19,0.19)
lista_compra = []
#tupla para constantes...
#quizas puedo hacer un conjunto para colocar labores no repetidas en la empresa
#probablemente podria designar un codigo de trabajador y crear distintos
#diccionarios relacionados con una clave
#puedo hacer un programa para asignar labores a un trabajador y bonos basado en ello
#quizas ahi puedo aplicar la constante de tupla
#cambio de opinion, seria mejor un programa para una libreria

def copias_valor (val1):
    while True:
        valor = input(val1)
        if valor.isdecimal():
            valor = int(valor)
        else:
            print("por favor ingresar numero")
            continue
        if valor <= 0:
            print("ingrese valor mayor a 0")
            continue
        print(f"valor {valor} aceptado")
        return valor

def sum_total(copia,valor_neto):
    sum_valor = copia * valor_neto
    return sum_valor

def validar_libro():
    while True:
        nombre = input("ingrese nombre del libro:").capitalize()
        for libritos in libro_inventario:
            
# tendria que ser que se agrege a un diccionario vacio datos del libro, como nombre, genero
                #codigo, precio. Me imagino que se puede colocar un numero clave para mostrar la cantidad de libros unicos
                #y colocar tambien dentro del diccionario o tupla interior la cantidad de copias de ese libro, ademas de sumar
                #el total de copias con el valor neto para saber cual es la ganancia bruta?
def agrega_libros():
    num_libros = input("ingrese la cantidad de libros a agregar")
    while True:
        if num_libros.isdecimal():
            num_libros = int(num_libros)
            if num_libros == 0:
                    print("cantidad de libros debe ser > a 0, intente de nuevo")
            else:
                for rotacion in range(num_libros):
                    while True:
                        print(f"{rotacion + 1} de {num_libros}libros")
                        nombre = input("ingrese nombre del libro:").capitalize()
                        if nombre in libro_inventario:
                            print("ya se encuentra disponible")
                        else:
                            genero = input("ingrese genero del libro:").capitalize()
                            autor = input("ingrese el autor").capitalize()
                            copias = copias_valor("ingrese la cantidad de copias del libro:")
                            valor_unitario = copias_valor("ingrese el valor unitario neto del libro")
                            valor_total = sum_total(copias,valor_unitario)
                        break
                    codigo_libro = len(libro_inventario) + 1
                    libro_inventario[codigo_libro] = {
                        "nombre":nombre,
                        "genero":genero,
                        "autor":autor,
                        "copias":copias,
                        "valor unitario":valor_unitario,
                        "valor total":valor_total,
                        "valor total con IVA":valor_total * iva_constante[0]
                    }
        break

                                
                            





while True:
    print("""
                |###########################|
                |###########################|
                |--<Bienvenido a programa>--|
                |###########################|
                |###########################|


    1.Entrada y salida de libros
    2.Buscar libro
    3.Comprar libro
    4.Salir

    """)
    opcion = input("elija una opcion del menu:")
    if opcion == "1":
        while True:
            print("""
            1.Agregar libros
            2.Eliminar libros
            3.Lista de libros
            4.Volver             
            """)
            opcion = input("elija una opcion del menu:")
            if opcion == "1":
                
            elif opcion == "2":
                
            elif opcion == "3":
                
            elif opcion == "4":
                print("volviendo a menu principal")
                break
    elif opcion == "2":
        print("buscando ")        
    elif opcion == "3":
        print("")
        #pendiente, probablemente no haga respecto a empleados sino inventario
        #no encuentro razon de calcular sueldo, a menos que agregue labores o acciones
        #o bonos que se dan a trabajadores que cumplen, asi que podria hacer condiciones
        #e ir añadiendo bonos basado en eso

        #voy a utilizar las funciones, mas facil trabajar con mi codigo
    elif opcion == "4":
        print("Cerrando programa")
        break
    