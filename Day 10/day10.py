from itertools import groupby

def main():
    for part in [40, 50]:
        data = "3113322113"
        for i in xrange(part):
            data = ''.join(str(len(list(value))) + key for key, value in groupby(data))

        print len(data)


if __name__ == '__main__':
    main()
