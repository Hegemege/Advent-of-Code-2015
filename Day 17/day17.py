import itertools

def main():
    data = sorted([33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42])

    count = 0
    for i in xrange(len(data)):
        for comb in itertools.combinations(data, i):
            if sum(comb) == 150:
                count += 1
    print count

if __name__ == '__main__':
   main()
