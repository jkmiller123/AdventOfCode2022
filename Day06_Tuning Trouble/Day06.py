# Tuning trouble sounds right for a Queue and a set
# a queue is a FIFO list
# a set is a unique unordered set.  It will prevent any duplicate values from being added


from collections import deque

testing = False  # used for debugging messages and to pick the file
stage_1 = False  # used for more complex coding changes
file2read = 'Day06_sample.txt' if testing else 'Day06_01.txt'

# set number of characters to look for
marker_len = 4 if stage_1 else 14  # 4 for stage 1  # 14 for stage 2


def read_file(a_file):
    the_queue = deque()

    with open(a_file) as f:
        # set everything up
        # first read in four characters then loop
        for x in range(0, marker_len):
            the_queue.append(f.read(1))
        position = marker_len

        # check the length of the set, if it's less than the marker length then there are duplicate
        # in the queue.  Pop one off and add a new one.

        while len(set(the_queue)) < marker_len:
            the_queue.popleft()
            position += 1
            the_queue.append(f.read(1))

        print(f"the marker ends at position {position}  --> {the_queue}")


# 1876 stage 1
# 2202 stage 2

read_file(file2read)
