def words(wrd):
    words = {
        '0': 'ноль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять'
    }
    return ' '.join(words[d] for d in wrd)

file = open("bonus123.txt", 'r')
data = file.read()
mas = data.split()

for i in mas:
    if int(i[0]) % 2 != 0:
        if (i.count('1') + i.count('3') + i.count('5') + i.count('7') + i.count('9')) <= 3:
            nechet = [d for d in i if int(d) % 2 != 0]
            print(i, ' - ', words(i[0]), words(nechet))