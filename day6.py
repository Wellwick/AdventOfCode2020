# Does part 1 and 2!

inputs = []

with open("inputs/day6.input", "r") as i_file:
    inputs = i_file.readlines()

groups = []
group = { "size": 0 }
for i in inputs:
    if i.strip() == "":
        groups += [group]
        group = { "size": 0 }
    else:
        group["size"] += 1
        for j in i.strip():
            if j not in group:
                group[j] = 0
            group[j] += 1

if len(group) > 1:
    groups += [group]

sum_group_counts = 0
for g in groups:
    sum_group_counts += len(g) - 1

print("Part 1: " + str(sum_group_counts) + "\n")

sum_group_everyones = 0
for g in groups:
    for i in g:
        if i == "size": continue
        if g["size"] == g[i]:
            sum_group_everyones += 1

print("Part 2: " + str(sum_group_everyones))