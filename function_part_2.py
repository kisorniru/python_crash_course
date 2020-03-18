
# Function return
def square(num):
    return num * num

print( square(2), square(2.2), sep='|' )


# Optional argument

def get_name(f_name, l_name, middle_name=''):
    complete_name = f_name
    if middle_name:
        complete_name += ' ' + middle_name
    complete_name += ' ' + l_name
    return complete_name

print( get_name('Bill', 'Gates') )
print( get_name('Bill', 'Gates', 'S') )


# ------------------------------------------------------

num_list = [1, 2, 3, 4, 5]
num_dict = {'one': 1, 'two': 2, 'three': 3}

def change_num_list(list, dict):
    del list[0]
    list[-1] = 50

    del dict['one']
    dict['three'] = 33
    print("Inner List : ", list)
    print("Inner Dict : ", dict)

print("Before")
print("Outer List : ", num_list)
print("Outer Dict : ", num_dict)

change_num_list(list=num_list, dict=num_dict)

print("After")
print("Outer List : ", num_list)
print("Outer Dict : ", num_dict)






















