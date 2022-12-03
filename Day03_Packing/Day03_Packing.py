

testing = True  # used for debugging messages and to pick the file
stage_1 = True  # used for more complex coding changes
file2read = 'Day03_sample.txt' if testing else 'Day03_01.txt'


def read_file(a_file):
    priority_total = 0
    with open(a_file) as f:
        for line_in in f.readlines():
            # divide the line into two rucksacks.  Only want unique items so remove dups at the same time
            pack1 = "".join(set(line_in[:len(line_in)//2]))
            pack2 = "".join(set(line_in[len(line_in)//2:]))
            for achar in pack1:   # loop through each item in the first pack
                if (pack2.count(achar) == 1 ):  # can you find it in the second one.
                    # each character has an ASCII value use that as the starting point instead of
                    # creating a list.  A = 65 a = 97
                    # a-z = 1-26  A-Z = 27-52
                    priority = ord(achar) - ((64 - 26) if achar.isupper() else 96)
                    priority_total += priority
                    print('Found packing character: {:2s}  Ord: {:3d} Priority: {:2d}'.format(achar, ord(achar), priority))
    print(f"Total Priority = {priority_total}")

print(f"{ord('a')}")
read_file(file2read)
