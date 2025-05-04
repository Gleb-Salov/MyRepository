def read_input():
    return input("Введите текст: ")

def print_stats(text: str):
    print(f"Слов: {len(text.split())}")
    print(f"Символов: {len(text.replace(" ",""))}")

