from bitarray import bitarray

def main():
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    data = [x.replace("\n", "") for x in data]

    wires = []
    knownValues = {}

    #add wires according to the file
    for line in data:
        inout = line.split(" -> ")
        command = ""
        if "AND" in line:
            command = " AND "
        elif "OR" in line:
            command = " OR "
        elif "LSHIFT" in line:
            command = " LSHIFT "
        elif "RSHIFT" in line:
            command = " RSHIFT "
        elif "NOT" in line:
            command = "NOT "
        wires.append(Wire(inout[0], command, inout[1]))

    while "a" not in knownValues:
        for wire in wires:
            # Add computed values to known values
            if wire.outputBitArray is not None and wire.outputName not in knownValues:
                knownValues[wire.outputName] = wire.outputBitArray

            if wire.outputName in knownValues:
                continue

            wire.tryMakeBitArrays(knownValues)


    print int(knownValues["a"].to01(), 2)



def leftshift(ba, count):
    return ba[count:] + (bitarray('0') * count)

def rightshift(ba, count):
    return (bitarray('0') * count) + ba[:-count]

def bitfield(n):
    field = [int(digit) for digit in bin(n)[2:]]
    while len(field) < 16:
        field.insert(0, 0)
    return field

class Wire(object):
    def __init__(self, inputName, commandName, outputName):
        self.inputName = inputName
        self.outputName = outputName
        self.commandName = commandName
        self.outputBitArray = None

    def tryMakeBitArrays(self, knownValues):
        try:
            self.outputBitArray = bitarray(bitfield(int(self.inputName)))
        except ValueError:
            #parse command and try again
            try:
                parts = self.inputName.split(self.commandName)

                if len(parts[0]) != 0: #not NOT command
                    arr1 = []
                    arr2 = []
                    if parts[0] in knownValues:
                        arr1 = bitarray(knownValues[parts[0]])
                    if parts[1] in knownValues:
                        arr2 = bitarray(knownValues[parts[1]])

                    if arr1 == []: #first param is value
                        if str(int(parts[0])) == parts[0]:
                            arr1 = bitarray(bitfield(int(parts[0])))
                    if arr2 == []: #second param is value
                        if str(int(parts[1])) == parts[1]:
                            arr2 = bitarray(bitfield(int(parts[1])))

                    #exception before this point if something is wrong :-D
                    if self.commandName == " AND ":
                        self.outputBitArray = arr1 & arr2
                    elif self.commandName == " OR ":
                        self.outputBitArray = arr1 | arr2
                    elif self.commandName == " LSHIFT ": #second parameter always a value
                        self.outputBitArray = leftshift(arr1, int(parts[1]))
                    elif self.commandName == " RSHIFT ": #second parameter always a value
                        self.outputBitArray = rightshift(arr1, int(parts[1]))

                else: #NOT command
                    if parts[1] in knownValues: #known value
                        temp = bitarray(16) #invert() doesnt work :/
                        temp.setall(True)
                        self.outputBitArray = knownValues[parts[1]] ^ temp
                    elif str(int(parts[1])) == parts[1]: #try int()
                        temp = bitarray(16) #invert() doesnt work :/
                        temp.setall(True)
                        self.outputBitArray = bitarray(bitfield(int(parts[1]))) ^ temp

            except ValueError:
                if self.commandName == "": #no command
                    if self.inputName in knownValues:
                        self.outputBitArray = knownValues[self.inputName]





if __name__ == '__main__':
    main()