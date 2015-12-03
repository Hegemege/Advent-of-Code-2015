

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    total = 0
    totalRibbon = 0

    for line in data:
        dims = map(lambda x: int(x), line.split("x"))
        areas = getAreas(*dims)
        smallest = min(areas)
        total += sum([x*2 for x in areas])
        total += smallest

        totalRibbon += getRibbon(*dims)

    print total
    print totalRibbon


def getAreas(l, w, h):
    return [l*w, w*h, h*l]

def getRibbon(l, w, h):
    tl = [l, w, h]
    tl.remove(max(tl))
    tl = [x*2 for x in tl]
    return sum(tl) + l*w*h

if __name__ == '__main__':
    main()