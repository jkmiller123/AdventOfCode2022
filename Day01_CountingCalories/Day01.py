# Day 1 OF Advent of code.
# Part 1.  Find the most number of Calories by any one elf
# Part 2.  Find the total for the top 3 elves.

# Concept:  read in file and only store the top elf, ignore the rest
# Update:   store in the top 3, shifting everyone down if necessary


testing = False   # used for debugging messages and to pick the file
stage_1 = True    # used for more complex coding changes
file2read = 'Day01_sample.txt' if testing else 'Day01_01.txt'


def read_file(a_file):
    elf_counter = 1    # if we need to determine which elf had the most
    max_calories = 0   # Sum Total per elf
    max_calories2 = 0
    max_calories3 = 0

    which_elf = 0    # the elf with the current top score
    current_calories = 0   # running total for the current elf

    with open(a_file) as f:
        for line_in in f.readlines():
            if line_in in ['\n', '\r\n']:   # if it's a blank line then it's a new elf
                # swap the leader board of total calories
                if current_calories > max_calories:
                    max_calories3 = max_calories2
                    max_calories2 = max_calories
                    max_calories = current_calories
                    which_elf = elf_counter
                elif current_calories > max_calories2:
                    max_calories3 = max_calories2
                    max_calories2 = current_calories
                elif current_calories > max_calories3:
                    max_calories3 = current_calories

                # debug messages during development
                if testing:
                    print(f"found a elf # {elf_counter} with {current_calories} and current max = {max_calories}")
                elf_counter += 1  # since it's a new line , increase elf counter , not really needed
                current_calories = 0  # reset the calorie counter

            else:  # not a new line so add this new value in with the existing total
                current_calories += int(line_in)

        # done reading the file, need to redo the max checking
        # swap the leader board of total calories
        if current_calories > max_calories:
            max_calories3 = max_calories2
            max_calories2 = max_calories
            max_calories = current_calories
        elif current_calories > max_calories2:
            max_calories3 = max_calories2
            max_calories2 = current_calories
        elif current_calories > max_calories3:
            max_calories3 = current_calories

        if testing:
            print(f"found last elf # {elf_counter} with {current_calories} and current max = {max_calories}")

    print(f"The elf with the most calories is #{which_elf} with {max_calories}")
    total_calories = max_calories + max_calories2 + max_calories3
    print(f"Total Calories by top 3 elves = {total_calories}")


read_file(file2read)
