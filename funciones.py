libro_inventario = {
}
iva_constante = (1.19,0.19)
#tiene que ser asi y no como tuple, no lo deja funcionar bien
clientes = set()
compra = []
def verificar_cantidad_entero():
    while True:
        numero = input(f"ingrese una cantidad, escriba salir para terminar: ").lower()
        if numero == "salir":
            return "salir"
        if not numero.isdecimal():
            print(f"la cantidad {numero} no es valida")
            continue
        else:
            numero = int(numero)
            if numero == 0:
                print("numero no puede ser 0")
                continue
            return numero
        
def valor_unitario_total():  
        print("ingrese el valor unitario del producto")
        valor_unitario = verificar_cantidad_entero()
        return valor_unitario
    
def ingreso_libro_nuevo ():
    while True:
        nombre = input("ingrese nombre de libro, escriba salir para terminar: ").lower()
        if nombre == "":
                print("no puede ser un espacio vacio")
                continue
        if nombre == "salir":
            print("saliendo")
            break
            #este es el que destruye al bucle while
        for codigo_libro, diccionario_libro in libro_inventario.items():
            print(codigo_libro, diccionario_libro)
            if diccionario_libro["nombre"] == nombre:
                print("libro ya se encuentra en la lista")
                #buscas aca el nombre, ubicas que en clave-valor, tit_lib es el que contiene
                #{"nombre": "papita"}, pero no puedes solo buscar tit_lib == nombre ya que compara
                #{"nombre": "papita"} == "nombre", por lo que debes colocar tit_lib["nombre"] que
                #indica que buscas el valor, en este caso "papita" == "papita"
                #si no tiene "" se interpreta como una variable
                break
            #break de aca corta solo el bucle for y lo reinicia
        else:
            codigo = input("ingrese codigo: ")
            genero = input("ingrese genero: ").lower()
            autor = input("ingrese autor: ").lower()
            print("ingrese el valor unitario")
            valor_unitario = verificar_cantidad_entero()
            print("ingrese cantidad de copias")
            stock = verificar_cantidad_entero()
            if valor_unitario == "salir" or stock == "salir":
                print("se termina el ingreso de valores numericos")
                return

            # funcion valor unitario + valor total combinado con numero postivo
            libro_inventario[codigo] ={
                "nombre": nombre,
                "genero": genero,
                "autor": autor,
                "valor unitario":valor_unitario,
                "valor total con IVA":valor_unitario * iva_constante[0] * stock ,
                "stock": stock
                        }
            print(f"el libro ingresado satisfactoriamente es {nombre} con codigo {codigo}, autor {autor}, y son {stock} copias")
    return libro_inventario
        
def modificar_libro_existente():
    while True:
        cambiar_datos = input("ingrese libro a cambiar datos:")
        if len(libro_inventario) == 0:
            print("Error: No existen libros ingresados actualmente en el inventario.")
            return 1
        for codigo_libro, diccionario_libro in libro_inventario.items():
            print(codigo_libro, diccionario_libro )
            if cambiar_datos == diccionario_libro["nombre"]:
                print(f"{cambiar_datos} se encuentra en la lista")
                return codigo_libro                 
        else:
            print(f"libro {cambiar_datos} no se encuentra registrado para modificar")
            return 1    
        
def editar_codigo():
    codigo_anterior = modificar_libro_existente()
    if codigo_anterior == 1:
        return
    nuevo = input("ingresar nuevo codigo: ")
    libro_inventario[nuevo] = libro_inventario[codigo_anterior]
    del libro_inventario[codigo_anterior]
            #update solo sirve con valores, no con claves
            #no se puede cambiar tamaño de diccionario dentro de bucle for
    
def editar_entrada(clave):
    codigo_libro = modificar_libro_existente()
    if codigo_libro == 1:
        return
    nuevo = input(f"ingrese nuevo {clave}: ")
    libro_inventario[codigo_libro].update({clave: nuevo})
    print(f"valor {nuevo} se cambió satisfactoriamente")
    

def editar_valor_unitario():
    codigo_libro = modificar_libro_existente()
    if codigo_libro == 1:
        return
    print(f"ingrese nuevo valor unitario")
    nuevo = verificar_cantidad_entero()
    if nuevo == "salir":
                print("se termina el ingreso de valores numericos")
                return
    libro_inventario[codigo_libro].update({"valor unitario": nuevo})
    libro_inventario[codigo_libro].update({"valor total con IVA": nuevo * iva_constante[0] * libro_inventario[codigo_libro]["stock"] })
            #llamo diccionario_libro["stock"], recuerda que diccionario_libro representa un diccionario anidado dentor
            #de libro inventario, por lo que estoy buscando el valor de la clave stock dentro del diccionario
            #llamaod diccionario_libro
    print(f"valor {nuevo} se cambió satisfactoriamente")
def editar_copias():
    codigo_libro = modificar_libro_existente()
    if codigo_libro == 1:
        return
    print("ingrese nueva cantidad de stock")
    nuevo = verificar_cantidad_entero()
    if nuevo == "salir":
                print("se termina el ingreso de valores numericos")
                return
    libro_inventario[codigo_libro].update({"stock": nuevo})
    libro_inventario[codigo_libro].update({"valor total con IVA": nuevo * iva_constante[0] * libro_inventario[codigo_libro]["valor unitario"] })
    print(f"el stock fue correctamente cambiado a {nuevo}")

def eliminar_libro():
    codigo_libro = modificar_libro_existente()
    if codigo_libro == 1:
        return
    confirmacion = input(f"ESTA SEGURO QUE DESEA ELIMINAR ENTRADA{codigo_libro}?\n ESCRIBA SI PARA CONFIRMAR, PULSE CUALQUIER OTRA TECLA PARA SALIR").lower()
    if confirmacion == "si":
        nombre_borrado = libro_inventario[codigo_libro]['nombre']
        del libro_inventario[codigo_libro]
        print(f"libro {nombre_borrado} con codigo {codigo_libro} ha sido eliminado de forma satisfactoria")
    pass

def busqueda_libro_existente():
    buscar_libro_lista = input("ingrese nombre de libro a buscar")
    for codigo_libro, nombre_libro in libro_inventario.items():
        if buscar_libro_lista == nombre_libro["nombre"]:
            print(f"libro {nombre_libro['nombre']} con codigo {codigo_libro} se encuentra en la lista")
            break
    else:
        print("libro no se encuentra disponible")

def listar_libros():
    contador = 1
    if len(libro_inventario) == 0:
            print("Error: No existen libros ingresados actualmente en el inventario.")
            return
    for clave,valor in libro_inventario.items():
        print(f" |{contador}-> CÓDIGO: {clave} || LIBRO: {valor['nombre'].upper()}")
        print(f" |Género: {valor['genero'].capitalize()}")
        print(f" |Autor: {valor['autor'].capitalize()}")
        print(f" |Stock: {valor['stock']} copias")
        print(f" |Precio Unitario: ${valor['valor unitario']}")
        #recordar que se deben usar comillas, no doble comillas para poder
        #escribir una direccion de un diccionario, en este caso se busca el valor de un diccionario
        #anidado dentro de libro_inventario, este esta desigando como valor y se escribe el nombre
        #de su categoria par buscar el valor necesario, se anota con ''
        contador += 1 
def registro_clientes():
    pass
def compra_libros():
    while True:
        for clave, valor in libro_inventario.items():
            print(f"-{clave}--{valor['nombre'].upper()}--{valor['valor unitario']}--{valor['stock']}")
        else:
            ingreso_compra = input("ingrese codigo de libro a comprar, escriba 1 para terminar: ")
            if ingreso_compra == "1":
                if len(compra) > 0:
                #en realidad aca podria hacer un f-string y ordenar la lista de compras
                    print(compra)
                    return compra
                else:
                    print("no hay productos registrados")
                    return 
            if ingreso_compra == clave:
                compra.append(ingreso_compra)
                print
            else:
                print("libro no se encuentra en el inventario disponible!")
                break
