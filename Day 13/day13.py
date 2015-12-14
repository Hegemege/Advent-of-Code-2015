
def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]
    data = [x.replace(".", "") for x in data]
    names = set([x.split(" ")[0] for x in data])

    pref = {name: {} for name in names} #dict comprehension

    #parse
    for line in data:
        parts = line.split(" ")
        hapdiff = (1 if parts[2] == "gain" else -1)*int(parts[3])
        source = parts[0]
        target = parts[10]
        pref[source][target] = hapdiff

    left = list(names)

    highest = [-99999]
    starter = pref.iterkeys().next()
    arrange(starter, [starter], left + [], pref, highest)

    print highest


    #Part 2

    for key, value in pref.iteritems():
        value["Me"] = 0

    pref["Me"] = { name : 0 for name in left }

    left.append("Me")
    highest = [-99999]
    starter = pref.iterkeys().next()
    arrange(starter, [starter], left + [], pref, highest)

    print highest


def arrange(cur, builder, left, pref, highest):
    curindex = left.index(cur)
    templeft = left[:curindex] + left[curindex+1:]
    if len(templeft) > 0:
        for name in xrange(len(templeft)):
            arrange(templeft[name], builder + [templeft[name]], templeft, pref, highest)
    else:
        total = 0
        for i in xrange(len(builder)):
            thisname = builder[i]
            prevname = builder[i-1]
            nextname = builder[(i+1)%len(builder)]

            total += pref[thisname][prevname]
            total += pref[thisname][nextname]
        if total > highest[0]:
            highest[0] = total


if __name__ == '__main__':
    main()
