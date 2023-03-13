# 3
def separator(simbol, count):
    return simbol * count

print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True

#2
def long_separator(count):
    return separator('*', count)


print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True


#1
def simple_separator():
    return long_separator(10)

print(simple_separator() == '**********')  # True

#5
def hello_who(who='World'):
    print(separator('*', 10))
    print()
    print(f'Hello {who}!')
    print()
    print(separator('#', 10))

hello_who()

hello_who('Max')

hello_who('Kate')

#4
def hello_world():
    hello_who()

hello_world()

#6
def pow_many(power, *args):
    return sum (args) ** power


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

#7
def print_key_val(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} --> {v}')


print_key_val(name='Max', age=21)

print_key_val(animal='Cat', is_animal=True)

#8
def my_filter(iterable, function):
    result = []
    for item in iterable:
        if function(item):
            result.append(item)
    return result


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True