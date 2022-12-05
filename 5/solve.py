import re

def part1():
    with open("input.txt") as f:
        crates = []
        s = []
        commands = []
        for line in f:
            line = line.strip("\n")
            if "[" in line: # collect lines with crates
                crates.append(line)
            elif "move" in line: # collect commands on how to move the crates
                commands.append(tuple([int(x) - 1 for x in re.findall(r"\d+", line)]))
            elif "1" in line: # use the "indexing" line to find indices in crates lines
                nums = len(re.findall(r"\d", line))
                for i in range(nums):
                    r = 1 + 4 * i
                    s.append([])
                    for c in crates: 
                        m = c[r].strip()
                        if m:
                            s[i].append(c[r])

        for a in s: # reverse the lists, so we can use them like stacks
            a.reverse()

        for amount, f, t in commands: # do the moves
            for _ in range(amount + 1):
                s[t].append(s[f].pop())

        # pretty print
        res = "" 
        for a in s:
            res += a.pop()

        print(res)

def part2():
    with open("input.txt") as f:
        crates = []
        s = []
        commands = []
        for line in f:
            line = line.strip("\n")
            if "[" in line:
                crates.append(line)
            elif "move" in line:
                commands.append(tuple([int(x) - 1 for x in re.findall(r"\d+", line)]))
            elif "1" in line:
                nums = len(re.findall(r"\d", line))
                for i in range(nums):
                    r = 1 + 4 * i
                    s.append([])
                    for c in crates:
                        m = c[r].strip()
                        if m:
                            s[i].append(c[r])

        for a in s:
            a.reverse()
        
        for amount, f, t in commands:
            tomove = []
            # trick for part, collect what is to be moved as before
            # but then reverse it and finnaly push to the other stack
            for _ in range(amount + 1):
                tomove.append(s[f].pop())
            tomove.reverse()
            for q in tomove:
                s[t].append(q)

        res = ""
        for a in s:
            res += a.pop()

        print(res)

part1()
part2()
