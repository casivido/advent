from helpers import loadFileByLine;

elf_food_raw = loadFileByLine('inputs/day1_1.txt')

elf_food_list = []
max_elf_food_list = [0]
current_elf_food = 0

for food_raw in elf_food_raw:
    if food_raw != "":
        current_elf_food += int(food_raw)
    else:
        if current_elf_food > max_elf_food_list[0]:
            max_elf_food_list.insert(0, current_elf_food)
        elif current_elf_food > max_elf_food_list[1]:
            max_elf_food_list.insert(1, current_elf_food)
        elif current_elf_food > max_elf_food_list[2]:
            max_elf_food_list.insert(2, current_elf_food)
        elf_food_list.append(current_elf_food)
        current_elf_food = 0

if current_elf_food > max_elf_food_list[0]:
    max_elf_food_list.insert(current_elf_food, 0)
elif current_elf_food > max_elf_food_list[1]:
    max_elf_food_list.insert(current_elf_food, 1)
elif current_elf_food > max_elf_food_list[2]:
    max_elf_food_list.insert(current_elf_food, 1)
elf_food_list.append(current_elf_food)
current_elf_food = 0

print(elf_food_list)
print(max_elf_food_list[0:3])
print(sum(max_elf_food_list[0:3]))

