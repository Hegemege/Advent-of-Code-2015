import re

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]

    nice = 0

    p1 = re.compile('(.*([aeiou]).*){3,}') #match any three vowels anywhere
    p2 = re.compile('.*([a-z])\\1+.*') #match double letter
    p3 = re.compile('.*((ab)|(cd)|(pq)|(xy)).*') #match the combinations

    for line in data:
        nice += (p1.match(line) is not None) and (p2.match(line) is not None) and (p3.match(line) is None)

    print nice

    #Part 2

    nice = 0

    p1 = re.compile('.*([a-z][a-z])[a-z]*\\1.*')
    p2 = re.compile('.*([a-z])[a-z]\\1.*')

    for line in data:
        nice += (p1.match(line) is not None) and (p2.match(line) is not None)

    print nice


if __name__ == '__main__':
    main()