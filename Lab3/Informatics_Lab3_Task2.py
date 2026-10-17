import re

test01 = 'students.spam@yandex.ru'
        # yandex.ru
test02 = 'example@example'
        # Fail!
test03 = 'example@example.com'
        # example.com
test1 = 'vlad.ivanov@mail.ru'
        # mail.ru
test2 = 'dmitriy-smirnov@yandex.ru'
        # Fail!
test3 = '123.sveta_petrova@gmail.com'
        # gmail.com
test4 = 'tihonova@.ru'
        # Fail!
test5 = 'alex@alex.alex'
        # alex.alex
test6 = '.@mail.ru'
        # Fail!
test7 = 'a@gmail.com'
        # gmail.com

tests = [test01, test02, test03, test1, test2, test3, test4, test5, test6, test7]

pattern = r"^\w+(?:\.\w+)*@([a-z]+\.[a-z]+)$"

for text in tests:
    result = re.findall(pattern, text)
    print('Ввод:\n', text)
    print()
    print('Вывод:\n', result)
    print('__________________')
