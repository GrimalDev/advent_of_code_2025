def part1():
    patternSum = 0
    with open("day2/input.txt", "r") as f:
        content = f.read().strip().replace("\n", "")
        rangesN = content.split(",")

        for rangeN in rangesN:
            if not rangeN:
                continue

            start, end = rangeN.split("-")

            for idLen in range(len(start), len(end) + 1):

                if idLen % 2 != 0:
                    continue

                halfIdLen = idLen // 2

                halfStart = int("1" + "0" * (halfIdLen - 1))
                halfEnd = int("9" * halfIdLen)

                if idLen == len(start):
                    halfStart = max(halfStart, int(start[:halfIdLen]))

                if idLen == len(end):
                    halfEnd = min(halfEnd, int(end[:halfIdLen]))

                for number in range(halfStart, halfEnd + 1):
                    pattern = int(str(number) * 2)

                    if pattern >= int(start) and pattern <= int(end):
                        patternSum += pattern

    return patternSum


def part2():
    patternSum = 0
    with open("day2/input.txt", "r") as f:
        content = f.read().strip().replace("\n", "")
        rangesN = content.split(",")

        for rangeN in rangesN:
            if not rangeN:
                continue

            start, end = rangeN.split("-")

            uniquePatternsInRange = set()

            for idLen in range(max(2, len(start)), len(end) + 1):

                for repeats in [*range(2, (idLen // 2) + 1), idLen]:
                    if idLen % repeats != 0:
                        continue

                    partLen = idLen // repeats

                    partStart = int("1" + "0" * (partLen - 1))
                    partEnd = int("9" * partLen)

                    if idLen == len(start):
                        partStart = max(partStart, int(start[:partLen]))

                    if idLen == len(end):
                        partEnd = min(partEnd, int(end[:partLen]))

                    for number in range(partStart, partEnd + 1):
                        pattern = int(str(number) * repeats)
                        print(pattern)

                        if pattern >= int(start) and pattern <= int(end):
                            uniquePatternsInRange.add(pattern)

            patternSum += sum(uniquePatternsInRange)

    return patternSum


def main():
    print(f"Part 1: {part1()}, answer: 23534117921")
    print(f"Part 2: {part2()}, answer: 31755323497")
