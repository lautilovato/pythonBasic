### List comprehension ###

my_original_list = [20, 11, 34, 67]

my_list = [i -10 for i  in my_original_list]
print(my_list)

my_list = [i for i in range(11)]
print(my_list)

my_list = [i * 2 for i in range(11)]
print(my_list)  


def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(11)]
print(my_list)  
