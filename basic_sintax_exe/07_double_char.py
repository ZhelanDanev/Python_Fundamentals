
while True:
    new_word = ''
    command = input()
    if command == 'SoftUni':
        continue
    elif command == "End":
        break
    else:
        for letter in command:
            new_word += letter * 2

        print(new_word)
