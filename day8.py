# Does part 1 and 2!

inputs = []

with open("inputs/day8.input", "r") as i_file:
    inputs = i_file.readlines()

class Program:
    def __init__(self, instructions):
        self.instructions = []
        for i in instructions:
            self.instructions += [ i.strip() ]
        self.acc = 0
        self.index = 0
        self.complete = False

    def process(self):
        operation, argument = self.instructions[self.index].split(" ")
        argument = int(argument)
        if operation == "acc":
            self.acc += argument
            self.index += 1
        elif operation == "nop":
            self.index += 1
        elif operation == "jmp":
            self.index += argument
        if self.index == len(self.instructions):
            self.complete = True
            return

    # Each run part assumes the Program is fresh
    def run_part1(self):
        visited = []
        while self.index not in visited:
            visited += [self.index]
            self.process()
        print("Part 1: " + str(self.acc) + "\n")

    # Each run part assumes the Program is fresh
    def run_part2(self):
        visited = []
        while self.index not in visited:
            visited += [self.index]
            self.process()
            if self.complete:
                return self.acc
        return None


p = Program(inputs)
p.run_part1()

for i in range(0,len(inputs)):
    if "jmp" in inputs[i]:
        c_inputs = inputs.copy()
        c_inputs[i] = inputs[i].replace("jmp", "nop")
    elif "nop" in inputs[i]:
        c_inputs = inputs.copy()
        c_inputs[i] = inputs[i].replace("nop", "jmp")
    else:
        continue
    p = Program(c_inputs)
    val = p.run_part2()
    if val != None:
        break

print("Part 2: " + str(val))
