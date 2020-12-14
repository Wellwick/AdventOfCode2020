# Does part 1 and 2!

inputs = []

with open("inputs/day13.input", "r") as i_file:
    inputs = i_file.readlines()

start = int(inputs[0].strip())
busses = inputs[1].strip().split(",")
# Functioning busses
f_busses = []
# Scheduled busses
s_busses = {}
index = 0

for i in busses:
    try:
        f_busses += [int(i)]
        s_busses[int(i)] = index % int(i)
    except:
        pass
    index += 1

dist = max(f_busses)
for i in f_busses:
    if start % i == 0:
        dist = 0
        output = 0
        break
    # Find the next one beyond this bus
    multiples = int(start / i) + 1
    if (multiples * i) - start < dist:
        dist = (multiples * i) - start
        output = dist * i

print("Part 1: " + str(output) + "\n")
#print(s_busses)

modulo = 1
value = 0

for i in s_busses:
    # Need to invert these values so we can get back to the timestamp
    s_busses[i] = (i - s_busses[i]) % i
    modulo *= i
    # Multiply all the values that aren't i
    l_value = 1
    for j in s_busses:
        if i == j:
            continue
        l_value *= j
    multiple = 1
    while ((l_value * multiple) % i) != s_busses[i]:
        multiple += 1
    value += l_value * multiple

print("Part 2: " + str(value % modulo))

