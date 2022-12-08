dir_sizes = {}
active_dirs = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        e = line.split(" ")
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

def part1():
    sum = 0
    for size in dir_sizes.values():
        if size <= 100000:
            sum += size
    print(sum)

def part2():
    fs_size = dir_sizes["['/']"]
    total = 70000000
    need = 30000000
    unused = total - fs_size
    best = None
    for size in dir_sizes.values():
        if unused + size >= need and (best == None or size < best):
            best = size
    print(best)


part1()
part2()
