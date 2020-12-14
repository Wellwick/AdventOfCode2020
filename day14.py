# Does part 1 and 2!

inputs = []

with open("inputs/day14.input", "r") as i_file:
    inputs = i_file.readlines()

# This is going to be pretty sparse
mem = {}

class BitMask:
    def __init__(self):
        self.bitmask = {}
        self.data = {}

    def set_mask(self, mask):
        pow_2 = 35
        for i in mask:
            if i != "X":
                self.bitmask[pow_2] = int(i)
            elif pow_2 in self.bitmask:
                del self.bitmask[pow_2]
            pow_2 -= 1

    def mask(self, value):
        acc = 0
        for i in range(0, 36):
            if i in self.bitmask:
                acc += (2 ** i) * self.bitmask[i]
            elif value % 2 == 1:
                acc += 2 ** i
            
            if value % 2 == 1:
                value -= 1
            # bit shift it along
            value = value >> 1
        return acc

    def store(self, address, value):
        # We need to apply the mask in a weird way now
        # Let's apply the 1's and 0's first!
        acc = 0
        for i in range(0, 36):
            if i in self.bitmask:
                if self.bitmask[i] == 1 or address % 2 == 1:
                    acc += 2 ** i
            
            if address % 2 == 1:
                address -= 1
            # bit shift it along
            address = address >> 1
        addresses = [acc]
        # Now go through the unknown ones!
        for i in range(0, 36):
            if i not in self.bitmask:
                # Time to double the address range
                for j in addresses.copy():
                    addresses += [ j + (2 ** i) ]

        for i in addresses:
            self.data[i] = value

    def sum(self):
        acc = 0
        for i in self.data:
            acc += self.data[i]

        return acc

b = BitMask()

data = {}

for i in inputs:
    i = i.strip()
    if i == "":
        continue
    if "mask" in i:
        b.set_mask(i.split(" ")[2])
    else:
        mem, eq, val = i.split(" ")
        mem = mem.replace("mem[", "").replace("]","")
        mem = int(mem)
        val = int(val)
        data[mem] = b.mask(val)

d_sum = 0
for i in data:
    d_sum += data[i]

print("Part 1: " + str(d_sum) + "\n")

for i in inputs:
    i = i.strip()
    if i == "":
        continue
    if "mask" in i:
        b.set_mask(i.split(" ")[2])
    else:
        mem, eq, val = i.split(" ")
        mem = mem.replace("mem[", "").replace("]","")
        mem = int(mem)
        val = int(val)
        b.store(mem, val)

print("Part 2: " + str(b.sum()))