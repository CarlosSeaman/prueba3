import random

# Lista para almacenar los datos de las personas
personas = []

def grabar_persona():
    dni = input("Ingrese el número de DNI: ")
    while len(dni) != 8 or not dni.isdigit():
        dni = input("DNI inválido. Ingrese nuevamente: ")
    
    nombre = input("Ingrese el nombre: ")
    while len(nombre) < 8:
        nombre = input("Nombre inválido. Ingrese nuevamente: ")
    
    edad = int(input("Ingrese la edad: "))
    while edad < 0:
        edad = int(input("Edad inválida. Ingrese nuevamente: "))
    
    pais = input("Ingrese el país de nacimiento: ")
    ciudad = input("Ingrese la ciudad de nacimiento: ")
    
    persona = {"DNI": dni, "Nombre": nombre, "Edad": edad, "País de Nacimiento": pais, "Ciudad de Nacimiento": ciudad}
    personas.append(persona)
    
    print("Datos de la persona grabados exitosamente.\n")

def buscar_persona():
    dni = input("Ingrese el número de DNI: ")
    
    for persona in personas:
        if persona["DNI"] == dni:
            print("Información de la persona:")
            print(f"DNI: {persona['DNI']}")
            print(f"Nombre: {persona['Nombre']}")
            print(f"Edad: {persona['Edad']}")
            print(f"País de Nacimiento: {persona['País de Nacimiento']}")
            print(f"Ciudad de Nacimiento: {persona['Ciudad de Nacimiento']}")
            if persona['País de Nacimiento'].lower() == 'argentina':
                print("La persona pertenece al país de Argentina.")
            else:
                print("La persona no pertenece al país de Argentina.")
            return
    
    print("No se encontró ninguna persona con ese DNI.\n")

def imprimir_certificados():
    certificados = ["Certificado de Nacimiento", "Certificado de Estado Conyugal", "Certificado de Pertenencia a Argentina"]
    
    for persona in personas:
        certificado = random.choice(certificados)
        print(f"Certificado: {certificado}")
        print(f"DNI: {persona['DNI']}")
        print(f"Nombre: {persona['Nombre']}")
        print(f"Datos de la persona: {persona}\n")

def eliminar_persona():
    dni = input("Ingrese el número de DNI de la persona a eliminar: ")
    
    for persona in personas:
        if persona["DNI"] == dni:
            personas.remove(persona)
            print("La persona ha sido eliminada.\n")
            return
    
    print("No se encontró ninguna persona con ese DNI.\n")

def generar_rut():
   
    digitos = random.randint(10000000, 99999999)
    rut = str(digitos)
    multiplicadores = [2, 3, 4, 5, 6, 7, 2, 3]
    suma = 0
    for i in range(8):
        suma += int(rut[i]) * multiplicadores[i]
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = "K"
    
    
    rut = rut[:2] + "." + rut[2:5] + "." + rut[5:] + "-" + str(dv)
    print(rut)
    return 
    
    


    

def main():
    print("Bienvenido al sistema de autoservicio de RENAPER")
    
    while True:
        print("Menú:")
        print("1. Grabar datos de una persona")
        print("2. Buscar persona por DNI")
        print("3. Imprimir certificados")
        print("4. Eliminar persona")
        print("5. Renovar rut extranjero")
        print("6. Salir")
        
        opcion = input("Ingrese el número de opción: ")
        
        if opcion == "1":
            grabar_persona()
        elif opcion == "2":
            buscar_persona()
        elif opcion == "3":
            imprimir_certificados()
        elif opcion == "4":
            eliminar_persona()
        elif opcion == "5":
            generar_rut()    
        elif opcion == "6":
            print("Gracias por utilizar el sistema de autoservicio de RENAPER")
            print("Autor: CARLOS SEAMAN")
            print("Versión del programa: 1.0")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número de opción válido.\n")

if __name__ == "__main__":
    main()
