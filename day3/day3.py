fileName = "day3_data.txt"

lastAdded = 0


def isSymbol(char: str):
    return char != '.' and not char.isnumeric()


def selectNumber(string: str, index: int):
    if index < 0 or index > len(string):
        return 0
    if not string[index].isnumeric():
        return 0
    startIndex = index
    endIndex = index
    while startIndex > 0:
        if string[startIndex-1].isnumeric():
            startIndex = startIndex - 1
        else:
            break
    while endIndex < len(string) - 1:
        if string[endIndex+1].isnumeric():
            endIndex = endIndex + 1
        else:
            break
    numString = string[startIndex:endIndex+1]
    num = int(numString)
    global lastAdded
    if lastAdded != num:
        lastAdded = num
        return num
    else:
        return 0


def part1():
    data = []
    numberSum = 0

    with open(fileName) as file:
        for line in file:
            line = line.strip()
            data.append(line)

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if isSymbol(char):
                for m in range(i-1, i+2):
                    for n in range(j-1, j+2):
                        numberSum += selectNumber(data[m], n)

    print(f"Part 1: {numberSum}")


def part2():
    data = []
    numberSum = 0

    with open(fileName) as file:
        for line in file:
            line = line.strip()
            data.append(line)

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == '*':
                foundValues = []
                for m in range(i-1, i+2):
                    for n in range(j-1, j+2):
                        found = selectNumber(data[m], n)
                        if found != 0:
                            foundValues.append(found)
                if len(foundValues) == 2:
                    numberSum += foundValues[0] * foundValues[1]

    print(f"Part 2: {numberSum}")


if __name__ == "__main__":
    part1()
    part2()
