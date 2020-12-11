# Does part 1 and 2!

inputs = []

with open("inputs/day11.input", "r") as i_file:
    inputs = i_file.readlines()

class ChairAutomata:
    def __init__(self, inputs):
        self.layout = []
        for i in inputs:
            if i.strip() == "":
                break
            line = []
            for j in i.strip():
                line += [j]
            self.layout += [line]

    def count_nearby(self, old, i, j):
        filled = 0
        above = i - 1
        if i == 0:
            above = i
        below = i + 1
        if i == len(self.layout) - 1:
            below = i
        left = j - 1
        if j == 0:
            left = j
        right = j + 1
        if j == len(self.layout[i]) - 1:
            right = j
        for x in range(above, below+1):
            for y in range(left, right+1):
                if x == i and y == j:
                    continue
                if old[x][y] == "#":
                    filled += 1
        
        return filled

    def count_in_view(self, old, i, j):
        filled = 0
        # Look along the straights first
        for x in range(i-1, -1, -1):
            if old[x][j] == "L":
                break
            elif old[x][j] == "#":
                filled += 1
                break
        for x in range(i+1, len(old)):
            if old[x][j] == "L":
                break
            elif old[x][j] == "#":
                filled += 1
                break
        for y in range(j-1, -1, -1):
            if old[i][y] == "L":
                break
            elif old[i][y] == "#":
                filled += 1
                break
        for y in range(j+1, len(old[i])):
            if old[i][y] == "L":
                break
            elif old[i][y] == "#":
                filled += 1
                break

        # Now do the diagonals
        for x_change in range(-1, 3, 2):
            for y_change in range(-1, 3, 2):
                x = i
                y = j
                while x + x_change >= 0 and y + y_change >= 0 and x + x_change <= len(old)-1 and y + y_change <= len(old[x])-1:
                    x += x_change
                    y += y_change
                    if old[x][y] == "L":
                        break
                    elif old[x][y] == "#":
                        filled += 1
                        break
        
        return filled


    def progress(self, new=False):
        old = []
        for i in self.layout:
            old += [ i.copy() ]
        changed = 0

        for i in range(0, len(self.layout)):
            for j in range(0, len(self.layout[i])):
                if old[i][j] == ".":
                    continue
                elif old[i][j] == "L":
                    # This may change if we can't find any filled seats nearby
                    if not new:
                        filled = self.count_nearby(old, i, j)
                    else:
                        filled = self.count_in_view(old, i, j)
                    if filled == 0:
                        self.layout[i][j] = "#"
                        changed += 1
                elif old[i][j] == "#":
                    # This will change if we have four seats adjacent that are
                    # full
                    if not new:
                        filled = self.count_nearby(old, i, j)
                    else:
                        filled = self.count_in_view(old, i, j)
                    if filled >= 4 and not new:
                        self.layout[i][j] = "L"
                        changed += 1
                    elif filled >= 5 and new:
                        self.layout[i][j] = "L"
                        changed += 1

        # Return true if we're changing, false if we've gone stale/stable
        return changed > 0

    def count_filled(self):
        count = 0
        for i in range(0, len(self.layout)):
            for j in range(0, len(self.layout[i])):
                if self.layout[i][j] == "#":
                    count += 1
        return count

ca = ChairAutomata(inputs)

steps = 1

while ca.progress():
    steps += 1

print("Part 1: " + str(ca.count_filled()) + " (in " + str(steps) + " steps)\n")

ca = ChairAutomata(inputs)

steps = 1

while ca.progress(new=True):
    steps += 1

print("Part 2: " + str(ca.count_filled()) + " (in " + str(steps) + " steps)")
