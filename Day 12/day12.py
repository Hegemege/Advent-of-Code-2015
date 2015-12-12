import re

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data][0]

    p1 = re.compile("-?[0-9]+")
    print sum(map(int, p1.findall(data)))





if __name__ == '__main__':
    main()
