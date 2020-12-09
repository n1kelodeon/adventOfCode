import re

with open("input.txt") as file:
    lines = file.read().splitlines()

lines.append("")
passports_list = []
passport = ""
for line in lines:
    passport += line
    if line == "":
        passports_list.append(passport)
        passport = ""
    else:
        passport += " "


passport_dicts = []
for passport in passports_list:
    passport_dict = {}
    items = passport.split()
    for item in items:
        key, value = item.split(":")
        passport_dict[key] = value
    passport_dicts.append(passport_dict)

required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid_count = 0
for passport in passport_dicts:
    passport.pop("cid", None)
    if len(passport) == len(required_keys):
        valid_count += 1

print(valid_count)

# part two
valid_count = 0
for passport in passport_dicts:
    if len(passport) != len(required_keys):
        continue
    # byr
    if not 1920 <= int(passport["byr"]) <= 2002:
        continue
    # iyr
    if not 2010 <= int(passport["iyr"]) <= 2020:
        continue
    # eyr
    if not 2020 <= int(passport["eyr"]) <= 2030:
        continue
    # hgt
    re_match = re.search("^([1-9][0-9]+)(cm|in)$", passport["hgt"])
    if re_match is None:
        continue
    if re_match.group(2) == "cm":
        low, high = 150, 193
    else:
        low, high = 59, 76
    if not low <= int(re_match.group(1)) <= high:
        continue
    # hcl
    re_match = re.search("^#[0-9-a-f]{6}$", passport["hcl"])
    if re_match is None:
        continue
    # ecl
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue
    # pid
    re_match = re.search("^[0-9]{9}$", passport["pid"])
    if re_match is None:
        continue
    valid_count += 1

print(valid_count)
