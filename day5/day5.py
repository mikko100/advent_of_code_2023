fileName = "day5_data.txt"
sampleFile = "day5_sample.txt"


def readFile(fn):
    seeds = []
    maps = []

    with open(fn) as file:
        mapValues = []
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            if line.startswith('seeds'):
                _, nums = line.split(':')
                nums = nums.strip()
                seedStrings = nums.split(' ')
                seeds = list(map(lambda x: int(x), seedStrings))
            elif line[0].isalpha():
                if len(mapValues) > 0:
                    maps.append(mapValues)
                mapValues = []
            else:
                valueString = line.split(' ')
                values = list(map(lambda x: int(x), valueString))
                mapValues.append(values)
        maps.append(mapValues)
    return (seeds, maps)


def sourceToDest(valueMap, sourceVal):
    for m in valueMap:
        destination, source, rangeLen = m
        if source <= sourceVal < source + rangeLen:
            offset = sourceVal - source
            return destination + offset
    return sourceVal


def part1():
    seeds, maps = readFile(fileName)
    lowestLocation = None
    for s in seeds:
        source = s
        for m in maps:
            source = sourceToDest(m, source)
        if lowestLocation is None or source < lowestLocation:
            lowestLocation = source
    print(f"Part 1: {lowestLocation}")


def seedsToRanges(seeds):
    seedRanges = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        end = start + seeds[i+1]
        seedRanges.append([start, end])
    return seedRanges


def part2():
    # seedPairs, maps = readFile(sampleFile)
    seedPairs, maps = readFile(fileName)
    seedRanges = seedsToRanges(seedPairs)
    valuesToProcess = 0
    for s, e in seedRanges:
        valuesToProcess += e-s
    lowestLocation = None
    for start, end in seedRanges:
        for s in range(start, end):
            source = s
            for m in maps:
                source = sourceToDest(m, source)
            if lowestLocation is None or source < lowestLocation:
                lowestLocation = source
    print(f"Part 2: {lowestLocation}")


def part2Fast():
    # seedPairs, maps = readFile(sampleFile)
    seedPairs, maps = readFile(fileName)
    seedRanges = seedsToRanges(seedPairs)
    for map in maps:
        newSeeds = []
        while len(seedRanges) > 0:
            start, end = seedRanges.pop()
            for dest, sour, step in map:
                overlapStart = max(start, sour)
                overlapEnd = min(end, sour + step)
                if overlapStart < overlapEnd:
                    newSeeds.append(
                        (overlapStart - sour + dest, overlapEnd - sour + dest))
                    if overlapStart > start:
                        seedRanges.append((start, overlapStart))
                    if end > overlapEnd:
                        seedRanges.append((overlapEnd, end))
                    break
            else:
                newSeeds.append((start, end))
        seedRanges = newSeeds
    lowestLocation = min(seedRanges)[0]
    print(f"Part 2: {lowestLocation}")


if __name__ == '__main__':
    part1()
    # part2()
    part2Fast()
