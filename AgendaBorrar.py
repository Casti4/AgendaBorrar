#OPCION BORRAR
def borrar_Rafa(nombre, agenda):
        nombre = input("Nombre del contacto a borrar:")    
        if nombre in agenda:
            opcion = input("Pulsa 's' si quieres borrarlo! Otra tecla para continuar.")
            if opcion == "s":
                del agenda[nombre]
        else:
            print("No existe el contacto")