import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)

# O(n^2)
for number in numbers_1_to_10:
    the_numbers_match = False
    for num in my_randoms:
        if num == number:
            the_numbers_match = True
    if the_numbers_match:
        print(f'{number} is in the random list')
    else:
        print(f'{number} is NOT in the random list')
print(my_randoms)

# O(n) ...?
my_randoms = set(my_randoms)
numbers_1_to_10 = set(numbers_1_to_10)
exist = my_randoms.intersection(numbers_1_to_10)
dont_exist = (exist^numbers_1_to_10)&numbers_1_to_10
print(f'These numbers exist in the my_randoms list: {list(exist)}\nThese numbers do not exist in the my_randoms list: {list(dont_exist)}')