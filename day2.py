# Does part 1 and 2!

inputs = []

with open("inputs/day2.input", "r") as i_file:
    inputs = i_file.readlines()

valids = 0

for i in inputs:
    min_count, max_count = i.split("-")
    max_count, key, password = max_count.split(" ")
    min_count = int(min_count)
    max_count = int(max_count)
    key = key[:-1]
    count = 0
    for letter in password:
        if letter == key:
            count += 1
    if count >= min_count and count <= max_count:
        valids += 1

print("Part 1: " + str(valids) + "\n")

valids = 0

for i in inputs:
    first_index, second_index = i.split("-")
    second_index, key, password = second_index.split(" ")
    first_index = int(first_index)
    second_index = int(second_index)
    key = key[:-1]
    count = 0
    if ((password[first_index-1] == key and password[second_index-1] != key)
    or (password[first_index-1] != key and password[second_index-1] == key)):
        valids += 1

print("Part 2: " + str(valids))
