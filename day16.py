# Does part 1 and 2!

inputs = []

with open("inputs/day16.input", "r") as i_file:
    inputs = i_file.readlines()

i = 0 
fields = {}
while inputs[i].strip() != "":
    field, ranges = inputs[i].strip().split(":")
    ranges = ranges.strip().split(" or ")
    fields[field] = []
    for f in ranges:
        start, end = f.strip().split("-")
        start = int(start)
        end = int(end)
        fields[field] += [ [start, end] ]
    i += 1

def create_ticket(input_line):
    ticket = input_line.strip().split(",")
    for i in range(0, len(ticket)):
        ticket[i] = int(ticket[i])
    return ticket


i += 2
your_ticket = create_ticket(inputs[i])

other_tickets = []
i += 3
for i in range(i, len(inputs)):
    other_tickets += [create_ticket(inputs[i])]

valid_tickets = []

invalids = 0
for i in other_tickets:
    invalid_ticket = False
    for j in i:
        valid = False
        for f in fields:
            for r in fields[f]:
                if j >= r[0] and j <= r[1]:
                    valid = True
                if valid:
                    break
            if valid:
                break
        if not valid:
            invalids += j
            invalid_ticket = True
            continue
    if not invalid_ticket:
        valid_tickets += [i]

print("Part 1: " + str(invalids) + "\n")

def test_index(field, fields, valid_tickets, index):
    for i in valid_tickets:
        valid = False
        for r in fields[field]:
            if i[index] >= r[0] and i[index] <= r[1]:
                valid = True
        if not valid:
            return False

    return True


valid_indices = {}
for f in fields:
    valid_indices[f] = []
    for i in range(0, len(your_ticket)):
        if test_index(f, fields, valid_tickets, i):
            valid_indices[f] += [i]

#print(str(valid_indices))

indices_valid = []
for i in range(0, len(your_ticket)):
    indices_valid += [[]]
for f in valid_indices:
    string = ""
    for i in valid_indices[f]:
        string += str(i) + ", "
        indices_valid[i] += [f]
        #print(str(i) + ": " + str(indices_valid[i]))
    #print(f + ": " + string[:-2])
    #exit(0)

#print(indices_valid)
field_indices = []
for i in range(0, len(your_ticket)):
    field_indices += [0]

filled = 0
while filled < len(field_indices):
    for i in range(0, len(your_ticket)):
        if len(indices_valid[i]) == 1:
            # This means we've found a location
            field_name = indices_valid[i][0]
            #print(str(i) + ": " +  field_name)
            assert field_indices[i] == 0
            field_indices[i] = field_name
            for j in indices_valid:
                try:
                    j.remove(field_name)
                except:
                    pass
            filled += 1
            break

#print(field_indices)
index_it = {}
for i in range(0, len(field_indices)):
    index_it[field_indices[i]] = i

x = 1
for i in index_it:
    if "departure" in i:
        x *= your_ticket[index_it[i]]

print("Part 2: " + str(x))