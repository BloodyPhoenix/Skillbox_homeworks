# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# Использование range по полному кругу даёт то, что последняя линия рисуется дважды, причём не всегда чётко
# поверх самой себя, что выглядит некрасиво. Чтобы фигура нормально замкнулась, её необходимо заканчивать через
# sd.line. Можно делать цикл от количества сторон, тем более что по уму оно используется для расчёта шага, так как
# сумма углов правильного многоугольника равна 180 * (кол-во сторон - 2)

def draw_triangle(start_point, start_angle, side_length, sides = 3):
    point_1 = sd.get_point(*start_point)
    start_point = point_1
    # TODO а что если int(360 \ sides)
    inner_angle = 180*(sides-2)/sides
    step = int(180-inner_angle)
    for angle_step in range(0, 361, step):
        side = sd.get_vector(start_point, start_angle + angle_step, side_length)
        side.draw(sd.COLOR_DARK_ORANGE, width=3)
        start_point = side.end_point

draw_triangle((100, 100), 20, 200)

def draw_square(start_point, start_angle, side_length, sides = 4):
    point_1 = sd.get_point(*start_point)
    start_point = point_1
    inner_angle = 180 * (sides - 2) / sides
    step = int(180 - inner_angle)
    for angle_step in range(0, 361, step):
        side = sd.get_vector(start_point, start_angle + angle_step, side_length)
        side.draw(sd.COLOR_DARK_ORANGE, width=3)
        start_point = side.end_point

draw_square((300,300), 50, 150)

def draw_pentagon(start_point, start_angle, side_length, sides = 5):
    point_1 = sd.get_point(*start_point)
    start_point = point_1
    inner_angle = 180 * (sides - 2) / sides
    step = int(180 - inner_angle)
    for angle_step in range(0, 361, step):
        side = sd.get_vector(start_point, start_angle + angle_step, side_length)
        side.draw(sd.COLOR_DARK_ORANGE, width=3)
        start_point = side.end_point

draw_pentagon((100,400), 50, 50)

# def draw_hexagon(start_point, start_angle, side_length, sides = 6):
#     point_1 = sd.get_point(*start_point)
#     start_point = point_1
#     inner_angle = 180 * (sides - 2) / sides
#     step = int(180 - inner_angle)
#     for angle_step in range(0, 361, step):
#         side = sd.get_vector(start_point, start_angle + angle_step, side_length)
#         side.draw(sd.COLOR_DARK_ORANGE, width=3)
#         start_point = side.end_point



# Вариант с использованием количества сторон как счётчика цикла

def draw_hexagon(start_point, start_angle, side_length, sides = 6):
    point_1 = sd.get_point(*start_point)
    start_point = point_1
    inner_angle = 180 * (sides - 2) / sides
    step = int(180 - inner_angle)
    for n in range(0, sides-1):
        side = sd.get_vector(start_point, start_angle + step*n, side_length)
        side.draw(sd.COLOR_DARK_ORANGE, width=3)
        start_point = side.end_point
    sd.line(point_1, start_point, sd.COLOR_DARK_ORANGE, width=3)

draw_hexagon((300, 400), 50, 100)

# TODO есть недочеты по оформлению кода по PEP8?. Используйте пункт меню пайчарма code-reformatCode

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()