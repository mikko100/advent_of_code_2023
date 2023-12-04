import re
from time import perf_counter_ns

fileName = "day4_data.txt"


def part1():
    totalSum = 0

    with open(fileName) as file:
        for line in file:
            game, nums = line.split(':')
            nums = re.sub(' +', ' ', nums)
            win, have = nums.split('|')
            win = win.strip()
            have = have.strip()
            winNums = win.split(' ')
            haveNums = have.split(' ')
            matching = 0
            for h in haveNums:
                if h in winNums:
                    matching += 1
            if matching > 0:
                totalSum += 2 ** (matching - 1)

    print(f"Part 1: {totalSum}")


gameTotals = {}


def countWins(games, gameNum):
    if gameNum >= len(games):
        return 0
    if gameNum in gameTotals:
        return gameTotals[gameNum]
    else:
        win, have = games[gameNum]
        count = 1
        matches = 0
        for h in have:
            if h in win:
                matches += 1
                count += countWins(games, gameNum + matches)
        gameTotals[gameNum] = count
        return count


def part2():
    totalSum = 0
    games = []

    with open(fileName) as file:
        for line in file:
            game, nums = line.split(':')
            nums = re.sub(' +', ' ', nums)
            win, have = nums.split('|')
            win = win.strip()
            have = have.strip()
            winNums = win.split(' ')
            haveNums = have.split(' ')
            games.append((winNums, haveNums))

    for i in range(len(games)):
        totalSum += countWins(games, i)

    print(f"Part 2: {totalSum}")


if __name__ == '__main__':
    part1()
    start = perf_counter_ns()
    part2()
    end = perf_counter_ns()
    total = end - start
    print(f"Time taken: {total/1000000:.2f}ms")
