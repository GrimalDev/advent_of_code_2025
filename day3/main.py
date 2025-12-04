def part1():
    with open("day3/input.txt", "r") as f:
        banks = f.read().strip().split("\n")
        bankLen = len(banks[0])

        sum = 0

        for bank in banks:
            digit1, digit2 = "0", "0"
            n = 0
            for digit in bank:
                if digit > digit1 and n < bankLen - 1:
                    digit1 = digit
                    digit2 = "0"
                elif digit > digit2:
                    digit2 = digit
                n += 1
            sum += int(digit1 + digit2)
        return sum


def part2():
    with open("day3/input.txt", "r") as f:
        banks = f.read().strip().split("\n")
        bankLen = len(banks[0])
        nSkip = bankLen - 12

        sum = 0

        for bank in banks:
            start = 0
            batteries = []

            for group in range(12):
                nextStart = start
                end = nSkip + group + 1
                maxDigit = "0"

                for digit in range(start, end):
                    battery = bank[digit]
                    if battery > maxDigit:
                        maxDigit = battery
                        nextStart = digit + 1

                start = nextStart
                batteries.append(maxDigit)
            sum += int("".join(batteries))

        return sum


def main():
    print(f"Part 1: {part1()}, answer: 17435")
    print(f"Part 2: {part2()}, answer: 172886048065379")
