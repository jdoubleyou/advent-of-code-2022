def part_one(puzzle_input: str):
    pairs = puzzle_input.strip().split("\n")
    count = 0
    for pair in pairs:
        first, second = pair.split(",")
        f1, f2 = first.split("-")
        f1, f2 = int(f1), int(f2)
        s1, s2 = second.split("-")
        s1, s2 = int(s1), int(s2)

        if (f1 <= s1 and f2 >= s2) or (s1 <= f1 and s2 >= f2):
            count += 1
    return count


def part_two(puzzle_input: str):
    pairs = puzzle_input.strip().split("\n")
    count = 0
    for pair in pairs:
        first, second = pair.split(",")
        f1, f2 = first.split("-")
        f1, f2 = int(f1), int(f2)
        s1, s2 = second.split("-")
        s1, s2 = int(s1), int(s2)

        if (f1 <= s1 and f2 >= s2) or (s1 <= f1 and s2 >= f2):
            count += 1
        elif (f2 >= s1 and f1 <= s1) or (s2 >= f1 and s1 <= f1):
            count += 1
    return count
