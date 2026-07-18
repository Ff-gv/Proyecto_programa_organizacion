def menu_libros():
    while True:
            print("""
            1.Agregar libros
            2.Eliminar libros
            3.Lista de libros
            4.Actualizar datos de libros       
            5.Volver             
            """)
            opcion = input("elija una opcion del menu:")
            if opcion == "1":
                
            elif opcion == "2":
                
            elif opcion == "3":

            elif opcion == "4":
                  
            elif opcion == "5":
                  break
            else:
                  print("ingrese una opcion nuevamente: ")

def menu_principal():
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
            menu_libros()
        elif opcion == "2":
            