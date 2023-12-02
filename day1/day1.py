fileName = "day1_data.txt"

def part1():
    totalSum = 0

    with open(fileName) as file:
        for line in file:
            line = line.strip()
            valueString = ""
            for c in line:
                if c.isnumeric():
                    valueString += c
                    break
            for c in line[::-1]:
                if c.isnumeric():
                    valueString += c
                    break
            valueNum = int(valueString)
            totalSum += valueNum

    print(f"Part 1: {totalSum}")

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def parseNum(string: str, index: int, reversed=False):
    for i, num in enumerate(nums, 1):
        if not reversed:
            if string.find(num, index) == index:
                return i
        else:
            if string.find(num[::-1], index) == index:
                return i
    if string[index].isnumeric():
        return int(string[index])
    return None


def part2():
    totalSum = 0

    with open(fileName) as file:
        for line in file:
            line = line.strip()
            valueString = ""
            for i in range(len(line)):
                res = parseNum(line, i)
                if res is not None:
                    valueString += str(res)
                    break
            line = line[::-1]
            for i in range(len(line)):
                res = parseNum(line, i, True)
                if res is not None:
                    valueString += str(res)
                    break
            valueNum = int(valueString)
            totalSum += valueNum

    print(f"Part 2: {totalSum}")
    

if __name__ == "__main__":
    part1()
    part2()
