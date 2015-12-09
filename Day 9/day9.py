import copy

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]

    cities = { }

    for line in data:
        dims = line.split(" = ")
        dist = int(dims[1])
        fromCity = dims[0].split(" to ")[0]
        toCity = dims[0].split(" to ")[1]

        if fromCity not in cities:
            cities[fromCity] = {}
        cities[fromCity][toCity] = dist

        if toCity not in cities:
            cities[toCity] = {}
        cities[toCity][fromCity] = dist

    for key, value in cities.iteritems(): #start from any city
        shortest = [99999]
        traverseFrom(cities, key, [key], 0, shortest)
        print key, shortest

    # Part 2

    print "---------"

    for key, value in cities.iteritems():
        longest = [0]
        traverseFromLong(cities, key, [key], 0, longest)
        print key, longest


def traverseFrom(cities, cityname, visited, s, shortest):
    for key, value in cities[cityname].iteritems():
        if key in visited:
            continue
        traverseFrom(cities, key, visited + [key], s + value, shortest)

    if len(visited) == len(cities):
        if s < shortest[0]:
            shortest[0] = s

def traverseFromLong(cities, cityname, visited, s, longest):
    for key, value in cities[cityname].iteritems():
        if key in visited:
            continue
        traverseFromLong(cities, key, visited + [key], s + value, longest)

    if len(visited) == len(cities):
        if s > longest[0]:
            longest[0] = s

if __name__ == '__main__':
    main()
