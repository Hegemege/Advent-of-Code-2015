
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
        status = True

        reindeer[name] = [status, speed, flytime, resttime, distance]

    for key, value in reindeer.iteritems():
        fly(value, finish)

    print max([value[4] for key, value in reindeer.iteritems()])

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
        

if __name__ == '__main__':
    main()
