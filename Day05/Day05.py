
testing = False  # used for debugging messages and to pick the file
stage_1 = False  # used for more complex coding changes
file2read = 'Day05_sample.txt' if testing else 'Day05_01.txt'

# create some lists that can be used to push and pop the values of the crates



def read_file(a_file):
    stacks = [[]]    # use an array of arrays to store the crates
    # note for simplicity in coding the input list was manually transposed
    # didn't want to worry about counting the spaces to determine which stack the
    # values belonged on

    holdvalues = []
    row_counter = 0
    final_sting = ""
    with open(a_file) as f:
        for line_in in f.readlines():
            # break up the sections by the first letter of each line.  [ = data m = move
            if line_in[0] == "[":
                new_line = line_in.strip().split(" ")
                for item in new_line:
                    # strip off all the crap and only put the characters on the stacks
                    stacks[row_counter].append(item.strip("[]"))
                row_counter += 1   # each row is a different stack
                stacks.append([])

            elif line_in[0] != "\n":  # if it's not a new line and not a [ then its instructions
                print(f"{stacks}")
                movement = line_in.split(" ")
                print(f"From : {int(movement[3])}  going to  {int(movement[5])} ")
                from_column = int(movement[3]) - 1
                to_column = int(movement[5]) - 1
                # for stage 2, I added an intermediate stack to push everything on then pop it off on the
                # destination stack
                if stage_1 == False:
                    for x in range(0, int(movement[1])):
                        holdvalue = stacks[from_column].pop()
                        holdvalues.append(holdvalue)
                for x in range(0, int(movement[1])):
                    if stage_1:
                        holdvalue = stacks[from_column].pop()
                    else:
                        holdvalue = holdvalues.pop()
                    print(f"Cell moving : {holdvalue}")
                    stacks[to_column].append(holdvalue)
                if testing:
                    for x in range(0, len(stacks)):
                        print(f"row{x} {stacks[x]}")
            else:
                junkstack =  stacks.pop()
    for x in  range(0, len(stacks)):
        final_sting += stacks[x].pop()
    print(f"Final string = {final_sting}")

# answer for stage 1 : JCMHLVGMG
# answer for stage 2 : LVMRWSSPZ
read_file(file2read)
