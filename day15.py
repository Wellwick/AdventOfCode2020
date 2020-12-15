# Does part 1 and 2!

inputs = []

with open("inputs/day15.input", "r") as i_file:
    inputs = i_file.readlines()

vals = inputs[0].split(",")
#vals = [0,3,6]

#sequence = []
step = 0
last_said = {}
for i in vals:
    i = int(i)
    last_val = i
    #sequence += [i]
    new = last_val not in last_said
    last_said[i] = step
    step += 1

while step < 30000000:
    if step == 2020:
        print("Part 1: " + str(last_val) + "\n")
    if new:
        last_said[last_val] = step - 1
        last_val = 0
    else:
        new_val = step - 1 - last_said[last_val]
        last_said[last_val] = step - 1
        last_val = new_val
    
    #sequence += [last_val]
    new = last_val not in last_said
    step += 1

print("Part 2: " + str(last_val))
