for i in range(100):
    if i % 5 == 0 or i % 3 == 0:
        newstr = ''
        if i % 5 == 0:
            newstr += 'Fizz'
        if i % 3 == 0:
            newstr += 'Buzz'
        print(newstr)
    else:
        print(i)
