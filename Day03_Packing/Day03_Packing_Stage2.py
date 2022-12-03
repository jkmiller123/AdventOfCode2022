
# decided to create a second file because I can.  to keep a base line
# for the first stage

testing = False  # used for debugging messages and to pick the file
stage_1 = False  # used for more complex coding changes
file2read = 'Day03_sample.txt' if testing else 'Day03_01.txt'


def read_file(a_file):
    priority_total = 0
    group_counter = 0   # create groups of three
    groups = []
    with open(a_file) as f:
        for line_in in f.readlines():
            group_counter += 1
            if group_counter <= 3:    # create groups of three.  No error checking on number of lines
                groups.append("".join(set(line_in.strip())))  # get only the unique characters

            # Third group now see what is common in all of them.
            if group_counter == 3:
                for achar in groups[0]:
                    if groups[1].count(achar) > 0 and groups[2].count(achar) > 0:
                        # each character has an ASCII value use that as the starting point instead of
                        # creating a list.  A = 65 a = 97
                        # a-z = 1-26  A-Z = 27-52
                        priority = ord(achar) - ((64 - 26) if achar.isupper() else 96)
                        priority_total += priority
                        print('Found packing character: {:2s}  Ord: {:3d} Priority: {:2d}'.format(achar, ord(achar),
                                                                                                  priority))
                groups.clear()      # reset the list of groups
                group_counter = 0  # Reset group counter

    print(f"Total Priority = {priority_total}")

print(f"{ord('a')}")
read_file(file2read)
