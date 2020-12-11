with open("input.txt", "r") as file:
    lines = file.read().splitlines()

# part 1
answers = []
group_answers = set()
for line in lines:
    if line == "":
        answers.append(group_answers)
        group_answers = set()
        continue
    for char in line:
        group_answers.add(char)
if len(group_answers) != 0:
    answers.append(group_answers)

answer_count = 0
for answer in answers:
    answer_count += len(answer)
print(answer_count)

# part 2
answers = []
group_answers = []
for line in lines:
    if line == "":
        answers.append(set(group_answers[0]).intersection(*group_answers))
        group_answers = []
    else:
        group_answers.append(line)
if len(group_answers) != 0:
    answers.append(set(group_answers[0]).intersection(*group_answers))

answer_count = 0
for answer in answers:
    answer_count += len(answer)
print(answer_count)
