
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

    #try starting seating from everyone
    for key, value in pref.iteritems():
        smallest = [999999]
        arrange(key, left + [], pref, smallest)


def arrange(cur, left, pref, smallest):
    for name in xrange(len(left)):
        pass


if __name__ == '__main__':
    main()
