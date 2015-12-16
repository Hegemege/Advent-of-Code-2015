import operator
import functools

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]

    ing = []

    for line in data:
        parts = line.split(":")
        name = parts[0]
        attrs = parts[1].split(",")
        tingredient = []
        for attr in attrs:
            parts = attr.split(" ")
            tingredient.append(int(parts[2]))

        ing.append(tingredient)

    maxscore = 0

    for i in xrange(100):
        for j in xrange(100 - i):
            for k in xrange(100 - i - j):
                l = 100 - i - j - k

                factors = [i, j, k, l]
                sums = [0,0,0,0,0]
                for ingr in xrange(4):
                    for item in xrange(5):
                        sums[item] += ing[ingr][item] * factors[ingr]

                if len(filter(lambda x: x <= 0, sums)) > 0:
                    continue

                # Part 2
                if sums[-1] != 500:
                    continue

                score = functools.reduce(operator.mul, sums[:-1], 1)
                if score > maxscore:
                    maxscore = score
    
    print maxscore

if __name__ == '__main__':
    main()
