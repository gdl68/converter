# coding=utf-8
import sys


def number_check(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


def conv_speed():
    while True:
        choice_1 = input('\nИз какой единицы измерения '
                         'скорости мы\n будем конвертировать? "м\с"/"м\м"/"м\ч"/"км\с"/"км\м"/"км\ч"\n')
        if choice_1 == 'м\с' or choice_1 == 'м\м' or choice_1 == 'м\ч' or choice_1 == 'км\с' or choice_1 == 'км\м'\
            or choice_1 == 'км\ч':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная еденица измерения!\n'
                  '===================================\n')
            continue
    while True:
        choice_2 = str(input('\nСколько?\n'))
        number = number_check(choice_2)
        if number == False:
            print('\n===================================\n'
                  '            Это не число!\n'
                  '===================================\n')
            continue
        else:
            choice_2 = float(choice_2)
            break
    while True:
        choice_3 = input('\nВ какую единицу измерения скорости мы\n '
                         'будем конвертировать?\n')
        if choice_3 == 'м\с' or choice_3 == 'м\м' or choice_3 == 'м\ч' or choice_3 == 'км\с' or choice_3 == 'км\м' \
                or choice_3 == 'км\ч':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная еденица измерения!\n'
                  '===================================\n')
            continue
    if choice_1 == 'м\с':
        if choice_3 == 'м\м':
            conv_speed = choice_2 * 60
            return conv_speed
        elif choice_3 == 'м\ч':
            conv_speed = choice_2 * 3600
            return conv_speed
        elif choice_3 == 'км\с':
            conv_speed = choice_2 * 0.001
            return conv_speed
        elif choice_3 == 'км\м':
            conv_speed = choice_2 * 0.06
            return conv_speed
        elif choice_3 == 'км\ч':
            conv_speed = choice_2 * 3.6
            return conv_speed
        elif choice_3 == choice_1:
            conv_speed = choice_2
            return conv_speed
    elif choice_1 == 'м\м':
        if choice_3 == 'м\с':
            conv_speed = choice_2 * 0.01667
            return conv_speed
        elif choice_3 == 'м\ч':
            conv_speed = choice_2 * 60
            return conv_speed
        elif choice_3 == 'км\с':
            conv_speed = choice_2 * 0.00001667
            return conv_speed
        elif choice_3 == 'км\м':
            conv_speed = choice_2 * 0.001
            return conv_speed
        elif choice_3 == 'км\ч':
            conv_speed = choice_2 * 0.06
            return conv_speed
        elif choice_3 == choice_1:
            conv_speed = choice_2
            return conv_speed
    elif choice_1 == 'м\ч':
        if choice_3 == 'м\с':
            conv_speed = choice_2 * 0.0002778
            return conv_speed
        elif choice_3 == 'м\м':
            conv_speed = choice_2 * 0.01667
            return conv_speed
        elif choice_3 == 'км\с':
            conv_speed = choice_2 * 0.0000002778
            return conv_speed
        elif choice_3 == 'км\м':
            conv_speed = choice_2 * 0.00001667
            return conv_speed
        elif choice_3 == 'км\ч':
            conv_speed = choice_2 * 0.001
            return conv_speed
        elif choice_1 == choice_3:
            conv_speed = choice_2
            return conv_speed
    elif choice_1 == 'км\с':
        if choice_3 == 'м\с':
            conv_speed = choice_2 * 1000
            return conv_speed
        elif choice_3 == 'м\м':
            conv_speed = choice_2 * 60000
            return conv_speed
        elif choice_3 == 'м\ч':
            conv_speed = choice_2 * 3600000
            return conv_speed
        elif choice_3 == 'км\м':
            conv_speed = choice_2 * 60
            return conv_speed
        elif choice_3 == 'км\ч':
            conv_speed = choice_2 * 3600
            return conv_speed
        elif choice_3 == choice_1:
            conv_speed = choice_2
            return conv_speed
    elif choice_1 == 'км\м':
        if choice_3 == 'м\с':
            conv_speed = choice_2 * 16.67
            return conv_speed
        elif choice_3 == 'м\м':
            conv_speed = choice_2 * 1000
            return conv_speed
        elif choice_3 == 'м\ч':
            conv_speed = choice_2 * 60000
            return conv_speed
        elif choice_3 == 'км\с':
            conv_speed = choice_2 * 0.01667
            return conv_speed
        elif choice_3 == 'км\ч':
            conv_speed = choice_2 * 60
            return conv_speed
        elif choice_1 == choice_3:
            conv_speed = choice_2
            return conv_speed
    elif choice_1 == 'км\ч':
        if choice_3 == 'м\с':
            conv_speed = choice_2 * 0.2778
            return conv_speed
        elif choice_3 == 'м\м':
            conv_speed = choice_2 * 16.67
            return conv_speed
        elif choice_3 == 'м\ч':
            conv_speed = choice_2 * 1000
            return conv_speed
        elif choice_3 == 'км\с':
            conv_speed = choice_2 * 0.0002778
            return conv_speed
        elif choice_3 == 'км\м':
            conv_speed = choice_2 * 0.01667
            return conv_speed
        elif choice_1 == choice_3:
            conv_speed = choice_2
            return conv_speed
    else:
        print('Что то пошло не так...')
        main_func()
        pass


def conv_strength():
    # Коневертация силы
    # http://www.convert-me.com/ru/convert/force/newton.html?u=newton&v=1
    while True:
        choice_1 = input('Из какой единицы измерения '
                         'силы мы\n будем конвертировать? мН/Н/кН/МН\n')
        if choice_1 == 'мН' or choice_1 == 'Н' or choice_1 == 'кН' or choice_1 == 'МН':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная единица измерения!\n'
                  '===================================\n')
            continue
    while True:
        choice_2 = str(input('\nСколько?(целое число)\n'))
        number = number_check(choice_2)
        if number == False:
            print('\n===================================\n'
                  '            Это не число!\n'
                  '===================================\n')
            continue
        else:
            choice_2 = int(choice_2)
            break
    while True:
        choice_3 = input('\nВ какую единицы измерения силы мы\n '
                         'будем конвертировать? мН/Н/кН/МН\n')
        if choice_3 == 'мН' or choice_3 == 'Н' or choice_3 == 'кН' or choice_3 == 'МН':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная единица измерения!\n'
                  '===================================\n')
            continue
    if choice_1 == 'мН' and choice_3 == 'Н':
        conv_strength = choice_2 / 1000
        return conv_strength
    elif choice_1 == 'мН' and choice_3 == 'кН':
        conv_strength = choice_2 / 1000 * 0.001
        return conv_strength
    elif choice_1 == 'мН' and choice_3 == 'МН':
        conv_strength = choice_2 / 1000 * 0.000001
        return conv_strength
    elif choice_1 == 'Н' and choice_3 == 'мН':
        conv_strength = choice_2 * 1000
        return conv_strength
    elif choice_1 == 'Н' and choice_3 == 'кН':
        conv_strength = choice_2 * 0.001
        return conv_strength
    elif choice_1 == 'Н' and choice_3 == 'МН':
        conv_strength = choice_2 * 0.000001
        return conv_strength
    elif choice_1 == 'кН' and choice_3 == 'мН':
        conv_strength = choice_2 * 1000000
        return conv_strength
    elif choice_1 == 'кН' and choice_3 == 'Н':
        conv_strength = choice_2 * 1000
        return conv_strength
    elif choice_1 == 'кН' and choice_3 == 'МН':
        conv_strength = choice_2 * 0.001
        return conv_strength
    elif choice_1 == 'МН' and choice_3 == 'мН':
        conv_strength = choice_2 * 1000000000
        return conv_strength
    elif choice_1 == 'МН' and choice_3 == 'Н':
        conv_strength = choice_2 * 1000000
        return conv_strength
    elif choice_1 == 'МН' and choice_3 == 'кН':
        conv_strength = choice_2 * 1000
        return conv_strength
    elif choice_1 == choice_3:
        conv_strength = choice_2
        return conv_strength
    else:
        print('\nОдна из мер длины неверна.')
        main_func()
        pass


def conv_mass():
    # Конвертация массы
    while True:
        choice_1 = input('\nИз какой единицы измерения '
                         'массы мы\n будем конвертировать? мг/г/кг/ц/т\n')
        if choice_1 == 'мг' or choice_1 == 'г' or choice_1 == 'кг' or choice_1 == 'ц' or choice_1 == 'т':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная единица измерения!\n'
                  '===================================\n')
            continue
    while True:
        choice_2 = str(input('\nСколько?\n'))
        number = number_check(choice_2)
        if number == False:
            print('\n===================================\n'
                  '            Это не число!\n'
                  '===================================\n')
            continue
        else:
            choice_2 = float(choice_2)
            break
    while True:
        choice_3 = input('\nВ какую единицы измерения массы мы\n '
                         'будем конвертировать? мг/г/кг/ц/т\n')
        if choice_3 == 'мг' or choice_3 == 'г' or choice_3 == 'кг' or choice_3 == 'ц' or choice_3 == 'т':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная единица измерения!\n'
                  '===================================\n')
            continue
    if choice_1 == 'мг' and choice_3 == 'г':
        conv_mass = choice_2 * 0.001
        return conv_mass
    elif choice_1 == 'мг' and choice_3 == 'кг':
        conv_mass = choice_2 * 0.000001
        return conv_mass
    elif choice_1 == 'мг' and choice_3 == 'ц':
        conv_mass = choice_2 * 0.00000001
        return conv_mass
    elif choice_1 == 'мг' and choice_3 == 'т':
        conv_mass = choice_2 * 0.000000001
        return conv_mass
    elif choice_1 == 'г' and choice_3 == 'мг':
        conv_mass = choice_2 * 1000
        return conv_mass
    elif choice_1 == 'г' and choice_3 == 'кг':
        conv_mass = choice_2 * 0.001
        return conv_mass
    elif choice_1 == 'г' and choice_3 == 'ц':
        conv_mass = choice_2 * 0.00001
        return conv_mass
    elif choice_1 == 'г' and choice_3 == 'т':
        conv_mass = choice_2 * 0.000001
        return conv_mass
    elif choice_1 == 'кг' and choice_3 == 'мг':
        conv_mass = choice_2 * 1000000
        return conv_mass
    elif choice_1 == 'кг' and choice_3 == 'г':
        conv_mass = choice_2 * 1000
        return conv_mass
    elif choice_1 == 'кг' and choice_3 == 'ц':
        conv_mass = choice_2 * 0.01
        return conv_mass
    elif choice_1 == 'кг' and choice_3 == 'т':
        conv_mass = choice_2 * 0.001
        return conv_mass
    elif choice_1 == 'ц' and choice_3 == 'мг':
        conv_mass = choice_2 * 100000000
        return conv_mass
    elif choice_1 == 'ц' and choice_3 == 'г':
        conv_mass = choice_2 * 100000
        return conv_mass
    elif choice_1 == 'ц' and choice_3 == 'кг':
        conv_mass = choice_2 * 100
        return conv_mass
    elif choice_1 == 'ц' and choice_3 == 'т':
        conv_mass = choice_2 * 0.1
        return conv_mass
    elif choice_1 == 'т' and choice_3 == 'мг':
        conv_mass = choice_2 * 1000000000
        return conv_mass
    elif choice_1 == 'т' and choice_3 == 'г':
        conv_mass = choice_2 * 1000000
        return conv_mass
    elif choice_1 == 'т' and choice_3 == 'кг':
        conv_mass = choice_2 * 1000
        return conv_mass
    elif choice_1 == 'т' and choice_3 == 'ц':
        conv_mass = choice_2 * 10
        return conv_mass
    elif choice_1 == choice_3:
        conv_mass = choice_2
        return conv_mass
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    pass


def conv_pressure():
    # Конвертация давления
    while True:
        choice_1 = input('\nИз какой единицы измерения '
                         'давления мы\n будем конвертировать? Па/МПа/гПа/кПа\n')
        if choice_1 == 'Па' or choice_1 == 'МПа' or choice_1 == 'гПа' or choice_1 == 'кПа':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная единица измерения!\n'
                  '===================================\n')
            continue
    while True:
        choice_2 = str(input('\nСколько?\n'))
        number = number_check(choice_2)
        if number == False:
            print('\n===================================\n'
                  '            Это не число!\n'
                  '===================================\n')

            continue
        else:
            choice_2 = float(choice_2)
            break
    while True:
        choice_3 = input('\nВ какую единицы измерения давления мы\n '
                         'будем конвертировать? Па/МПа/гПа/кПа\n')
        if choice_3 == 'Па' or choice_3 == 'МПа' or choice_3 == 'гПа' or choice_3 == 'кПа':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная единица измерения!\n'
                  '===================================\n')
            continue
    if choice_1 == 'Па' and choice_3 == 'МПа':
        conv_pressure = choice_2 * 0.000001
        return conv_pressure
    elif choice_1 == 'Па' and choice_3 == 'гПа':
        conv_pressure = choice_2 * 0.01
        return conv_pressure
    elif choice_1 == 'Па' and choice_3 == 'кПа':
        conv_pressure = choice_2 * 0.001
        return conv_pressure
    elif choice_1 == 'МПа' and choice_3 == 'Па':
        conv_pressure = choice_2 * 1000000
        return conv_pressure
    elif choice_1 == 'МПа' and choice_3 == 'гПа':
        conv_pressure = choice_2 * 10000
        return conv_pressure
    elif choice_1 == 'МПа' and choice_3 == 'кПа':
        conv_pressure = choice_2 * 1000
        return conv_pressure
    elif choice_1 == 'гПа' and choice_3 == 'Па':
        conv_pressure = choice_2 * 100
        return conv_pressure
    elif choice_1 == 'гПа' and choice_3 == 'МПа':
        conv_pressure = choice_2 * 0.0001
        return conv_pressure
    elif choice_1 == 'гПа' and choice_3 == 'кПа':
        conv_pressure = choice_2 * 0.1
        return conv_pressure
    elif choice_1 == 'кПа' and choice_3 == 'Па':
        conv_pressure = choice_2 * 1000
        return conv_pressure
    elif choice_1 == 'кПа' and choice_3 == 'МПа':
        conv_pressure = choice_2 * 0.001
        return conv_pressure
    elif choice_1 == 'кПа' and choice_3 == 'гПа':
        conv_pressure = choice_2 * 10
        return conv_pressure
    elif choice_1 == choice_3:
        conv_pressure = choice_2
        return conv_pressure
    else:
        print('Что то пошло не так...')
        main_func()
        pass
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    pass


def conv_metres():
    # Конвертация длины1
    while True:
        choice_1 = input('\nИз какой единицы измерения '
                         'длины мы\n будем конвертировать? мм\см\дм\м\км\n')
        if choice_1 == 'мм' or choice_1 == 'см' or choice_1 == 'дм' or choice_1 == 'км' or choice_1 == 'м':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная единица измерения!\n'
                  '===================================\n')
            continue
    while True:
        choice_2 = str(input('\nСколько?\n'))
        number = number_check(choice_2)
        if number == False:
            print('\n===================================\n'
                  '            Это не число!\n'
                  '===================================\n')
            continue
        else:
            choice_2 = float(choice_2)
            break
    while True:
        choice_3 = input('\nВ какую единицы измерения '
                         'длины мы\n будем конвертировать? мм\см\дм\м\км\n')
        if choice_3 == 'мм' or choice_3 == 'см' or choice_3 == 'дм' or choice_3 == 'км' or choice_3 == 'м':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная единица измерения!\n'
                  '===================================\n')
            continue
    if choice_1 == 'мм' and choice_3 == 'см':
        conv_metres = choice_2 / 10
        return conv_metres
    elif choice_1 == 'мм' and choice_3 == 'дм':
        conv_metres = choice_2 / 100
        return conv_metres
    elif choice_1 == 'мм' and choice_3 == 'м':
        conv_metres = choice_2 / 1000
        return conv_metres
    elif choice_1 == 'мм' and choice_3 == 'км':
        conv_metres = choice_2 / 1000000
        return conv_metres
    elif choice_1 == 'см' and choice_3 == 'мм':
        conv_metres = choice_2 * 10
        return conv_metres
    elif choice_1 == 'см' and choice_3 == 'дм':
        conv_metres = choice_2 / 10
        return conv_metres
    elif choice_1 == 'см' and choice_3 == 'м':
        conv_metres = choice_2 / 100
        return conv_metres
    elif choice_1 == 'см' and choice_3 == 'км':
        conv_metres = choice_2 / 100000
        return conv_metres
    elif choice_1 == 'дм' and choice_3 == 'мм':
        conv_metres = choice_2 * 100
        return conv_metres
    elif choice_1 == 'дм' and choice_3 == 'см':
        conv_metres = choice_2 * 10
        return conv_metres
    elif choice_1 == 'дм' and choice_3 == 'м':
        conv_metres = choice_2 / 10
        return conv_metres
    elif choice_1 == 'дм' and choice_3 == 'км':
        conv_metres = choice_2 / 10000
        return conv_metres
    elif choice_1 == 'м' and choice_3 == 'мм':
        conv_metres = choice_2 * 1000
        return conv_metres
    elif choice_1 == 'м' and choice_3 == 'см':
        conv_metres = choice_2 * 100
        return conv_metres
    elif choice_1 == 'м' and choice_3 == 'дм':
        conv_metres = choice_2 * 10
        return conv_metres
    elif choice_1 == 'м' and choice_3 == 'км':
        conv_metres = choice_2 / 1000
        return conv_metres
    elif choice_1 == 'км' and choice_3 == 'мм':
        conv_metres = choice_2 * 1000000
        return conv_metres
    elif choice_1 == 'км' and choice_3 == 'см':
        conv_metres = choice_2 * 100000
        return conv_metres
    elif choice_1 == 'км' and choice_3 == 'дм':
        conv_metres = choice_2 * 10000
        return conv_metres
    elif choice_1 == 'км' and choice_3 == 'м':
        conv_metres = choice_2 * 1000
        return conv_metres
    elif choice_1 == choice_3:
        conv_metres = choice_2
        return conv_metres
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    else:
        print('\nОдна из мер силы неверна.')
        main_func()
        pass


# мл/л/мм3/см3/м3/дм3/км3
def conv_volume():
    # Конвертация объема
    while True:
        choice_1 = input('\nИз какой единицы измерения '
                         'массы мы\n будем конвертировать? мл/л/мм3/см3/м3/дм3/км3\n')
        if choice_1 == 'мл' or choice_1 == 'л' or choice_1 == 'мм3' or choice_1 == 'см3' or choice_1 == 'м3' or \
                        choice_1 == 'дм3' or choice_1 == 'км3':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная единица измерения!\n'
                  '===================================\n')
            continue
    while True:
        choice_2 = str(input('\nСколько?\n'))
        number = number_check(choice_2)
        if number == False:
            print('\n===================================\n'
                  '            Это не число!\n'
                  '===================================\n')
            continue
        else:
            choice_2 = float(choice_2)
            break
    while True:
        choice_3 = input('\nВ какую единицы измерения массы мы\n '
                         'будем конвертировать? мл/л/мм3/см3/м3/дм3/км3\n')
        if choice_3 == 'мл' or choice_3 == 'л' or choice_3 == 'мм3' or choice_3 == 'см3' or choice_3 == 'м3' or \
                        choice_3 == 'дм3' or choice_3 == 'км3':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная единица измерения!\n'
                  '===================================\n')
            continue
    if choice_1 == 'мл' and choice_3 == 'л':
        conv_volume = choice_2 * 0.001
        return conv_volume
    elif choice_1 == 'мл' and choice_3 == 'мм3':
        conv_volume = choice_2 * 1000
        return conv_volume
    elif choice_1 == 'мл' and choice_3 == 'см3':
        conv_volume = choice_2 * 1
        return conv_volume
    elif choice_1 == 'мл' and choice_3 == 'дм3':
        conv_volume = choice_2 * 0.001
        return conv_volume
    elif choice_1 == 'мл' and choice_3 == 'м3':
        conv_volume = choice_2 * 0.000001
        return conv_volume
    elif choice_1 == 'мл' and choice_3 == 'км3':
        conv_volume = choice_2 * 0.000000000000001
        return conv_volume
    elif choice_1 == 'л' and choice_3 == 'мл':
        conv_volume = choice_2 * 1000
        return conv_volume
    elif choice_1 == 'л' and choice_3 == 'мм3':
        conv_volume = choice_2 * 1000000
        return conv_volume
    elif choice_1 == 'л' and choice_3 == 'см3':
        conv_volume = choice_2 * 1000
        return conv_volume
    elif choice_1 == 'л' and choice_3 == 'дм3':
        conv_volume = choice_2 * 1
        return conv_volume
    elif choice_1 == 'л' and choice_3 == 'м3':
        conv_volume = choice_2 * 0.001
        return conv_volume
    elif choice_1 == 'л' and choice_3 == 'км3':
        conv_volume = choice_2 * 0.000000000001
        return conv_volume
    elif choice_1 == 'мм3' and choice_3 == 'мл':
        conv_volume = choice_2 * 0.001
        return conv_volume
    elif choice_1 == 'мм3' and choice_3 == 'л':
        conv_volume = choice_2 * 0.000001
        return conv_volume
    elif choice_1 == 'мм3' and choice_3 == 'см3':
        conv_volume = choice_2 * 0.001
        return conv_volume
    elif choice_1 == 'мм3' and choice_3 == 'дм3':
        conv_volume = choice_2 * 0.000001
        return conv_volume
    elif choice_1 == 'мм3' and choice_3 == 'м3':
        conv_volume = choice_2 * 0.000000001
        return conv_volume
    elif choice_1 == 'мм3' and choice_3 == 'км3':
        conv_volume = choice_2 * 0.0000000000000000001
        return conv_volume
    elif choice_1 == 'см3' and choice_3 == 'мл':
        conv_volume = choice_2 * 1
        return conv_volume
    elif choice_1 == 'см3' and choice_3 == 'л':
        conv_volume = choice_2 * 0.001
        return conv_volume
    elif choice_1 == 'см3' and choice_3 == 'мм3':
        conv_volume = choice_2 * 1000
        return conv_volume
    elif choice_1 == 'см3' and choice_3 == 'дм3':
        conv_volume = choice_2 * 0.001
        return conv_volume
    elif choice_1 == 'см3' and choice_3 == 'м3':
        conv_volume = choice_2 * 0.000001
        return conv_volume
    elif choice_1 == 'см3' and choice_3 == 'км3':
        conv_volume = choice_2 * 0.000000000000001
        return conv_volume
    elif choice_1 == 'дм3' and choice_3 == 'мл':
        conv_volume = choice_2 * 1000
        return conv_volume
    elif choice_1 == 'дм3' and choice_3 == 'л':
        conv_volume = choice_2 * 1
        return conv_volume
    elif choice_1 == 'дм3' and choice_3 == 'мм3':
        conv_volume = choice_2 * 1000000
        return conv_volume
    elif choice_1 == 'дм3' and choice_3 == 'см3':
        conv_volume = choice_2 * 1000
        return conv_volume
    elif choice_1 == 'дм3' and choice_3 == 'м3':
        conv_volume = choice_2 * 0.001
        return conv_volume
    elif choice_1 == 'дм3' and choice_3 == 'км3':
        conv_volume = choice_2 * 0.000000000001
        return conv_volume
    elif choice_1 == 'м3' and choice_3 == 'мл':
        conv_volume = choice_2 * 1000000
        return conv_volume
    elif choice_1 == 'м3' and choice_3 == 'л':
        conv_volume = choice_2 * 1000
        return conv_volume
    elif choice_1 == 'м3' and choice_3 == 'мм3':
        conv_volume = choice_2 * 1000000000
        return conv_volume
    elif choice_1 == 'м3' and choice_3 == 'см3':
        conv_volume = choice_2 * 1000000
        return conv_volume
    elif choice_1 == 'м3' and choice_3 == 'дм3':
        conv_volume = choice_2 * 1000
        return conv_volume
    elif choice_1 == 'м3' and choice_3 == 'км3':
        conv_volume = choice_2 * 0.000000001
        return conv_volume
    elif choice_1 == 'км3' and choice_3 == 'мл':
        conv_volume = choice_2 * 1000000000000000
        return conv_volume
    elif choice_1 == 'км3' and choice_3 == 'л':
        conv_volume = choice_2 * 1000000000000
        return conv_volume
    elif choice_1 == 'км3' and choice_3 == 'мм3':
        conv_volume = choice_2 * 1000000000000000000
        return conv_volume
    elif choice_1 == 'км3' and choice_3 == 'см3':
        conv_volume = choice_2 * 1000000000000000
        return conv_volume
    elif choice_1 == 'км3' and choice_3 == 'дм3':
        conv_volume = choice_2 * 1000000000000
        return conv_volume
    elif choice_1 == 'км3' and choice_3 == 'м3':
        conv_volume = choice_2 * 1000000000
        return conv_volume
    # Для одинаковых
    elif choice_1 == choice_3:
        conv_volume = choice_2
        return conv_volume, choice_3
    else:
        print('\n'
              '===================================\n'
              'Ошибка, пожалуйста сообщите автору\n'
              'Телефон: +79611619556\n'
              'VK: vk.com\gdl68\n'
              'Почта: tampio.ilya.gdl68@gmail.com\n'
              '===================================\n')
        exit_conv()
        pass


def conv_metres2():
    # Конвертация длины2
    while True:
        choice_1 = input('\nИз какой единицы измерения '
                         'площади мы\n будем конвертировать? мм2/см2/дм2/м2/га/км2\n')
        if choice_1 == 'мм2' or choice_1 == 'см2' or choice_1 == 'дм2' or choice_1 == 'м2' or choice_1 == 'га'\
                or choice_1 == 'км2':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная еденица измерения!\n'
                  '===================================\n')
            continue
    while True:
        choice_2 = str(input('\nСколько?(целое число)\n'))
        number = number_check(choice_2)
        if number == False:
            print('\n===================================\n'
                  '            Это не число!\n'
                  '===================================\n')
            continue
        else:
            choice_2 = float(choice_2)
            break
    while True:
        choice_3 = input('\nВ какую единицы измерения массы мы\n '
                         'будем конвертировать? мм2/см2/дм2/м2/га/км2\n')
        if choice_3 == 'мм2' or choice_3 == 'см2' or choice_3 == 'дм2' or choice_3 == 'м2' or choice_3 == 'га'\
                or choice_3 == 'км2':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная еденица измерения!\n'
                  '===================================\n')
            continue
    if choice_1 == 'мм2' and choice_3 == 'см2':
        conv_metres2 = choice_2 * 0.01
        return conv_metres2
    elif choice_1 == 'мм2' and choice_3 == 'дм2':
        conv_metres2 = choice_2 * 0.0001
        return conv_metres2
    elif choice_1 == 'мм2' and choice_3 == 'м2':
        conv_metres2 = choice_2 * 0.000001
        return conv_metres2
    elif choice_1 == 'мм2' and choice_3 == 'га':
        conv_metres2 = choice_2 * 0.0000000001
        return conv_metres2
    elif choice_1 == 'мм2' and choice_3 == 'км2':
        conv_metres2 = choice_2 * 0.000000000001
        return conv_metres2
    elif choice_1 == 'см2' and choice_3 == 'мм2':
        conv_metres2 = choice_2 * 100
        return conv_metres2
    elif choice_1 == 'см2' and choice_3 == 'дм2':
        conv_metres2 = choice_2 * 0.01
        return conv_metres2
    elif choice_1 == 'см2' and choice_3 == 'м2':
        conv_metres2 = choice_2 * 0.0001
        return conv_metres2
    elif choice_1 == 'см2' and choice_3 == 'га':
        conv_metres2 = choice_2 * 0.00000001
        return conv_metres2
    elif choice_1 == 'см2' and choice_3 == 'км2':
        conv_metres2 = choice_2 * 0.0000000001
        return conv_metres2
    elif choice_1 == 'дм2' and choice_3 == 'мм2':
        conv_metres2 = choice_2 * 10000
        return conv_metres2
    elif choice_1 == 'дм2' and choice_3 == 'см2':
        conv_metres2 = choice_2 * 100
        return conv_metres2
    elif choice_1 == 'дм2' and choice_3 == 'м2':
        conv_metres2 = choice_2 * 0.01
        return conv_metres2
    elif choice_1 == 'дм2' and choice_3 == 'га':
        conv_metres2 = choice_2 * 0.000001
        return conv_metres2
    elif choice_1 == 'дм2' and choice_3 == 'км2':
        conv_metres2 = choice_2 * 0.00000001
        return conv_metres2
    elif choice_1 == 'м2' and choice_3 == 'мм2':
        conv_metres2 = choice_2 * 1000000
        return conv_metres2
    elif choice_1 == 'м2' and choice_3 == 'см2':
        conv_metres2 = choice_2 * 10000
        return conv_metres2
    elif choice_1 == 'м2' and choice_3 == 'дм2':
        conv_metres2 = choice_2 * 100
        return conv_metres2
    elif choice_1 == 'м2' and choice_3 == 'га':
        conv_metres2 = choice_2 * 0.0001
        return conv_metres2
    elif choice_1 == 'м2' and choice_3 == 'км2':
        conv_metres2 = choice_2 * 0.000001
        return conv_metres2
    elif choice_1 == 'га' and choice_3 == 'мм2':
        conv_metres2 = choice_2 * 10000000000
        return conv_metres2
    elif choice_1 == 'га' and choice_3 == 'см2':
        conv_metres2 = choice_2 * 100000000
        return conv_metres2
    elif choice_1 == 'га' and choice_3 == 'дм2':
        conv_metres2 = choice_2 * 1000000
        return conv_metres2
    elif choice_1 == 'га' and choice_3 == 'м2':
        conv_metres2 = choice_2 * 10000
        return conv_metres2
    elif choice_1 == 'га' and choice_3 == 'км2':
        conv_metres2 = choice_2 * 0.01
        return conv_metres2
    elif choice_1 == 'км2' and choice_3 == 'мм2':
        conv_metres2 = choice_2 * 1000000000000
        return conv_metres2
    elif choice_1 == 'км2' and choice_3 == 'см2':
        conv_metres2 = choice_2 * 10000000000
        return conv_metres2
    elif choice_1 == 'км2' and choice_3 == 'дм2':
        conv_metres2 = choice_2 * 100000000
        return conv_metres2
    elif choice_1 == 'км2' and choice_3 == 'м2':
        conv_metres2 = choice_2 * 1000000
        return conv_metres2
    elif choice_1 == 'км2' and choice_3 == 'га':
        conv_metres2 = choice_2 * 100
        return conv_metres2
    elif choice_1 == choice_3:
        conv_metres2 = choice_2
        return conv_metres2
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    else:
        print('что то пошло не так...')
        main_func()
        pass
    return conv_metres


def exit_conv_1():
    # "Хочеь продолжить конвертировать?" да - main_func() нет - exit_conv()
    conv_exit = input('\nХочешь продолжить конвертировать? да/нет\n')
    if conv_exit == 'да':
        main_func()
        pass
    elif conv_exit == 'нет':
        exit_conv()
        pass
    else:
        exit_conv_1()
        pass


def exit_conv():
    # Выход из конвертатора
    conv_exit = input('\nХочешь выйти из конвертатора V1.4? да/нет\n')
    if conv_exit == 'да':
        print('\nДо скорых встреч!')
        input('Нажмите Enter')
        sys.exit()
        pass
    elif conv_exit == 'нет':
        main_func()
        pass
    else:
        print('\n===================================\n'
              'Неправильный выбор (', conv_exit, ')'
              '\n===================================\n')
        exit_conv()
        pass


def main_func():
    # Выбор типа конвертации
    conv_choice = input('\nЧто ты хочешь конвертировать?\n'
                        ' длина/площадь/объем/давление/масса'
                        '/сила/скорость/выход\n')
    if conv_choice == 'длина':
        print(conv_metres())
        exit_conv_1()
        pass
    elif conv_choice == 'площадь':
        print(conv_metres2())
        exit_conv_1()
        pass
    elif conv_choice == 'выход':
        exit_conv()
        pass
    elif conv_choice == 'объем':
        print(conv_volume())
        exit_conv_1()
        pass
    elif conv_choice == 'давление':
        print(conv_pressure())
        exit_conv_1()
        pass
    elif conv_choice == 'масса':
        print(conv_mass())
        exit_conv_1()
        pass
    elif conv_choice == 'сила':
        print(conv_strength())
        exit_conv_1()
        pass
    elif conv_choice == 'скорость':
        print(conv_speed())
        exit_conv_1()
        pass
    else:
        print('\n===================================\n'
              ' Неверная величина!(', conv_choice, ')\n'
              '===================================\n')
        main_func()
        pass


print('\n===============================================\n'
      'Добро пожаловать в конвертер единиц V1.4\n'
      '===============================================\n')
main_func()
exit_conv()
