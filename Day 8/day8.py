import codecs

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]

    totalSymbols = sum(map(len, data))
 
    f = open("in_fixed.txt", "r")
    data2 = f.readlines()[0]
    f.close()

    realSymbols = len(data2)

    print totalSymbols - realSymbols


    #Part 2
    #reuse data
    data = [x.replace("\\", "\\\\") for x in data]
    data = [x.replace('\"', '\\\"') for x in data]
    data = ["\"" + x + "\"" for x in data]

    encodeSymbols = sum(map(len, data))

    print encodeSymbols - totalSymbols

if __name__ == '__main__':
    main()
