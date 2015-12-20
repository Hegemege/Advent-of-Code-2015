import itertools, re

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]

    compound = [x for x in re.split("([A-Z][a-z]?)", data[-1]) if x != '']
    compoundstr = ''.join(compound)
    
    transformations = [ ]

    for line in data:
        if line == "":
            break

        parts = line.split(" => ")
        transformations.append([parts[0], parts[1]])

    results = set()

    for transform in transformations:
        old = transform[0]
        replace = transform[1]
        # Find all combinations of 1 to N of how the compound can be mutated, where N is the count of <old> in compound
        # Replace each
        # Add to results if not there in reverse
        i = compound.count(old)
        indices = []
        for index, item in enumerate(compound):
            if item == old:
                indices.append(index)
        for index in indices:
            copycompound = compound + []
            copycompound[index] = replace
            copycompound = ''.join(copycompound)
            results.add(copycompound)

    # Make sure compound itself is not in results
    print len(results)

if __name__ == '__main__':
    main()
