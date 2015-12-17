
def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    message = { "children": 3,
                "cats" : 7,
                "samoyeds" : 2,
                "pomeranians" : 3,
                "akitas" : 0,
                "vizslas" : 0,
                "goldfish" : 5,
                "trees" : 3,
                "cars" : 2,
                "perfumes" : 1 }

    data = [x.replace("\n", "") for x in data]

    sues = []
    for line in data:
        sues.append( Sue(line) )

    index = 0
    for sue in sues:
        index += 1
        count = 0
        for item, value in message.iteritems():
            if sue.features[item] == value:
                count += 1
        if count >= 3:
            print index
            return


class Sue(object):
    def __init__(self, line):
        self.features = { }
        self.features["children"] = -1
        self.features["cats"] = -1
        self.features["samoyeds"] = -1
        self.features["pomeranians"] = -1
        self.features["akitas"] = -1
        self.features["vizslas"] = -1
        self.features["goldfish"] = -1
        self.features["trees"] = -1
        self.features["cars"] = -1
        self.features["perfumes"] = -1

        tline = line.split(" ")[2:]
        tline = [x.replace(":","") for x in tline]
        tline = [x.replace(",","") for x in tline]

        self.features[tline[0]] = int(tline[1])
        self.features[tline[2]] = int(tline[3])
        self.features[tline[4]] = int(tline[5])

if __name__ == '__main__':
    main()
