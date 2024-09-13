class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]  # Inicializamos con listas vacías para encadenamiento

    def funcion_hash(self, clave):
        # Función hash simple: suma de valores ASCII de los caracteres
        suma_ascii = sum(ord(c) for c in clave)
        return suma_ascii % self.tamano  # Calcula el índice

    def insertar(self, clave):
        indice = self.funcion_hash(clave)
        if clave not in self.tabla[indice]:
            self.tabla[indice].append(clave)  # Insertar en la lista correspondiente
            return True
        return False

    def existe(self, clave):
        indice = self.funcion_hash(clave)
        return clave in self.tabla[indice]  # Verificar si la clave está en la lista

    def buscar(self, clave):
        if self.existe(clave):
            return f"'{clave}' encontrado."
        return f"'{clave}' no encontrado."

# Función para eliminar duplicados usando la TablaHash manual
def eliminar_duplicados(correos, tabla_hash):
    lista_sin_duplicados = []  # Lista para almacenar los correos sin duplicados
    
    for correo in correos:
        if tabla_hash.insertar(correo):  # Insertar y verificar si fue añadido
            lista_sin_duplicados.append(correo)  # Lo agregamos a la lista sin duplicados
    
    return lista_sin_duplicados

# Correos electrónicos predefinidos en el código (20 correos)
correos = [
    "john.doe@example.com", 
    "jane.smith@example.com", 
    "john.doe@example.com", 
    "alice.jones@example.com",
    "bob.brown@example.com",
    "jane.smith@example.com",
    "lucas.white@example.com",
    "maria.santos@example.com",
    "peter.parker@example.com",
    "tony.stark@example.com",
    "bruce.wayne@example.com",
    "clark.kent@example.com",
    "diana.prince@example.com",
    "bruce.banner@example.com",
    "natasha.romanoff@example.com",
    "thor.odinson@example.com",
    "steve.rogers@example.com",
    "wanda.maximoff@example.com",
    "vision.avenger@example.com",
    "scott.lang@example.com"
]

# Función del menú
def menu():
    tabla_hash = TablaHash(20)  # Crear la tabla hash
    correos_sin_duplicados = eliminar_duplicados(correos, tabla_hash)  # Insertar correos al inicio

    while True:
        print("\n----- Menú -----")
        print("1. Mostrar correos sin duplicados")
        print("2. Buscar correo")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Mostrar correos sin duplicados
            print("Correos sin duplicados:")
            for i, correo in enumerate(correos_sin_duplicados, 1):
                print(f"{i}. {correo}")
        elif opcion == "2":
            correo_a_buscar = input("Ingrese el correo electrónico a buscar: ")
            resultado = tabla_hash.buscar(correo_a_buscar)
            print(resultado)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Ejecutar el menú
menu()
