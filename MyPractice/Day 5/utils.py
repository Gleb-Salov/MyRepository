def is_even(n) -> bool:
    resolt = False
    if n % 2 == 0:
        resolt = True
    return resolt

if __name__ == "__main__":
    print(is_even(4))
