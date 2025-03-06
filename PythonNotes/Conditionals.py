

## Condicional simple


salary = 3300000

if salary < 2600000:
    print(f"recibe aux de transporte{200000}")

## Condicional Compuesto 

employee_salary = int(input("Ingrese el salario a validar"))

if employee_salary < 2600000:
    employee_salary += 200000
    print(employee_salary)
else:
    print(employee_salary) 

## Condicional anidado


userType = int( input("Escriba su tipo"))

if userType == 1:
    print("Administrativo")
elif userType == 2:
    print("Profesor")
elif userType == 3:
    print("Estudiante")
elif userType == 4:
    print("Servicios")
else:
    print("Visitante")   


##Selector multiple en python se conoce como match y solo es para versiones recientes


select = int(input("Opcion"))

match select:
    case 1:
        print("Hotel")
    case 2:
        print("Taxi")
    case _: 
        print("No require servicio")
        

    
                 
