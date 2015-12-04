import hashlib

def main():
    data = "bgvyzdsv"

    index = 1

    while(True):
        d = hashlib.md5()
        d.update(data + str(index))
        if (d.hexdigest()[:5] == "00000"):
            break
        index += 1

    print index

if __name__ == '__main__':
    main()