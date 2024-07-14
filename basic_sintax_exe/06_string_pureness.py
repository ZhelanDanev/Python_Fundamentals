n = int(input())
forbidden_symbols = [',', '.', '_']

for i in range(n):
    some_text = input()
    for letter in some_text:
        if letter in forbidden_symbols:
            print(f"{some_text} is not pure!")
            break

    else:
        print(f'{some_text} is pure.')

