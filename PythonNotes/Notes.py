users = []
notes = []

def user_register():
    id= input("Registre su Cédula")
    users.append(id)
    name = input("Registre su nombre")
    users.append(name)
    mail = input("Registre su email")
    users.append(mail)
    password = input("Registre su password")
    users.append(password)
    user_type = int(input("Ingrese 1 para estudiante o 2 para profesor"))
    users.append(user_type)

    print(users)


def init_session():
    mail = input("Ingrese el email registrado")
    password = input("Ingrese su passwoard")
    if mail == employee[2] and password == employee[3]:
        return True
    else: 
        print("Valide sus credenciales")
        return False
    
def note_register():
    note_amount = int(input("Ingrese la cantidad de notas a registrar"))
    for i in range(note_amount):
        notes.append(float(input(f"Ingrese la nota {i+1}: ")))
    print(notes)
    
def notes_average():
    if len(notes) == 0:
        print("No hay notas registradas")
        return
    average = sum(notes) / len(notes)
    print(f"El promedio de las notas es: {average}")

def init_menu():
    init = int(input("Seleccione:\n 1. Registro \n 2. Inicio de Sesión \n 3. Registrar notas \n 4. Promedio de notas \n 5. Finalizar"))
    match init:
        case 1:
            print("Registro de Usuario")
            user_register()
        case 2: 
            print("Inicio de Sesion")
            init_session()
        case 3:
            print("Registra notas")
            note_register()
        case 4:
            print("Promedio de notas")
            notes_average() 
        case 5: 
            print("Finalizar")
            init = 0
            return 0
        case _: 
            print("Seleccione una opción valida")  

def program():
    init_program = int(input("Presione 1 para iniciar el programa "))
    while init_program != 0:
        init_program = init_menu()

program()