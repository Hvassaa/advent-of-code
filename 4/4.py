elf_pairs = []
with open("input_4.txt") as f:
    for line in f:
        line = line.strip().replace(",", "-")
        e = tuple([int(x) for x in line.split("-")])
        elf_pairs.append(e)

def in_range(x, start, end):
    return x >= start and x <= end

def part1():
    res = 0
    for p in elf_pairs:
        if (p[0] >= p[2] and p[1] <= p[3]) or (p[2] >= p[0] and p[3] <= p[1]):
            res += 1
    print(res)

def part2():
    res = 0
    for p in elf_pairs:
        if in_range(p[0], p[2], p[3]) or in_range(p[1], p[2], p[3]) or in_range(p[2], p[0], p[1]) or in_range(p[3], p[0], p[1]):
            res += 1
    print(res)

part1()
part2()
