

testing = False
stage_1 = True
file2read = 'Day01_sample.txt' if testing else 'Day01_01.txt'


def read_file(a_file):
    elf_counter = 1
    max_calories = 0
    max_calories2 = 0
    max_calories3 = 0
    which_elf = 0
    current_calories = 0
    with open(a_file) as f:
        for line_in in f.readlines():
            if line_in in ['\n', '\r\n']:
                if current_calories > max_calories:
                        max_calories3 = max_calories2
                        max_calories2 = max_calories
                        max_calories = current_calories
                elif  current_calories > max_calories2:
                    max_calories3 = max_calories2
                    max_calories2 = current_calories
                elif current_calories > max_calories3:
                    max_calories3 = current_calories
                if testing:
                    print(f"found a elf # {elf_counter} with {current_calories} and current max = {max_calories}")
                elf_counter += 1
                current_calories = 0

            else:
                current_calories += int(line_in)
        if current_calories > max_calories:
            max_calories = current_calories
        print(f"found last elf # {elf_counter} with {current_calories} and current max = {max_calories}")
        elf_counter += 1
        current_calories = 0
    print(f"The elf with the most calories is #{which_elf} with {max_calories}")
    total_calories = max_calories + max_calories2    + max_calories3
    print(f"Total Calories by top 3 elves = {total_calories}")

read_file(file2read)
