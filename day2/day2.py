fileName = "day2_data.txt"

redLimit = 12
greenLimit = 13
blueLimit = 14


def part1():
    gameSum = 0

    with open(fileName) as file:
        for line in file:
            line = line.strip()
            game, gameData = line.split(':')
            hands = gameData.split(';')
            isPossible = True

            for hand in hands:
                amounts = {'red': 0, 'green': 0, 'blue': 0}
                cubes = hand.split(',')
                for cube in cubes:
                    cube = cube.strip()
                    amount, color = cube.split(' ')
                    amounts[color] += int(amount)

                if amounts['red'] > redLimit or amounts['green'] > greenLimit or amounts['blue'] > blueLimit:
                    isPossible = False
                    break

            if not isPossible:
                continue

            gameParts = game.split(' ')
            gameNum = int(gameParts[1])
            gameSum += gameNum
    print(f"Part 1: {gameSum}")


def part2():
    gameSum = 0

    with open(fileName) as file:
        for line in file:
            line = line.strip()
            game, gameData = line.split(':')
            hands = gameData.split(';')
            amounts = {'red': 0, 'green': 0, 'blue': 0}

            for hand in hands:
                cubes = hand.split(',')
                for cube in cubes:
                    cube = cube.strip()
                    amount, color = cube.split(' ')
                    if int(amount) > amounts[color]:
                        amounts[color] = int(amount)

            gameSum += amounts['red'] * amounts['green'] * amounts['blue']

    print(f"Part 2: {gameSum}")


if __name__ == "__main__":
    part1()
    part2()
