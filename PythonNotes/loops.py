

my_list = [23, 45, 24, 34, 18, 26]


i = 0

## Esto es un contador 

while i < len(my_list):
    print(my_list[i])
    i+=1

print("------------------")
## Esto es un acumulador

j = 0
sum = 0

while j < len(my_list):
    sum = sum + my_list[j]
    print(sum)
    j+=1

average = sum/ len(my_list)
print(f"el promedio es {average}")
print(len(my_list) )   

form = []

print(f"Nombre \n Cedula \n telefono \n correo \n salario ")

size = 5
y = 0

while y < size:
    dato = input("dato")
    form.append(dato)
    y+=1

z= 0

while z < size:
    print(form[z])
    z+=1


