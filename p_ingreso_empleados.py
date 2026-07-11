empleado = []
sueldo = tuple()
trabajos = set()




while True:
    print("""
                |###########################|
                |###########################|
                |--<Bienvenido a programa>--|
                |###########################|
                |###########################|


    1.Administrar empleados
    2.Buscar empleado
    3.Calcular sueldo
    4.Salir

    """)
    opcion = input("elija una opcion del menu:")
    if opcion == "1":
        while True:
            print("""
            1.Agregar empleado
            2.Eliminar empleado
            3.Lista de empleados
            4.Volver             
            """)
            opcion = input("elija una opcion del menu:")
            if opcion == "1":
                agregar_empleado = input("ingrese empleado a agregar:")
            elif opcion == "2":
                eliminar_empleado = input("ingrese empleado a eliminar:")
            elif opcion == "3":
                print("lista de empleados")
            #   for i in empleado
            elif opcion == "4":
                print("volviendo a menu principal")
                break
    elif opcion == "2":
        print("buscando empleado")        
    elif opcion == "3":
        print("calculando sueldo")
        #pendiente, probablemente no haga respecto a empleados sino inventario
        #no encuentro razon de calcular sueldo, a menos que agregue labores o acciones
        #o bonos que se dan a trabajadores que cumplen, asi que podria hacer condiciones
        #e ir añadiendo bonos basado en eso
    elif opcion == "4":
        print("Cerrando programa")
        break
    