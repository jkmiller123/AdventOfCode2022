


testing = False  # used for debugging messages and to pick the file
stage_1 = True  # used for more complex coding changes
file2read = 'Day10_sample.txt' if testing else 'Day10_01.txt'

# Create a dictionary of spots to trigger the output/ total.
values = {
    20: 0,
    60: 0,
    100: 0,
    140: 0,
    180: 0,
    220: 0
}


def read_day10(a_file):
    cycle_queue = [0]  # Define it as a queue and pre-populate it with 1 value because the example starts at 1
    X = 1              # Initial State as described in the puzzle
    running_total = 0  # create a running total because we can and it's easier

    # Read everything in and create a queue with the values to process or read.
    # each element is a cycle . noop's add one element,  all others add a blank and the value
    with open(a_file) as f:
        for line_in in f.readlines():
            oper = line_in.strip().split()
            if oper[0] == "noop":
                cycle_queue.append(0)
            else:
                cycle_queue.append(0)
                cycle_queue.append(int(oper[1]))

    crt = []           # for each line on the display, Stage 2
    position = 0       # position on the screen  ( could use elements in crt but that leads to harder readability)
    for cycle_count in range(1, len(cycle_queue)):   # loop though all items except the first one because it's a dummy
        items = cycle_queue[cycle_count]
        if stage_1 and cycle_count in values:   # is it in the list/dictionary of items
            cycle_total = cycle_count * X       # Create the total value
            running_total += cycle_total        # add to running total
            # Print out the values to match the examples
            print("Cycle Counter: \033[1m%3d\033[0m " % cycle_count, end="")
            print(" Instruction= \033[96m\033[1m%3d\033[0m " % items, end="")
            print(" X= \033[92m\033[1m%3d\033[0m " % X, end="")
            print(" Cycle Total= \033[92m\033[1m%5d\033[0m " % cycle_total, end="")
            print("")

        # Stage 2 . Drawing on the screen.
        if not stage_1:
            # is this value in the register +/- 1 of the position
            if position - 1 <= X <= position + 1:
                crt.append("#")
            else:
                crt.append(".")
            position += 1   # added something so move the position along.
            # ( kills me that should just count items in array )

            # have it reached the end of the screen.  Print it out
            if position % 40 == 0:
                for x in range(0, 40):
                    print(f"{crt[x]}" , end="")
                print("")
                crt.clear()     # Reset the register .. array
                position = 0    # rest the position counter :-(
        X += items     # finally add the item to the register since its the end of the cycle
    print(f"Final Total {running_total}")

read_day10(file2read)