# Если функция передает кортеж, то посчитать длину всех слов(1).
# Если список, то посчитать количество букв и цифр(2).
# Если число - количество нечетних цифр.(3)
# Строка - количество букв. (4)
# Сделать проверку по всем случаям.

def chetnechet():          #3
    a = input('chislo: ')
    chet_1 = '02468'
    chet = 0
    nechet = 0
    for i in a:
        if i in chet_1:
            chet += 1
        else:
            nechet += 1
    print('chetnih', chet, ',', 'nechetnih', nechet)
chetnechet()

def bukvi():                    #4
    a = input('Vvedite tekst: ')
    d = 0
    for i in a:
        if i.isalpha():
            d += 1
    print('bukv: ', d)
bukvi()


def spis():
    tekst = ['mama mila ramu 5 raz', 'papa mil 1 raz']         #2
    tekst_1 = str(tekst)
    a = {'Буквы': 0, 'Цифры': 0}
    for i in tekst_1:
        if i.isalpha():
            a['Буквы'] += 1
        elif i.isdigit():
            a['Цифры'] += 1
    print('cifri:',a['Цифры'],',', 'bukvi:', a['Буквы'],)
spis()

def kortezh():            #1
    a = ('jghh', 'afg', 'aa',)
    b = len(a[1])
    c = len(a[0])
    d = len(a[2])
    print('Dlina 1go:', '-', c, 'dlina 2go:', '-', b, 'dlina 3go:', '-', d)
kortezh()