libro_inventario = {
    1: {"nombre": "papita"},
    2: {"nombre": "lechugita"},
    3: {"nombre": "tomatito"}
}

def ingreso_libro_nuevo ():
    while True:
        nombre = input("ingrese nombre de libro: ").capitalize
        if nombre == "salir":
            print("saliendo")
            break
            #este es el que destruye al bucle while
        for num_lib,tit_lib in libro_inventario.items():
            print(num_lib,tit_lib)
            
            if tit_lib["nombre"] == nombre:
                print("libro se encuentra en la lista")
                #buscas aca el nombre, ubicas que en clave-valor, tit_lib es el que contiene
                #{"nombre": "papita"}, pero no puedes solo buscar tit_lib == nombre ya que compara
                #{"nombre": "papita"} == "nombre", por lo que debes colocar tit_lib["nombre"] que
                #indica que buscas el valor, en este caso "papita" == "papita"
                break
            #break de aca corta solo el bucle for
        else:
            codigo = input("ingrese codigo: ")
            genero = input("ingrese genero: ")
            autor = input("ingrese autor: ")
            libro_inventario[codigo] ={
                "nombre": nombre,
                "genero": genero,
                "autor": autor

                }
            print(f"el libro es {nombre} con codigo {codigo}")

def modificar_libro_existente():
    while True:
        cambiar_datos = input("ingrese libro a cambiar datos:")
        for codigo_libro, nombre_libro in libro_inventario.items():
            print(codigo_libro, nombre_libro )
            if cambiar_datos == nombre_libro["nombre"]:
                print(f"{cambiar_datos} se encuentra en la lista")
                while True:
                    print("""
                1.Cambiar nombre
                2.Cambiar genero
                3.Cambiar autor
                        """)
                    
            else:
                print(f"libro {cambiar_datos} no se encuentra registrado para modificar")
                break
        else:
            return cambiar_datos          

def busqueda_libro_existente():
    buscar_libro_lista = input("ingrese nombre de libro a buscar")
    for codigo_libro, nombre_libro in libro_inventario.items():
        if buscar_libro_lista == nombre_libro["nombre"]:
            print(f"libro {nombre_libro['nombre']} con codigo {codigo_libro} se encuentra en la lista")
            break
    else:
        print("libro no se encuentra disponible")

