import re

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]

    grid = [[False for x in xrange(1000)] for y in xrange(1000)]

    for line in data:
        firstCoord = re.search("\\d", line)
        topleft = line[firstCoord.start():]
        topleft = topleft.split(" ")[0].split(",")
        topleft = [int(x) for x in topleft]

        secondCoord = re.search("through", line)
        bottomright = line[secondCoord.start():].split(" ")[1].split(",")
        bottomright = [int(x) for x in bottomright]

        if "turn on" in line:
            for x in xrange(topleft[0], bottomright[0] + 1):
                for y in xrange(topleft[1], bottomright[1] + 1):
                    grid[x][y] = True
        elif "turn off" in line:
            for x in xrange(topleft[0], bottomright[0] + 1):
                for y in xrange(topleft[1], bottomright[1] + 1):
                    grid[x][y] = False
        elif "toggle" in line:
            for x in xrange(topleft[0], bottomright[0] + 1):
                for y in xrange(topleft[1], bottomright[1] + 1):
                    grid[x][y] = not grid[x][y]

    print sum(map(sum, grid))

if __name__ == '__main__':
    main()