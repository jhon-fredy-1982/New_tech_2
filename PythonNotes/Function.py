
# funciones en python
salaries =[1500000, 3000000, 2000000]
ages = [34, 45, 67 ,31, 23]
notes = [3.5, 4.6, 5.0, 2.8]

def average_calculator(my_list):
    sum = 0
    i = 0
    while i < len(my_list):
        sum = sum + my_list[i]
        i+=1
    average = sum/len(my_list)
    print(average)    


average_calculator(notes)