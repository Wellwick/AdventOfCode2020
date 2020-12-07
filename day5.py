# Does part 1 and 2!
import re

inputs = []

with open("inputs/day5.input", "r") as i_file:
    inputs = i_file.readlines()

seats = [False] * (2 ** 10)

def get_seat(b_pass):
    row = 0
    for i in range(0,7):
        if b_pass[6-i] == "B":
            row += 2 ** i

    column = 0
    for i in range(0,3):
        if b_pass[9-i] == "R":
            column += 2 ** i

    seat = (row * 8) + column
    seats[seat] = True
    return seat

highest = 0
for line in inputs:
    seat = get_seat(line)
    if seat > highest:
        highest = seat

print("Part 1: " + str(highest) + "\n")

for i in range(1, len(seats)-1):
    if not seats[i] and seats[i-1] and seats[i+1]:
        print("Part 2: " + str(i))
        break

