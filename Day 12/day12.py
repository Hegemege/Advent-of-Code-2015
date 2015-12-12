import re
import json

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data][0]

    p1 = re.compile("-?[0-9]+")
    print sum(map(int, p1.findall(data)))

    jsonobj = json.loads(data)
    print walk(jsonobj)


def walk(data):
    try:
        if type(data) is list:
            totalsum = 0
            for value in data:
                totalsum += walk(value)
            return totalsum
            #return sum(map(int, filter(lambda x: x == True, [x.isdigit() for x in data])))
        elif type(data) is dict:
            for key, value in data.iteritems():
                if value == "red":
                    return 0
            totalsum = 0
            for key, value in data.iteritems():
                totalsum += walk(value)
            return totalsum
        elif type(data) is int:
            return data
    except ValueError as e:
        pass
    return 0


if __name__ == '__main__':
    main()
