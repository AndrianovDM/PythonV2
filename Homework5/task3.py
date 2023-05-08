def fibonachi(number):
    list = [0, 1, 1]
    current = 0
    while current < number:
        while len(list) < number:
            list.append(sum(list[-2:]))
        yield list[current]
        current += 1