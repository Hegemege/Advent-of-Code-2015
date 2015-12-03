

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = data[0] #single line, readlines() returns a list

    grid = {}
    x = 0
    y = 0
    grid[(0, 0)] = 1

    for symbol in data:
        if symbol == '<':
            x -= 1
        elif symbol == '>':
            x += 1
        elif symbol == '^':
            y -= 1
        elif symbol == 'v':
            y += 1

        if (x, y) not in grid:
            grid[(x, y)] = 1
        else:
            grid[(x, y)] += 1

    print len(grid)


if __name__ == '__main__':
    main()