
def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]
    finish = 2503 #from problem page input
    reindeer = { }

    for line in data:
        parts = line.split(" ")
        name = parts[0]
        speed = int(parts[3])
        flytime = int(parts[6])
        resttime = int(parts[13])
        distance = 0
        distanceAt = []
        status = True

        reindeer[name] = [status, speed, flytime, resttime, distance, distanceAt]

    for key, value in reindeer.iteritems():
        fly(value, finish)

    print max([value[4] for key, value in reindeer.iteritems()])

    #Part 2

    points = { key : 0 for key, value in reindeer.iteritems() }
    for second in xrange(finish):
        tops = []
        for key, value in reindeer.iteritems():
            if len(tops) == 0:
                tops = [key]
            else:
                if reindeer[tops[0]][5][second] < reindeer[key][5][second]:
                    tops = [key]
                elif reindeer[tops[0]][5][second] == reindeer[key][5][second]:
                    tops.append(key)

        for top in tops:
            points[top] += 1

    print max([value for key, value in points.iteritems()])

def fly(data, time):
    counter = data[2]
    for i in xrange(time):
        counter -= 1

        if (data[0]): #flying
            data[4] += data[1]
            if (counter == 0): #gotta rest
                counter = data[3]
                data[0] = False
                
        else: #resting
            if (counter == 0):
                counter = data[2]
                data[0] = True

        data[5].append(data[4])
        

if __name__ == '__main__':
    main()
