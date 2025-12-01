def main():

    result1 = 0
    dial = 50
    with open("day1/input.txt", "r") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            sign = 2 * int(line[0] == "R") - 1
            rotations = int(line[1:])
            dial = (dial + sign * rotations) % 100
            print(dial)
            if dial == 0:
                result1 += 1

    # Part 2
    result2 = 0

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")
