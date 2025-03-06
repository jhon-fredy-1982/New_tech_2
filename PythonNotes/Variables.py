print("Hola Mundo")

#This is a comment

# Tipos de variables que se usan en python 

#Cadena 

text = "Esto es una cadena de caracteres"

print(type(text))

userName: str = "Laura" 

# Aunque python es de tipado dinamico , nosotros podemos tiparlo

text = 1

print(type(text))

userName: str = "1"

print(type(userName))

age = 26 # Entero
celciusDegree = 23.4 #float
married = True #Boolean

##Listas, Tuplas , Diccionarios y los conjuntos ##

med_temp_list = [23.4, 16.3, 28.2, 21.3]

print(type(med_temp_list))

# Tuplas 

third_level_submodules = ("Backend II", "frontend II" , "Nuevas tecnologías")

print(type(third_level_submodules))

# Diccionarios 

submodule_teacher = {"Bc2":"Juan", "Frn2":"Jaime", "NT":"Ber"}

# Conjuntos 

age_set = {34, 19, 25, 28, 42, 18}


## La concatenación

print(f"Usuario {userName}, tiene {age} años")

print("Usuario", userName ,",", "tiene " , age, "años")


## Input 


#salary = input("Ingrese el valor de su salario")

#print( f"Salario : {salary}")

# Operadores -> Ariméticos , comparación , lógicos , asignación

# +,-,*,/,%

num1 = 23

num2= 45

resultSum =  num1 + num2

print(resultSum) 

##lab: Cree las demás operaciones pero insertando los numeros desde teclado

#num3 = int(input("Ingrese el numero:"))  # Esto es casting de variables 

#num4 = int(input("Ingrese el otro numero")) # Esto es Casting de variables 

#result_substration = num3 - num4

#print( f"el resultado de la resta es: {result_substration} ")

## Operadores de comparacion <, > , >= , <= , ==, != , Estos retornan un booleano

dollar_price = 4100

euro_price = 4300

higer_coin_value = dollar_price > euro_price

print("Dolar es mayor: " , higer_coin_value)

##Lab realice ejemplos con los demás operadores 

## Operadores lógicos 

user_phone = False

user_mail = False

user  = user_phone or user_mail

password = True 

session = user and password

print (f"Inicio de Sesion: {session}")

# Operadores de asignación = , +=, -= , *=, /= , %=

salary = 1300000

#salary = salary + 200000

salary += 200000

print(salary)

# lab Use los demas operadores de asignacion en operaciones con numeros enteros 