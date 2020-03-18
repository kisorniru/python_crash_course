# function define
def welcome():
    print('Hello World!')
    for x in range(0, 5):
        print("Hi", str(x))

welcome()

# Built in function
def againWelcome(userName):
    print("Wellcome {name}".format(name=userName))

againWelcome('Bill')

# Person details
def person_details(name, age, country):
    print(name, age, country, sep='|')

# positional aurgument (Order Important)
person_details('Bill', 45, 'US')
person_details(name='Swifft', age=40, country='Canada')

# keyword aurgument (Order Not Important)
person_details('Bill', 45, 'US')
person_details(age=40, name='Swifft', country='Canada')

# Default value
def new_person_details(name, age, country='Bangladesh'):
    print(name, age, country, sep='|')

# keyword aurgument (Order Not Important)
new_person_details('Bill', 45, 'US')
new_person_details(name='Swifft', age=40)