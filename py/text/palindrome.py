from reverse import reverse
from rempunctuation import rempunc


def palindromeFinder(s: str):
    rsplit = rempunc(reverse(s)).split(' ')

    count = 0
    palindromes = []
    for word in rsplit:
        if len(word) == 1:
            pass
        elif word == reverse(word):
            palindromes.append(word)
            count += 1

    return count, palindromes


string = input("Type a sentence. I'll let you know if any word in that sentence is a palindrome.\n> ")

find = palindromeFinder(string)
palCount = find[0]
palList = find[1]
palindromes = ''
for word in palList:
    palindromes += f"\t{word}\n"

print(f"This string has {palCount} palindrome{'' if palCount == 1 else 's'}\n"
      f"Palindromes:\n{palindromes}"
      f"(Note: One-letter words are excluded)")

# todo: refine. (if you want to do it, you can. i'm not going to)
