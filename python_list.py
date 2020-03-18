

mix_list = ['honda', 28, 26.1, False, 'audi']


print(mix_list)

matrix = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
]

print(matrix)

for x in matrix:
    for y in x:
        print(y, end=' ')
    print()

# List Slicing
numbers_list = [1, 2, 3, 4, 5]
print(numbers_list[0:2])
print(numbers_list[2:-2])

# List Iteration mby for loop
cars = ['honda', 'toyota', 'audi']
for car in cars:
    print(car)
    if car == 'toyota':
        print('I love toyota')


shop_items = {
    'rice' : 44,
    'floor' : 33,
    'oil' : 59
}

print(shop_items)

for key, value in sorted(shop_items.items()):
    print(key, value, sep='|')
