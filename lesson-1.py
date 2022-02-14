import subprocess
import chardet

# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных. Затем с помощью
# онлайн-конвертера преобразовать строковые представление в формат Unicode и также
# проверить тип и содержимое переменных.

word1 = 'разработка'
word2 = 'сокет'
word3 = 'декоратор'

print(word1, word2, word3)
print(type(word1), type(word2), type(word3))

word1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word2 = '\u0441\u043e\u043a\u0435\u0442'
word3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(type(word1), type(word2), type(word3))
print(word1, word2, word3)
print('\n')

# --------------------------------------------------------------------------------------------------------------
# 2. Каждое из слов «class», «function», «method» записать в байтовом типе
# без преобразования в последовательность кодов (не используя методы encode
#  и decode) и определить тип, содержимое и длину соответствующих переменных.

word1 = b'class'
word2 = b'function'
word3 = b'method'

print(type(word1), type(word2), type(word3))
print(word1, word2, word3)
print(len(word1), len(word2), len(word3))
print('\n')

# ---------------------------------------------------------------------------------------------------------------
# 3. Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе.

words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    try:
        bytes(word, 'ascii')
    except UnicodeEncodeError:
        print(f'Слово "{word}" невозможно записать в виде байтовой строки')

print('\n')

# ---------------------------------------------------------------------------------------------------------------
# 4. Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить обратное
# преобразование (используя методы encode и decode).

word1 = 'разработка'.encode('utf-8')
word2 = 'администрирование'.encode('utf-8')
word3 = 'protocol'.encode('utf-8')
word4 = 'standard'.encode('utf-8')
print(word1, word2, word3, word4)
word1 = word1.decode('utf-8')
word2 = word2.decode('utf-8')
word3 = word3.decode('utf-8')
word4 = word4.decode('utf-8')
print(word1, word2, word3, word4)
print('\n')

# ---------------------------------------------------------------------------------------------------------------
# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
# результаты из байтовового в строковый тип на кириллице.

urls = ['yandex.ru', 'youtube.com']
for url in urls:
    ping = subprocess.Popen(('ping', url), stdout=subprocess.PIPE)

    for i, line in enumerate(ping.stdout):
        data = chardet.detect(line)
        line = line.decode(data['encoding']).encode('utf-8')
        print(line.decode('utf-8')) if i < 5 else ping.kill()

# ---------------------------------------------------------------------------------------------------------------
# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку
# файла по умолчанию. Принудительно открыть файл в формате Unicode и
# вывести его содержимое.

lines = ['сетевое программирование', 'сокет', 'декоратор']
with open('test.txt', 'w') as file:
    for line in lines:
        file.write(f'{line}\n')

with open('test.txt', 'rb') as file:
    data = file.read()
encoding = chardet.detect(data)['encoding']
print(encoding)

with open('test.txt', 'r', encoding=encoding) as file:
    data = file.read()
print(data)