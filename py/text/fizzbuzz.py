for i in range(1, 101):
    new_str = ""
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0:
            new_str += 'Fizz'
        if i % 5 == 0:
            new_str += 'Buzz'
        print(new_str)
    else:
        print(i)
