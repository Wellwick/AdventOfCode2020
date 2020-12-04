# Does part 1 and 2!
import re

inputs = []

with open("inputs/day4.input", "r") as i_file:
    inputs = i_file.readlines()

regexes = {}
regexes["byr"] = re.compile("^\d\d\d\d$")
regexes["iyr"] = re.compile("^\d\d\d\d$")
regexes["eyr"] = re.compile("^\d\d\d\d$")
regexes["hgt"] = re.compile("^\d+(in|cm)$")
regexes["hcl"] = re.compile("^\#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$")
regexes["ecl"] = re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$")
regexes["pid"] = re.compile("^\d\d\d\d\d\d\d\d\d$")


def valid(passport, weak_check):
    for i in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if i not in passport:
            return False

    if weak_check:
        return True
    
    for i in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if not regexes[i].match(passport[i]):
            return False

    byr = int(passport["byr"])
    iyr = int(passport["iyr"])
    eyr = int(passport["eyr"])
    if byr > 2002 or byr < 1920:
        return False
    elif iyr > 2020 or iyr < 2002:
        return False
    elif eyr > 2030 or eyr < 2020:
        return False

    hgt = passport["hgt"]
    if "cm" in hgt:
        hgt = int(hgt[:-2])
        if hgt > 193 or hgt < 150:
            return False
    else:
        hgt = int(hgt[:-2])
        if hgt > 76 or hgt < 59:
            return False
    
    return True

valids = 0
passports = []
passport = {}
# Add one empty to make sure the last one is processed!
inputs += [""]
for i in inputs:
    if i.strip() == "":
        if valid(passport, True):
            valids += 1
        passports += [passport]
        passport = {}
    else:
        key_vals = i.strip().split(" ")
        for j in key_vals:
            key, val = j.split(":")
            passport[key] = val

print("Part 1: " + str(valids) + "\n")

valids = 0
for i in passports:
    if valid(i, False):
        valids += 1


print("Part 2: " + str(valids))