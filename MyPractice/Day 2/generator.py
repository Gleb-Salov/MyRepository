def count_up_to(n:int):
    i = 0
    while i < n:
        i += 1
        yield i
    print("\n" + "-" * 40 + "\n")  

for numb in count_up_to(5):
    print(numb)

def even_range(n:int):
    i = 0
    while i < n:
        i += 1
        if i % 2 == 0:
            yield i
    print("\n" + "-" * 40 + "\n")  

for numb in even_range(10):
    print(numb)

def custom_range(start: int, end: int, step: int):
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step
    elif step == 0:
        raise ValueError("Такими темпами мы никогда не доберемся")
    print("\n" + "-" * 40 + "\n")  

for num in custom_range(3, 10, 2):
    print(num)