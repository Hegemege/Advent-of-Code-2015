
def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]

    grid = []

    for line in data:
        grid.append([True if x == "#" else False for x in line])

    for i in xrange(100):
        grid = newState(grid)

    print sum(map(sum, grid))

def newState(old):
    new = [[False for x in xrange(100)] for y in xrange(100)]

    for x in xrange(len(old)):
        for y in xrange(len(old[x])):
            neighbors = getNeighborSum(old, x, y)
            if old[x][y]:
                if neighbors == 2 or neighbors == 3:
                    new[x][y] = True
            else:
                if neighbors == 3:
                    new[x][y] = True
    return new

def getNeighborSum(data, x, y):
    count = 0
    if x > 0:
        if y > 0:
            if data[x-1][y-1]:
                count += 1
        if y < len(data[0]) - 1:
            if (data[x-1][y+1]):
                count += 1
        if data[x-1][y]:
            count += 1
    if x < len(data) - 1:
        if y > 0:
            if data[x+1][y-1]:
                count += 1
        if y < len(data[0]) - 1:
            if data[x+1][y+1]:
                count += 1
        if data[x+1][y]:
            count += 1
    if y > 0:
        if data[x][y-1]:
            count += 1
    if y < len(data[0]) - 1:
        if data[x][y+1]:
            count += 1
    return count


if __name__ == '__main__':
    main()
