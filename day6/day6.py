import re
from math import sqrt

fileName = "day6_data.txt"
sample = "day6_sample.txt"


def readFile1(fn):
    times = []
    distances = []
    with open(fn) as file:
        for line in file:
            line = re.sub(' +', ' ', line)
            type, nums = line.split(':')
            data = nums.strip().split(' ')
            data = list(map(lambda x: int(x), data))
            if type == 'Time':
                times = data
            else:
                distances = data
    return list(zip(times, distances))


def readFile2(fn):
    time = 0
    distance = 0
    with open(fn) as file:
        for line in file:
            line = re.sub(' ', '', line)
            type, nums = line.split(':')
            data = nums.strip()
            data = int(data)
            if type == 'Time':
                time = data
            else:
                distance = data
    return (time, distance)


def part1():
    data = readFile1(fileName)
    waysToDo = []
    for d in data:
        time, distance = d
        ways = 0
        for i in range(time):
            dist = i * (time-i)
            if dist > distance:
                ways += 1
        waysToDo.append(ways)

    ans = 1
    for w in waysToDo:
        ans *= w
    print(f"Part 1: {ans}")


def part2():
    data = readFile2(fileName)
    time, distance = data
    ways = 0
    for i in range(time):
        dist = i * (time-i)
        if dist > distance:
            ways += 1

    print(f"Part 2: {ways}")


def solveEq(a, b, c):
    inside = b**2 - 4*a*c
    minus = (-b - sqrt(inside)) / (2*a)
    plus = (-b + sqrt(inside)) / (2*a)
    return (minus, plus)


def part2Fast():
    data = readFile2(fileName)
    time, distance = data
    zeros = solveEq(-1, time, -distance)  # -x^2 + x*time - distance == 0
    low = int(min(zeros))
    high = int(max(zeros))
    ways = high - low

    print(f"Part 2: {ways}")


if __name__ == '__main__':
    part1()
    # part2()
    part2Fast()
