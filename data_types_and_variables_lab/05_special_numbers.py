n = int(input())
special_digits = [5, 7, 11]

for num in range(1, n + 1):
    total = 0
    digits = num
    while digits > 0:
        total += digits % 10
        digits = int(digits / 10)
    if total in special_digits:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')

