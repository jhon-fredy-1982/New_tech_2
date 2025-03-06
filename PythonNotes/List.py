

user = [100, "Pepito", "Perez", "pp@mail.com", 1350000, True , 8.5, 100]

user_responsabilities = ["Dicterions", "Supervision", "Informs"]



print(user.count(100))

print(len(user))

#user.remove(100)

user.pop()

user.pop(3)

user.reverse()

user.append("Manager")

user.insert(3, "pperez@mail.com")

user[2] = 2500000

#user.clear()

print("index ", user.index(2500000))


# listComprehesion

new_user = [ x for x in user]

user.extend(user_responsabilities)



print(user)