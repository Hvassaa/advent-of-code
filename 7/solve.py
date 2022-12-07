dir_sizes = {}
active_dirs = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        e = line.split[" "]
        first = e[0]
        second = e[1]
        if first == "$":
            if second == "cd":
                directory = e[2]
                if directory == "..":
                    active_dirs.pop()
                else:
                    active_dirs.append(directory)
        elif first != "dir":
            for i in range(1, len(active_dirs) + 1):
                curr_dir = str(active_dirs[:i])
                if curr_dir in dir_sizes:
                    dir_sizes[curr_dir] += int(first)
                else:
                    dir_sizes[curr_dir] = int(first)

    # for line in f:
    #     line = line.strip()
        # elems = line.split(" ")
        # f = elems[0]
        # s = elems[1]
        # if f == "$" and s == "cd":
        #     new_dir = elems[2]
        #     if new_dir == "/":
        #         active_dirs = ["/"]
        #     elif new_dir == "..":
        #         active_dirs.pop()
        #     else:
        #         active_dirs.append(new_dir)
        # elif f != "dir" and s != "ls":
        #     for d in active_dirs:
        #         if d in dir_sizes:
        #             dir_sizes[d] += int(f)
        #         else:
        #             dir_sizes[d] = int(f)

def part1():
    print(sum(s for s in dir_sizes.values() if s <= 100000))

def part2():
    pass

part1()
part2()
