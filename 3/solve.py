l = ord("a") - 1
u = ord("A") - 27

def part1():
    sum = 0
    with open("input.txt") as f:
        for line in f:
            rucksack = line.strip()
            lengthhalf = len(rucksack) // 2
            c1 = rucksack[0 : lengthhalf]
            c2 = rucksack[lengthhalf:]
            for c in c1:
                if c in c2:
                    if c.isupper():
                        sum += ord(c) - u
                    else:
                        sum += ord(c) - l
                    break
    print(sum)

def part2():
    sum = 0
    with open("input.txt") as f:
        lines = f.readlines()
        no_of_lines = len(lines)
        for i in range(0, len(lines), 3):
            l1 = lines[i].strip()
            l2 = lines[i + 1].strip()
            l3 = lines[i + 2].strip()
            for c in l1:
                if c in l2 and c in l3:
                    if c.isupper():
                        sum += ord(c) - u
                    else:
                        sum += ord(c) - l
                    break
    print(sum)

part1()
part2()
