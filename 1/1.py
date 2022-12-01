def get_cals_per_elf():
    cals = []
    current_elf_cals = 0

    with open("input_1.txt") as f:
        for line in f:
            try:
                current_elf_cals += int(line)
            except:
                cals.append(current_elf_cals)
                current_elf_cals = 0

    return cals

def part1():
    cals = get_cals_per_elf()
    print(max(cals))

def part2():
    cals = get_cals_per_elf()
    top3 = 0
    for _ in range(3):
        top_cal = max(cals)
        top3 += top_cal
        cals.remove(top_cal)
    print(top3)
