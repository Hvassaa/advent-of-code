trees = []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        trees.append([int(x) for x in line])

def part1():
    seen = set()
    for y in range(len(trees)):
        for x in range(len(trees[0])):
            if x == 0 or x == len(trees[0]) - 1:
                seen.add((x, y))
            else:
                can_see_l = True
                can_see_r = True
                for xx in range(x):
                    if trees[y][xx] >= trees[y][x]:
                        can_see_l = False
                        break
                for xx in range(len(trees[0]) - 1, x, -1):
                    if trees[y][xx] >= trees[y][x]:
                        can_see_r = False
                        break
                if can_see_l or can_see_r:
                    seen.add((x,y))
    for x in range(len(trees[0])):
        for y in range(len(trees)):
            if y == 0 or y == len(trees) - 1:
                seen.add((x, y))
            else:
                can_see_l = True
                can_see_r = True
                for yy in range(y):
                    if trees[yy][x] >= trees[y][x]:
                        can_see_l = False
                        break
                for yy in range(len(trees) - 1, y, -1):
                    if trees[yy][x] >= trees[y][x]:
                        can_see_r = False
                        break
                if can_see_l or can_see_r:
                    seen.add((x,y))

    print(len(seen))


def part2():
    best = -1
    for y in range(len(trees)):
        if y == 0 or y == len(trees) - 1:
            continue
        for x in range(len(trees[0])):
            if x == 0 or x == len(trees[0]) - 1:
                continue
            curr_tree = trees[y][x]
            left = 0
            for xx in range(x-1, -1, -1):
                left += 1
                if trees[y][xx] >= curr_tree:
                    break
            right = 0
            for xx in range(x+1, len(trees[0])):
                right += 1
                if trees[y][xx] >= curr_tree:
                    break
            up = 0
            for yy in range(y-1, -1, -1):
                up += 1
                if trees[yy][x] >= curr_tree:
                    break
            down = 0
            for yy in range(y+1, len(trees[0])):
                down += 1
                if trees[yy][x] >= curr_tree:
                    break
            score = left * right * up * down
            if score > best:
                best = score
            

    print(best)


part1()
part2()
