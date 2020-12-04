# Does part 1 and 2!

inputs = []

with open("inputs/day3.input", "r") as i_file:
    inputs = i_file.readlines()

# We're getting a bunch of newlines at the end of each line
map = []
for i in inputs:
    map += [i.strip()]

# We could make classes which return true for tree, false for empty, but let's
# be lazy

def count_trees(map, x_move, y_move):
    # We always move x_moves to the right, y_move down
    x = 0
    y = 0
    trees = 0
    while y < len(map):
        if map[y][x] == "#":
            trees += 1
        x = (x + x_move) % (len(map[y]))
        y += y_move
    return trees

r1d1 = count_trees(map, 1, 1)
r3d1 = count_trees(map, 3, 1)
r5d1 = count_trees(map, 5, 1)
r7d1 = count_trees(map, 7, 1)
r1d2 = count_trees(map, 1, 2)

print("Part 1: " + str(r3d1) + "\n")

p2 = r1d1 * r3d1 * r5d1 * r7d1 * r1d2

print("Part 2: " + str(p2))
