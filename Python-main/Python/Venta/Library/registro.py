import json

# Diccionario para almacenar información de usuario y contraseña
usuarios = {}

# Cargar datos de usuarios desde un archivo JSON (si existe)
def cargar_usuarios():
    try:
        with open('usuarios.json', 'r') as archivo:
            usuarios.update(json.load(archivo))
    except FileNotFoundError:
        pass

# Guardar datos de usuarios en un archivo JSON
def guardar_usuarios():
    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo)

# Función para registrar un usuario
def registrar_usuario(usuario, passwords):
    if usuario not in usuarios:
        usuarios[usuario] = passwords
        guardar_usuarios()
        print("Registro exitoso.")
    else:
        print("El usuario ya existe.")

# Función para mostrar la información de usuarios registrados
def mostrar_usuarios():
    print("Usuarios registrados:")
    for usuario in usuarios:
        print(usuario)

# Función para realizar el inicio de sesión
def iniciar_sesion(usuario, passwords):
    if usuario in usuarios and usuarios[usuario] == passwords:
        print("Inicio de sesion exitoso bienvenido",usuario)
    else:
        print("Credenciales incorrectas.")

# Función principal del programa
def main():
    cargar_usuarios()
    
    while True:
        print("Bienvenido a nuestra pagina")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Iniciar sesion")
        print("4. Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            usuario = input("Ingresa el nombre de usuario: ")
            passwords = input("Ingresa la passwords: ")
            registrar_usuario(usuario, passwords)
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            usuario = input("Ingresa el nombre de usuario: ")
            passwords = input("Ingresa la passwords: ")
            iniciar_sesion(usuario, passwords)
        elif opcion == "4":
            guardar_usuarios()
            print("Hasta luego!")
            break
        else:
            print("Opcion invalida. Por favor, selecciona una opcion valida.")

if __name__ == "__main__":
    main()
