import string
from itertools import groupby

def main():
    data = numerify("hxbxwxba")

    while not isValid(data):
        increment(data)

    print ''.join(letterify(data))

def isValid(data):
    straight = False
    for number in [0, 1, 2, 3, 4, 5, 6, 7]:
        if data[number] == 8 or data[number] == 11 or data[number] == 14:
            return False #banned letter

        if number < 6:
            if data[number+1] == data[number]+1 and data[number+2] == data[number+1]+1:
                straight = True

    #pairs
    pairs = {}
    for key, value in groupby(data):
        if len(list(value)) >= 2:
            pairs[key] = True

    return straight and len(pairs) >= 2


def increment(data):
    data[-1] += 1
    for item in [0, 1, 2, 3, 4, 5, 6, 7]:
        if data[item] > 25:
            data[item - 1] += 1
            data[item] = 0


def numerify(data):
    return [string.ascii_lowercase.index(i) for i in data]

def letterify(data):
    return [string.ascii_lowercase[i] for i in data]

if __name__ == '__main__':
    main()
