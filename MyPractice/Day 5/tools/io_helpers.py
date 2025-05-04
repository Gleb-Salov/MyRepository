def read_input():
    return input("Введите текст: ")

def print_stats(text):
    print("Слов:", len(text.split()))
    print("Символов:", len(text))
