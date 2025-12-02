def main():
    result1 = 0
    result2 = 0
    dial = 50
    with open("day1/input.txt", "r") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            sign = 2 * int(line[0] == "R") - 1
            rotations = int(line[1:])

            newDial = dial + sign * rotations

            if sign == 1:
                result2 += newDial // 100
            else:
                result2 += -((newDial - 1) // 100) - (1 if dial == 0 else 0)

            dial = newDial % 100

            if dial == 0:
                result1 += 1

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")
