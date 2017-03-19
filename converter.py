import sys


def conv_strength():
    # Коневертация силы
    # http://www.convert-me.com/ru/convert/force/newton.html?u=newton&v=1
    choice_1 = input('Из какой единицы силы мы будем конвертировать? мН/Н/кН/МН\n')
    try:
        choice_2 = int(input('Сколько?(число)\n'))
        pass
    except ValueError:
        print('Это не число, попробуй еще раз.')
        conv_strength()
        pass
    choice_3 = input('В какую единицу силы мы будем конвертировать? мН/Н/кН/МН\n')
    if choice_1 == 'мН' and choice_3 == 'мН':
        conv_strength = choice_2
        return conv_strength
    elif choice_1 == 'мН' and choice_3 == 'Н':
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
    elif choice_1 == 'Н' and choice_3 == 'Н':
        conv_strength = choice_2
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
    elif choice_1 == 'кН' and choice_3 == 'кН':
        conv_strength = choice_2
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
    elif choice_1 == 'МН' and choice_3 == 'МН':
        conv_strength = choice_2
        return conv_strength
    else:
        print('Одна из мер силы неверна.')
        conv_strength()
        pass


def conv_mass():
    # Конвертация массы
    choice_1 = input('Из какой единицы массы мы будем конвертировать? мг/г/кг/ц/т\n')
    try:
        choice_2 = int(input('Сколько?(число)\n'))
        pass
    except ValueError:
        print('Это не число, попробуй еще раз.')
        conv_mass()
        pass
    choice_3 = input('В какую единицу массы мы будем конвертировать? мг/г/кг/ц/т\n')
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    return conv_mass


def conv_pressure():
    # Конвертация давления
    choice_1 = input('Из какой единицы давления мы будем конвертировать? Па\кПа\гПа\МПа\мм.рт.ст.\n')
    try:
        choice_2 = int(input('Сколько?(число)\n'))
        pass
    except ValueError:
        print('Это не число, попробуй еще раз.')
        conv_pressure()
        pass
    choice_3 = input('В какую единицу давления мы будем конвертировать? Па\кПа\гПа\МПа\мм.рт.ст.\n')
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    return conv_mass


def conv_metres():
    # Конвертация длины1
    choice_1 = input('Из какой единицы длины мы будем конвертировать? мм/см/м/дм/км\n')
    try:
        choice_2 = int(input('Сколько?(число)\n'))
        pass
    except ValueError:
        print('Это не число, попробуй еще раз.')
        conv_metres()
        pass
    choice_3 = input('В какую единицу длины мы будем конвертировать? мм/см/м/дм/км\n')
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    return conv_metres


def conv_volume():
    # Конвертация объема
    choice_1 = input('Из какой единицы объема мы будем конвертировать? мл/л(мм3/см3/м3/дм3/км3)\n')
    try:
        choice_2 = int(input('Сколько?(число)\n'))
        pass
    except ValueError:
        print('Это не число.')
        main_func()  # Странная вещь
        pass
    choice_3 = input('В какую единицу объема мы будем конвертировать? мл/л(мм3/см3/м3/дм3/км3)\n')
    if choice_1 == 'мл' and choice_3 == 'мл':
        conv_volume = choice_2
        return conv_volume
    elif choice_1 == 'мл' and choice_3 == 'л':
        conv_volume = choice_2 / 1000
        return conv_volume
    elif choice_1 == 'л' and choice_3 == 'л':
        conv_volume = choice_2
        return conv_volume
    elif choice_1 == 'л' and choice_3 == 'мл':
        conv_volume = choice_2 * 1000
        return conv_volume
    else:
        print('Одна из мер объема неверна.')
        main_func()
        pass


def conv_metres2():
    # Конвертация длины2
    choice_1 = input('Из какой единицы длины мы будем конвертировать? мм2/см2/м2/дм2/км2\n')
    try:
        choice_2 = int(input('Сколько?(число)\n'))
        pass
    except ValueError:
        print('Это не число, попробуй еще раз.')
        conv_metres()
        pass
    choice_3 = input('В какую единицу длины мы будем конвертировать? мм2/см2/м2/дм2/км2\n')
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    return conv_metres


def conv_metres3():
    # Конвертация длины3
    choice_1 = input('Из какой единицы длины мы будем конвертировать? мм3/см3/м3/дм3/км3\n')
    try:
        choice_2 = int(input('Сколько?(число)\n'))
        pass
    except ValueError:
        print('Это не число, попробуй еще раз.')
        conv_metres()
        pass
    choice_3 = input('В какую единицу длины мы будем конвертировать? мм3/см3/м3/дм3/км3\n')
    # Дальше идут описания каждого случая
    # Не забудь про неправильный выбор
    return conv_metres


def exit_conv_1():
    # "Хочеь продолжить конвертировать?" да - main_func() нет - exit_conv()
    conv_exit = input('Хочешь продолжить конвертировать? да/нет\n')
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
    conv_exit = input('Хочешь выйти из конвертатора V1.0(alpha)? да/нет\n')
    if conv_exit == 'да':
        input('Нажмите Enter')
        sys.exit()
        pass
    elif conv_exit == 'нет':
        main_func()
        pass
    else:
        exit_conv()
        pass


def main_func():
    # Выбор типа конвертации
    conv_choice = input('Что ты хочешь конвертировать? длина/длина2/длина3/объем/давление/масса/сила/выход\n')
    if conv_choice == 'длина':
        print(conv_metres())
        exit_conv_1()
        pass
    if conv_choice == 'длина2':
        print(conv_metres2())
        exit_conv_1()
        pass
    if conv_choice == 'длина3':
        print(conv_metres3())
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
    else:
        print('Невозможная величина.')
        main_func()
        pass


print('Добро пожаловать в конвертер единиц V1.0(alpha)')
main_func()
exit_conv()
