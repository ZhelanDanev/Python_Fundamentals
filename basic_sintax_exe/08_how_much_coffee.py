command = input()
small_events = ['coding', 'dog', 'cat', 'movie']
big_events = [event.upper() for event in small_events]
count = 0

while command != 'END':
    if command in small_events:
        count += 1
    elif command in big_events:
        count += 2

    command = input()

if count > 5:
    print('You need extra sleep')
else:
    print(count)
