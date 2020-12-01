# Does part 1 and 2!

inputs = []

with open("inputs/day1p1.input", "r") as i_file:
    inputs = i_file.readlines()

sanitized_inputs = []
for i in inputs:
    sanitized_inputs += [int(i)]

complete = False

for i in sanitized_inputs:
    for j in sanitized_inputs:
        if i + j == 2020:
            print("Part 1: " + str(i*j) + "\n")
            complete = True
            break
    if complete:
        break

complete = False

for i in sanitized_inputs:
    for j in sanitized_inputs:
        for k in sanitized_inputs:
            if i + j + k == 2020:
                print("Part 2: " + str(i*j*k) + "\n")
                complete = True
                break
        if complete:
            break
    if complete:
        break


