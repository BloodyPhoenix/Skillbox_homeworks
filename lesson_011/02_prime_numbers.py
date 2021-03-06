# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.iteration_index = 0
        self.prime_numbers = []

    def __repr__(self):
        return f"Количество итераций {self.n}. Проверяется число {self.iteration_index}. Имеются числа {self.prime_numbers}"

    def __iter__(self):
        self.iteration_index = 1
        return self

    def __next__(self):
        while self.iteration_index <= self.n:
            self.iteration_index += 1
            if self.check_number():
                return self.iteration_index
        raise StopIteration()

    def check_number(self):
        for prime in self.prime_numbers:
            if self.iteration_index % prime == 0:
                return False
        self.prime_numbers.append(self.iteration_index)
        return True


#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)

#
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def happy_number(number):
    number = str(number)
    counter = len(number) // 2
    first_part = 0
    second_part = 0
    for index in range(counter):
        first_part += int(number[index])
        second_part += int(number[-index - 1])
    if first_part != second_part:
        return False
    return True


def palindrome(number):
    number = str(number)
    if number != number[::-1]:
        return False
    return True


def automorphic(number):
    square = str(number ** 2)
    number = str(number)
    if square[-len(number):] == number:
        return True
    else:
        return False


simple_palindromes = filter(palindrome, prime_numbers_generator(1000))
# for number in simple_palindromes:
#     print(number)

simple_automorphic_palindromes = filter(automorphic, filter(palindrome, prime_numbers_generator(10000)))
for number in simple_automorphic_palindromes:
    print(number)

spisok = []
for x in range(1000):
    spisok.append(x)

automorphic_happy = filter(automorphic, filter(happy_number, spisok))
for number in automorphic_happy:
    print(number)

# А палиндромы, вообще-то, явояются счастливыми по определению

# зачет!
