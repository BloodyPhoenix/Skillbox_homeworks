# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно просчитать протокол турнира по боулингу в файле tournament.txt
#
# Пример записи из лога турнира
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/
#   Татьяна	62334/6/4/44X361/X
#   Давид	--8/--8/4/8/-224----
#   Павел	----15623113-95/7/26
#   Роман	7/428/--4-533/34811/
#   winner is .........
#
# Нужно сформировать выходной файл tournament_result.txt c записями вида
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/    98
#   Татьяна	62334/6/4/44X361/X      131
#   Давид	--8/--8/4/8/-224----    68
#   Павел	----15623113-95/7/26    69
#   Роман	7/428/--4-533/34811/    94
#   winner is Татьяна

# Код обаботки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>

import bowling_tournament
import argparse


def main():
    parser = argparse.ArgumentParser(description="A score counter")
    parser.add_argument("--input", default=None, type=str, help="Tournaments result file")
    parser.add_argument("-o", "--output", default=None, type=str, help="Name of the output file")
    args = parser.parse_args()
    result = args.input
    file_name = args.output
    bowling_tournament.count_tournament_result(result, file_name)


# home\PycharmProjects\students\chashchina_mariia\lesson_014>python 02_tournament.py --input tournament.txt

# Некорректная пара: сбиты все кегли, должен быть знак "/" ('Некорректная пара: сбиты все кегли, должен быть знак "/"',)
# Ошибка входных данных: too many values to unpack (expected 2), ('too many values to unpack (expected 2)',)


if __name__ == "__main__":
    main()

# Усложненное задание (делать по желанию)
#
# После обработки протокола турнира вывести на консоль рейтинг игроков в виде таблицы:
#
# +----------+------------------+--------------+
# | Игрок    |  сыграно матчей  |  всего побед |
# +----------+------------------+--------------+
# | Татьяна  |        99        |      23      |
# ...
# | Алексей  |        20        |       5      |
# +----------+------------------+--------------+

# зачет!
