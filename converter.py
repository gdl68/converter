import sys

import math


def number_check(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


def conv_speed():
    # while True:
    #     choice_1 = input('\nИз какой единицы измерения '
    #                      'скорости мы\n будем конвертировать? мН/Н/кН/МН\n')
    #     if choice_1 == 'мН' or choice_1 == 'Н' or choice_1 == 'кН' or choice_1 == 'МН':
    #         break
    #     else:
    #         print('\n===================================\n'
    #               'Введена неверная еденица измерения!\n'
    #               '===================================\n')
    #         continue
    # while True:
    #     choice_2 = str(input('\nСколько?\n'))
    #     number = number_check(choice_2)
    #     if number == False:
    #         print('\n===================================\n'
    #               '            Это не число!\n'
    #               '===================================\n')
    #         continue
    #     else:
    #         choice_2 = float(choice_2)
    #         break
    # while True:
    #     choice_3 = input('\nВ какую единицы измерения скорости мы\n '
    #                      'будем конвертировать? мН/Н/кН/МН\n')
    #     if choice_3 == 'мН' or choice_3 == 'Н' or choice_3 == 'кН' or choice_3 == 'МН':
    #         break
    #     else:
    #         print('\n===================================\n'
    #               'Введена неверная еденица измерения!\n'
    #               '===================================\n')
    #         continue
    return conv_speed, choice_3


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
            choice_2 = int(choice_2)
            break
    while True:
        choice_3 = input('\nВ какую единицы измерения силы мы\n '
                         'будем конвертировать? мН/Н/кН/МН\n')
        if choice_3 == 'мН' or choice_3 == 'Н' or choice_3 == 'кН' or choice_3 == 'МН':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная еденица измерения!\n'
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
        print('\nОдна из мер силы неверна.')
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
        choice_3 = input('\nВ какую единицы измерения массы мы\n '
                         'будем конвертировать? мг/г/кг/ц/т/\n')
        if choice_3 == 'мг' or choice_3 == 'г' or choice_3 == 'кг' or choice_3 == 'ц' or choice_3 == 'т':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная еденица измерения!\n'
                  '===================================\n')
            continue
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    return conv_mass, choice_3


def conv_pressure():
    # Конвертация давления
    # while True:
    #     choice_1 = input('\nИз какой единицы измерения '
    #                      'давления мы\n будем конвертировать? мН/Н/кН/МН\n')
    #     if choice_1 == 'мН' or choice_1 == 'Н' or choice_1 == 'кН' or choice_1 == 'МН':
    #         break
    #     else:
    #         print('\n===================================\n'
    #               'Введена неверная еденица измерения!\n'
    #               '===================================\n')
    #         continue
    # while True:
    #     number = number_check(choice_2)
    #     if number == False:
    #         print('\n===================================\n'
    #               '            Это не число!\n'
    #               '===================================\n')
    #     choice_2 = str(input('\nСколько?\n'))
    #         continue
    #     else:
    #         choice_2 = float(choice_2)
    #         break
    # while True:
    #     choice_3 = input('\nВ какую единицы измерения давления мы\n '
    #                      'будем конвертировать? мН/Н/кН/МН\n')
    #     if choice_3 == 'мН' or choice_3 == 'Н' or choice_3 == 'кН' or choice_3 == 'МН':
    #         break
    #     else:
    #         print('\n===================================\n'
    #               'Введена неверная еденица измерения!\n'
    #               '===================================\n')
    #         continue
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    return conv_mass, choice_3


def conv_metres():
    # Конвертация длины1
    # while True:
    #     choice_1 = input('\nИз какой единицы измерения '
    #                      'массы мы\n будем конвертировать? мг/г/кг/ц/т\n')
    #     if choice_1 == 'мг' or choice_1 == 'г' or choice_1 == 'кг' or choice_1 == 'ц' or choice_1 == 'т':
    #         break
    #     else:
    #         print('\n===================================\n'
    #               'Введена неверная еденица измерения!\n'
    #               '===================================\n')
    #         continue
    # while True:
    #     choice_2 = str(input('\nСколько?\n'))
    #     number = number_check(choice_2)
    #     if number == False:
    #         print('\n===================================\n'
    #               '            Это не число!\n'
    #               '===================================\n')
    #         continue
    #     else:
    #         choice_2 = float(choice_2)
    #         break
    # while True:
    #     choice_3 = input('\nВ какую единицы измерения массы мы\n '
    #                      'будем конвертировать? мг/г/кг/ц/т/\n')
    #     if choice_3 == 'мг' or choice_3 == 'г' or choice_3 == 'кг' or choice_3 == 'ц' or choice_3 == 'т':
    #         break
    #     else:
    #         print('\n===================================\n'
    #               'Введена неверная еденица измерения!\n'
    #               '===================================\n')
    #         continue
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    return conv_metres, choice_3


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
        choice_3 = input('\nВ какую единицы измерения массы мы\n '
                         'будем конвертировать? мл/л/мм3/см3/м3/дм3/км3\n')
        if choice_3 == 'мл' or choice_3 == 'л' or choice_3 == 'мм3' or choice_3 == 'см3' or choice_3 == 'м3' or \
                        choice_3 == 'дм3' or choice_3 == 'км3':
            break
        else:
            print('\n===================================\n'
                  'Введена неверная еденица измерения!\n'
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
    # while True:
    #     choice_1 = input('\nИз какой единицы измерения '
    #                      'массы мы\n будем конвертировать? мг/г/кг/ц/т\n')
    #     if choice_1 == 'мг' or choice_1 == 'г' or choice_1 == 'кг' or choice_1 == 'ц' or choice_1 == 'т':
    #         break
    #     else:
    #         print('\n===================================\n'
    #               'Введена неверная еденица измерения!\n'
    #               '===================================\n')
    #         continue
    # while True:
    #     choice_2 = str(input('\nСколько?(целое число)\n'))
    #     number = number_check(choice_2)
    #     if number == False:
    #         print('\n===================================\n'
    #               '            Это не число!\n'
    #               '===================================\n')
    #         continue
    #     else:
    #         choice_2 = int(choice_2)
    #         break
    # while True:
    #     choice_3 = input('\nВ какую единицы измерения массы мы\n '
    #                      'будем конвертировать? мг/г/кг/ц/т/\n')
    #     if choice_3 == 'мг' or choice_3 == 'г' or choice_3 == 'кг' or choice_3 == 'ц' or choice_3 == 'т':
    #         break
    #     else:
    #         print('\n===================================\n'
    #               'Введена неверная еденица измерения!\n'
    #               '===================================\n')
    #         continue
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    return conv_metres, choice_3


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
    conv_exit = input('\nХочешь выйти из конвертатора V1.3(alpha)? да/нет\n')
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
                        '/сила/выход/скорость\n')
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
      'Добро пожаловать в конвертер единиц V1.3(alpha)\n'
      '===============================================\n')
main_func()
exit_conv()
