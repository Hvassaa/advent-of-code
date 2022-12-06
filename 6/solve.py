s = ""

with open("input.txt") as f:
    for l in f:
        s = l.strip()

def fn(num: int):
    k = ["a" for _ in range(num)]
    for idx, c in enumerate(s):
        k[idx % num] = c
        if len(set(k)) == num and idx >= num:
            print(idx + 1)
            break

        
def part1():
    fn(4)

def part2():
    fn(14)

part1()
part2()
