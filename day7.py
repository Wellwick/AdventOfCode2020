# Does part 1 and 2!

inputs = []

with open("inputs/day7.input", "r") as i_file:
    inputs = i_file.readlines()

def parse_instruction(recipes, line):
    line = line.replace(" bags", " bag")
    line = line.replace(" contain ", "")
    line = line.replace(".", "")
    line = line.replace(", ", "")
    recipe = line.split(" bag")
    recipes[recipe[0]] = {}
    if not "no other" in recipe[1]:
        for i in recipe[1:]:
            if i == "":
                continue
            space = i.find(" ")
            count = int(i[:space])
            recipes[recipe[0]][i[space+1:]] = count


recipes = {}
for i in inputs:
    if i.strip() == "":
        continue
    parse_instruction(recipes, i.strip())

def check_contains_gold(contains_gold, recipes, bag):
    if bag in contains_gold:
        return contains_gold[bag]
    
    count = 0
    # Let's track actual numbers!
    for i in recipes[bag]:
        if i == "shiny gold":
            count += recipes[bag][i]
        else:
            count += recipes[bag][i] * check_contains_gold(contains_gold, recipes, i)
    
    contains_gold[bag] = count
    return contains_gold[bag]


contains_gold = {}
count = 0
for i in recipes:
    if check_contains_gold(contains_gold, recipes, i) > 0:
        count += 1


print("Part 1: " + str(count) + "\n")

def count_internal_bags(contains_bags, recipes, bag):
    if bag in contains_bags:
        return contains_bags[bag]

    # Always count yourself
    count = 1
    for i in recipes[bag]:
        count += recipes[bag][i] * count_internal_bags(contains_bags, recipes, i)

    contains_bags[bag] = count
    return contains_bags[bag]


contains_bags = {}
gold_bags_count = count_internal_bags(contains_bags, recipes, "shiny gold")
print("Part 2: " + str(gold_bags_count))
