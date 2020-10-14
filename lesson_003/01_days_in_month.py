# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input('Введите, пожалуйста, номер месяца: ')
if user_input.isdigit():
    month = int(user_input)
    print('Вы ввели', month)
    monthes_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # можно сразу написать вот так
    if 1 <= month <= 12:
        print("Такого месяца не существует!")
    else:
        days = monthes_days[month-1]
        if days%10 == 1:
            print(f"В месяце номер {month} {days} день")
        else:
            print (f"В месяце номер {month} {days} дней")
else:
    print("Вы ввели неверное значение! Пожалуйста, введите целое число.")

# зачет!
