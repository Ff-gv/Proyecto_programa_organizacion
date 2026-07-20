from menu import *
from funciones import *
def main():
    if login() == 0:
        return
    while True:
        menu()
        opcion = input("ingrese una opcion del menu ->")
        if opcion == "1":
            while True:
                menu_libros()
                opcion = input("ingrese una opcion del menu ->")
                if opcion == "1":
                    ingreso_libro_nuevo()
                elif opcion == "2":
                    eliminar_libro()
                elif opcion == "3":
                    while True:
                        menu_editar_libro()
                        opcion = input("ingrese una opcion del menu ->")
                        if opcion == "1":
                            editar_codigo()
                        elif opcion == "2":
                            editar_entrada("genero")
                        elif opcion == "3":
                            editar_entrada("autor")
                        elif opcion == "4":
                            editar_copias()
                        elif opcion == "5":
                            editar_valor_unitario()
                        elif opcion == "6":
                            print("volver al menu principal")
                            break
                        else:
                            print("ingrese una opcion valida")
                elif opcion == "4":
                    listar_libros()
                elif opcion == "5":
                    print("volver al menu principal")
                    break
                else:
                    print("ingrese una opcion valida")
        elif opcion == "2":
            compra_libros()
        elif opcion == "3":
                lista_clientes()
        elif opcion == "4":
            print("Cerrando programa")
            break
        else:
            print("ingrese una opcion valida")

if __name__ == "__main__":
    main()      