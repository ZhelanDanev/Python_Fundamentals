budget = int(input())
command = input()

while command != "End":
    price = int(command)
    if budget - price < 0:
        print('You went in overdraft!')
        exit()
    budget -= price
    command = input()

print('You bought everything needed.')

