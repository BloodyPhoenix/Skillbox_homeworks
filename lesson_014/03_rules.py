# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно изменить правила подсчета очков в игре.
# "Выходим на внешний рынок, а там правила игры другие!" - сказал он.
#
# Правила подсчета очков изменяются так:
#
# Если во фрейме страйк, сумма очков за этот фрейм будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за два следующих броска шара (в одном или двух фреймах,
# в зависимости от того, был ли страйк в следующем броске).
# Например: первый бросок шара после страйка - тоже страйк, то +10 (сбил 10 кеглей)
# и второй бросок шара - сбил 2 кегли (не страйк, не важно как закончится этот фрейм - считаем кегли) - то еще +2.
#
# Если во фрейме сбит спэр, то сумма очков будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за первый бросок шара в следующем фрейме.
#
# Если фрейм остался открытым, то сумма очков будет равна количеству сбитых кеглей в этом фрейме.
#
# Страйк и спэр в последнем фрейме - по 10 очков.
#
# То есть для игры «Х4/34» сумма очков равна 10+10 + 10+3 + 3+4 = 40,
# а для игры «ХXX347/21» - 10+20 + 10+13 + 10+7 + 3+4 + 10+2 + 3 = 92

# Необходимые изменения сделать во всех модулях. Тесты - дополнить.

# "И да, старые правила должны остаться! для внутреннего рынка..." - уточнил менеджер напоследок.

import bowling_tournament
import argparse


def main():
    parser = argparse.ArgumentParser(description="A score counter")
    parser.add_argument("--input", default=None, type=str, help="Tournaments result file")
    parser.add_argument("-o", "--output", default=None, type=str, help="Name of the output file")
    parser.add_argument("-m", "--mode", default="external", type=str,
                        help="External or internal mode. External is default")
    args = parser.parse_args()
    result = args.input
    file_name = args.output
    mode = args.mode
    bowling_tournament.count_tournament_result(result, mode, file_name)


if __name__ == "__main__":
    main()
