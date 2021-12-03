with open('../inputs/day1.txt', 'r') as file: 
    text = file.read()
    numbers = list(map(lambda x: int(x), text.split('\n')))
    count = 0
    for (i, number) in enumerate(numbers):
        if i == 0:
            continue
        if number > numbers[i-1]:
            count += 1
    print(count)

