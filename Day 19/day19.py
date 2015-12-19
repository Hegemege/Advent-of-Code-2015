import itertools, re

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]

    compound = [x for x in re.split("([A-Z][a-z]?)", data[-1]) if x != '']
    
    transformations = { }

    for line in data:
        if line == "":
            break

        parts = line.split(" => ")
        transformations[parts[0]] = parts[1]

    results = set()

    for old, replace in transformations.iteritems():
        copycompound = compound + []

        # Find all combinations of 1 to N of how the compound can be mutated, where N is the count of <old> in compound
        # Replace each
        # Add to results if not there in reverse

        # Pseudocode
        # i = how many times <old> is in compound
        # indices = list of indices for each occurrence
        # for k in xrange(i):
        # for c in itertools.combinations(indices, i):


    print len(results)


if __name__ == '__main__':
    main()
