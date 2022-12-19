def count_vowels(s: str):
    l: list = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u']  # sometimes y, but this program will not include that for now
    count = 0
    for i in l:
        if i in vowels:
            count += 1

    return count
