# Does part 1 and 2!

inputs = []

with open("inputs/day12.input", "r") as i_file:
    inputs = i_file.readlines()

directions = {
    0: [0, 1], # North
    1: [1, 0], # East
    2: [0, -1], # South
    3: [-1, 0] # West
}

class Ship:
    def __init__(self, direction):
        self.direction = direction
        self.location = [0, 0]

    def process_step(self, step):
        command = step[0]
        amount = int(step[1:].strip())
        if command == "F":
            self.location[0] += directions[self.direction][0] * amount
            self.location[1] += directions[self.direction][1] * amount
        elif command == "L":
            self.direction = (self.direction - (amount/90)) % 4
        elif command == "R":
            self.direction = (self.direction + (amount/90)) % 4
        elif command == "N":
            self.location[1] += amount
        elif command == "E":
            self.location[0] += amount
        elif command == "S":
            self.location[1] -= amount
        elif command == "W":
            self.location[0] -= amount

    def manhattan_dist(self):
        return abs(self.location[0]) + abs(self.location[1])

s = Ship(1) # Heading starts as east

for i in inputs:
    s.process_step(i)

print("Part 1: " + str(s.manhattan_dist()) + "\n")

class Waypoint:
    def __init__(self, location):
        self.ship = [0, 0]
        # This is always relative to the ship
        self.location = location

    def rotate_right(self):
        old_loc = self.location.copy()
        self.location[1] = -old_loc[0]
        self.location[0] = old_loc[1]

    def rotate_left(self):
        old_loc = self.location.copy()
        self.location[1] = old_loc[0]
        self.location[0] = -old_loc[1]

    def process_step(self, step):
        command = step[0]
        amount = int(step[1:].strip())
        if command == "F":
            self.ship[0] += self.location[0] * amount
            self.ship[1] += self.location[1] * amount
        elif command == "L":
            while amount >= 360:
                amount -= 360
            count = amount/90
            for i in range(0, int(count)):
                self.rotate_left()
        elif command == "R":
            while amount >= 360:
                amount -= 360
            count = amount/90
            for i in range(0, int(count)):
                self.rotate_right()
        elif command == "N":
            self.location[1] += amount
        elif command == "E":
            self.location[0] += amount
        elif command == "S":
            self.location[1] -= amount
        elif command == "W":
            self.location[0] -= amount

    def manhattan_dist(self):
        return abs(self.ship[0]) + abs(self.ship[1])

w = Waypoint([10, 1]) # Heading starts as east

for i in inputs:
    w.process_step(i)

print("Part 2: " + str(w.manhattan_dist()))
