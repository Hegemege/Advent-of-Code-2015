from itertools import groupby

def main():
    data = "3113322113"

    for i in xrange(40):
        data = ''.join(str(len(list(value))) + key for key, value in groupby(data))

    print len(data)


if __name__ == '__main__':
    main()
