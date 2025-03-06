user_list = ["pp@mail.com", "maria@mail.com", "juan@mail.com", "laura@mail.com"]


for i in user_list:
    print(i)


for j in range(len(user_list)):
    print(f"email: {user_list[j]}")  


headers = ("Name", "DNI", "salary")

user= ["Pepe", "70100100", 2400000]


for k in headers:
    for l in user:
        print(k,l)
n=0
for m in user:
    print(headers[n],m)
    n+=1        