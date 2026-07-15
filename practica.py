libro_inventario = {1:"papita",2:"tomatito",3:"lechugota"}

def validar_libro():
    while True:
        nombre = input("ingrese nombre del libro").lower()
        for num,libros in libro_inventario.items():
            
            if libros == nombre:
                print(f"el libro {nombre} se encuentra en el sistema")
                break
            elif nombre not in libros:
                print("el libro no existe")
                agregar_libro = input("ingrese el nombre del libro")
                print(num,libros)
                continue
            elif nombre == "salir":
                print("se ha terminado el ingreso de nombres de libros")
                break
            return agregar_libro
    
validar_libro()

if num_libros == 0:
                    print("cantidad de libros debe ser > a 0, intente de nuevo")
            else:
                for rotacion in range(num_libros):
                    while True:
                        print(f"{rotacion + 1} de {num_libros}libros")
                        nombre = input("ingrese nombre del libro:").capitalize()
                        if nombre in libro_inventario:
                            print("ya se encuentra disponible")