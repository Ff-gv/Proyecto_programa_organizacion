from menu import *

while True:
    menu()
    opcion = input("ingrese una opcion del menu ->")
    if opcion == "1":
        while True:
            menu_libros()
            opcion = input("ingrese una opcion del menu ->")
            if opcion == "1":
                pass
            elif opcion == "2":
                pass
            elif opcion == "3":
                while True:
                    menu_editar_libro()
                    opcion = input("ingrese una opcion del menu ->")
                    if opcion == "1":
                        pass
                    elif opcion == "2":
                        pass
                    elif opcion == "3":
                        pass
                    elif opcion == "4":
                        pass
                    elif opcion == "5":
                        pass
                    elif opcion == "6":
                        print("volver al menu principal")
                        break
                    else:
                        print("ingrese una opcion valida")
            elif opcion == "4":
                pass
            elif opcion == "5":
                print("volver al menu principal")
                break
            else:
                print("ingrese una opcion valida")
    elif opcion == "2":
        pass
    elif opcion == "3":
        while True:
            opcion = input("ingrese una opcion del menu ->")
    elif opcion == "4":
        print("Cerrando programa")
        break
    else:
        print("ingrese una opcion valida")

        