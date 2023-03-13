def first_question():
    year = input('Ввведите год рождения А.С.Пушкина:')
    while year != '1799':
        print("Не верно")
        year = input('Ввведите год рождения А.С.Пушкина:')

first_question()

day = input('Ввведите день рождения А.С.Пушкина?')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился А.С.Пушкина?')
print('Верно')
