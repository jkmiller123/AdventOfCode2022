# pair counting exercise

testing = False  # used for debugging messages and to pick the file
stage_1 = True  # used for more complex coding changes
file2read = 'Day04_sample.txt' if testing else 'Day04_01.txt'


def read_file(a_file):
    pair_counter = 0    # stage 1 counter
    pair2_counter = 0   # stage 2 counter

    with open(a_file) as f:
        for line_in in f.readlines():
            # use these counters to see if one of the pairs match
            pair1 = 0
            pair2 = 0
            pair1_2 = 0
            pair2_2 = 0
            pairs = line_in.strip().split(",")
            cords0 = list(map(int, pairs[0].split("-")))   # split the values and convert them to ints
            cords1 = list(map(int, pairs[1].split("-")))

            # is the first value within the range of the second
            if cords1[0] <= cords0[0] <= cords1[1]:
                pair1_2 += 1
                if cords1[0] <= cords0[1] <= cords1[1]:
                    pair1 = 1

            # is my second set within the first sets
            if cords0[0] <= cords1[0] <= cords0[1]:
                pair2_2 += 1
                if cords0[0] <= cords1[1] <= cords0[1]:
                    pair2 = 1
            # there can be overlap so only count it once 6-19 6-19 is only one overlap
            if pair1 + pair2 > 0:
                pair_counter += 1
            # count the Or's
            if pair1_2 + pair2_2 > 0:
                pair2_counter += 1

            print(f"pairs {line_in.strip()} {pair1} {pair2}  ")

    print(f"total Pairs = {pair_counter}")
    print(f"total Pairs2 = {pair2_counter}")


# 513 right for part 1
# 878 right for part 2

read_file(file2read)
