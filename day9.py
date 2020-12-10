# Does part 1 and 2!

inputs = []

with open("inputs/day9.input", "r") as i_file:
    inputs = i_file.readlines()

numbers = []
for i in inputs:
    numbers += [int(i)]

def check_index(numbers, index):
    # Always true for first 25 numbers
    if index < 25:
        return True
    subset = numbers[index-25:index]
    for i in range(0,24):
        for j in range(i,25):
            if subset[i] == subset[j]:
                continue
            if subset[i] + subset[j] == numbers[index]:
                return True
    return False

def encryption_weakness(numbers, index):
    value = numbers[index]
    for i in range(0, index-2):
        summing = 0
        smallest = 9999999999999999999999
        largest = 0
        for j in range(i, index):
            if numbers[j] < smallest:
                smallest = numbers[j]
            if numbers[j] > largest:
                largest = numbers[j]
            summing += numbers[j]
            if summing == value:
                return smallest + largest
            elif summing > value:
                break


for i in range(25, len(numbers)):
    if not check_index(numbers, i):
        print("Part 1: " + str(numbers[i]) + "\n")
        print("Part 2: " + str(encryption_weakness(numbers, i)))
        break

