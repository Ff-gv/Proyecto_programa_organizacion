libro_inventario = {
    1: {"nombre": "papita"},
    2: {"nombre": "lechugita"},
    3: {"nombre": "tomatito"}
}

def modificar_datos_libro():
    cambiar_datos = input("ingrese libro a cambiar datos:")
    while True:
        for codigo_libro, nombre_libro in libro_inventario.items():
            print(codigo_libro, nombre_libro )
            if cambiar_datos == nombre_libro["nombre"]:
                print(f"{cambiar_datos} se encuentra en la lista")
                continue
            else:
                print(f"libro {cambiar_datos} no se encuentra registrado para modificar")
                break
        else:
            

def busqueda_libro_existente ():
    while True:
        nombre = input("ingrese nombre de libro: ")
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
                #{"nombre": "papita"} == nombre, por lo que debes colocar tit_lib["nombre"] que
                #indica que buscas el valor, en este caso "papita" == "papita"
                break
            #break de aca corta solo el bucle for
        else:
            codigo = input("ingrese codigo: ")
            genero = input("ingrese genero: ")
            libro_inventario[codigo] ={
                "nombre": nombre,
                "genero": genero

                }
            print(f"el libro es {nombre} con codigo {codigo}")
        

busqueda_libro_existente()
for codigo_libro, nombre_libro in libro_inventario.items():
    print(codigo_libro,nombre_libro)


                 
