import os
import sys

def limpiarConsola():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si la Maquinna esta corriendo en windows, usar cls
        command = 'cls'
    os.system(command)

limpiarConsola()

opcionElegida = 0
usuariosRegistrados = {}

## clase usuario
class Usuario:
    def __init__(self,usuario,contraseña,rol,Nombre,CURP,ciudad) -> None:
        self._usuario = usuario
        self._contraseña = contraseña
        self._rol = rol
        self._Nombre = Nombre
        self._CURP = CURP
        self._ciudad = ciudad

def mostrarMenu():
    print("\n------------MENU-------------- \n" +
        "     1. Registro \n" +
        "     2. Inicio de sesión \n" + 
        "     3. Salida \n" + 
        "------------------------------ \n")
    opcionElegida = int(input("Ingrese la opcion a elegir: "))
    limpiarConsola()
    return opcionElegida
opcionElegida = mostrarMenu()


##CREAMOS EL USUARIO ADMINISTRADOR 
administrador = Usuario("admin","admin","administrador","Aldo",'1', "Nuevo Laredo")
usuariosRegistrados.update({administrador._CURP:administrador})
##--------------------------------------------------------------------------------------


def mostrarOpcion(opcionElegida):
    if opcionElegida == 1:
        print("\n-----------REGISTRO DE USUARIO-----------")
        nuevoUsuario = Usuario(input("Ingrese el correo del usuario nuevo: "),
                            input("Ingrese la contaseña del usuario nuevo: "),
                            "cliente",
                            input("Ingrese el nombre del usuario nuevo: "),
                            input("Ingrese el CURP del usuario nuevo: "), 
                            input("Ingrese la ciudad del usuario nuevo: "))
    
        print("------------------------------------------ \n")

        bandera = 0
        for u in usuariosRegistrados:
            if usuariosRegistrados[u]._CURP == nuevoUsuario._CURP:
                print("El usuario ya existe")
                bandera = 1
        if bandera != 1:
            usuariosRegistrados.update({nuevoUsuario._CURP:nuevoUsuario})
            print("SE HA AGREADO EL NUEVO USUARIO! \n")
            bandera = 0
        mostrarOpcion(mostrarMenu())

    if opcionElegida == 2:
        nusuario = ""
        ncontraseña = ""
        nrol = ""
        nNombre = ""
        nCURP = ""
        nciudad = ""

        print("\n------------INICIO DE SESION-----------")
        nusuario = input("Ingrese el correo del usuario: ")
        ncontraseña = input("Ingrese la contraseña del usuario: ")

        usuario = Usuario(nusuario,ncontraseña,nrol,nNombre,nCURP,nciudad)

        print("--------------------------------------- \n")

        for u in usuariosRegistrados:
            if usuariosRegistrados[u]._usuario == usuario._usuario:
                usuarioContraseña = usuariosRegistrados[u]
                if usuarioContraseña._contraseña == usuario._contraseña:
                    print("------INICIO DE SESION EXITOSO!------ \n" + 
                        "Usuario: " + usuariosRegistrados[u]._usuario +  "\n" +
                        "Contraseña: " + usuariosRegistrados[u]._contraseña +  "\n" +
                        "ROL: " + usuariosRegistrados[u]._rol +  "\n" +
                        "Nombre: " + usuariosRegistrados[u]._Nombre +  "\n" +
                        "CURP: " + usuariosRegistrados[u]._CURP +  "\n" +
                        "Ciudad: " + usuariosRegistrados[u]._ciudad +  "\n" +
                        "-----------------------------------\n")
                    if usuarioContraseña._rol == 'administrador':
                        print("--------USUARIOS REGISTRADOS-------")
                        for u in usuariosRegistrados:
                            print("Usuario: " + usuariosRegistrados[u]._usuario +  "\n" +
                                "Contraseña: " + usuariosRegistrados[u]._contraseña +  "\n" +
                                "ROL: " + usuariosRegistrados[u]._rol +  "\n" +
                                "Nombre: " + usuariosRegistrados[u]._Nombre +  "\n" +
                                "CURP: " + usuariosRegistrados[u]._CURP +  "\n" +
                                "Ciudad: " + usuariosRegistrados[u]._ciudad +  "\n" +
                                "--------------------------------------")
                else:
                    print("Datos incorrectos :c")
        mostrarOpcion(mostrarMenu())

    if opcionElegida == 3:
        print("FIN DEL PROGRAMA...")
        sys.exit()

    if opcionElegida != 1 and opcionElegida != 2 and opcionElegida != 3:
        print("La opción elegida es invalida!!! \n")
        mostrarOpcion(opcionElegida)

    mostrarMenu()

mostrarOpcion(opcionElegida)
