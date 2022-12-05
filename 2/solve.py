w = {
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3
}

o = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

def part1():
    score = 0
    with open("input.txt") as f:
        for line in f:
            l = line.split(" ")
            you = w[l[0][0]]
            me = w[l[1][0]]
            score += me
            if you + me == 4:
                me = me % 3
                you = you % 3
            if me == you:
                score += 3
            elif me > you:
                score += 6
    print(score)

def part2():
    score = 0
    with open("input.txt") as f:
        for line in f:
            l = line.split(" ")
            you = w[l[0][0]]
            outcome = l[1][0]
            score += o[outcome]
            if outcome == "X":
                me = you - 1
                if me == 0:
                    score += 3
                else:
                    score += me
            elif outcome == "Y":
                score += you
            else:
                me = you + 1
                # score += me % 3
                if me == 4:
                    score += 1
                else:
                    score += me
    print(score)

part1()
part2()
