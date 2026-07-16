def validar_libros():
    while True:
        num_libros = input("ingrese la cantidad de libros a agregar")
        if num_libros.isdecimal():
            num_libros = int(num_libros)
            if num_libros == 0:
                print("cantidad de libros debe ser > a 0, intente de nuevo")
                continue            
        else:
            print("ingrese numero de libros a agregar, no texto")
            continue
        return num_libros

validacion= validar_libros()
print(validacion)