# Does part 1 and 2!

inputs = []

with open("inputs/day10.input", "r") as i_file:
    inputs = i_file.readlines()

adapters = []
target = 0
for i in inputs:
    jolts = int(i)
    adapters += [jolts]
    if jolts + 3 > target:
        target = jolts + 3

adapters.sort()

steps = { 1: 0, 2: 0, 3: 0 }
last = 0
for i in adapters:
    steps[i-last] += 1
    last = i

# We always do one last jump to the device
steps[3] += 1

print("Step 1: " + str(steps[1] * steps[3]) + "\n")

# Make a list of routes to the device and cache them. It will always be 1 from the
# final one!
def calc_steps(routes, adapters, index):
    val = adapters[index]
    if val in routes:
        return routes[val]

    if index == len(adapters) - 1:
        # We know there is only one route to the end
        routes[val] = 1
        return routes[val]

    possible_routes = 0
    for i in range(index+1, index+4):
        if i >= len(adapters):
            break
        if val + 3 >= adapters[i]:
            possible_routes += calc_steps(routes, adapters, i)

    routes[val] = possible_routes
    return routes[val]

routes = {}

adapters = [0] + adapters

print("Step 2: " + str(calc_steps(routes, adapters, 0)))
