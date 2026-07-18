
def verificar_cantidad_libro(cantidad_libros):
        if not cantidad_libros.isdecimal() or cantidad_libros == 0:
            print(f"la cantidad {cantidad_libros} no es valida")
            return
        else:
            print("correcto")

#def agregar_libro():
cantidad_libros = input("escriba la cantidad a ingresar --> ")    
verificar_cantidad_libro(cantidad_libros)
            
        