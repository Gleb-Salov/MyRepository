# Можем ввести строку и проверить ее на кол-во слов и символов
from tools.io_helpers import read_input, print_stats 
# Можем записать текст в файл и потом его отттуда вынуть и почесть
from tools.file_ops import save_text_to_file, read_text_from_file
# Можем каждое слово текста вывести с большой буквы
from tools.formatter import capitalize_words
# Можем перевернуть текст наизнанку
from tools.utils.reverse import reverse_words

text = read_input() # Запрашиваем текст

save_text_to_file(text) # Сохраняем текст в файл

saved_text = read_text_from_file()
# Читаем текст уже из файла, т.к. у нас в функции
# read_text_from_file по умолчанию такой же путь как и у save_text_to_file

print_stats(saved_text) # Печатаем аналитику: слова и символы(без пробелов)

print(capitalize_words(saved_text)) # Печатаем текст с заглавными буквами

print(reverse_words(saved_text)) # Печатаем текст задо наперед