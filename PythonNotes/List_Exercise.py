

headers = ("ID", "Name", "LastName", "Mail", "Salary")

employee = [101,  "Maria", "Castro", "mcastro@mail.com" , 3400000]

i=0
for item in employee:
    print(headers[i], item)
    i+=1

for j in range(len(employee)):
    print(headers[j], employee[j])  