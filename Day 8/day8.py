import codecs

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]

    totalSymbols = sum(map(len, data))
 
    f = open("in_fixed.txt", "r")
    data = f.readlines()[0]
    f.close()

    realSymbols = len(data)

    print totalSymbols - realSymbols


if __name__ == '__main__':
    main()
