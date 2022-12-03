from enum import Enum

testing = False  # used for debugging messages and to pick the file
stage_1 = False  # used for more complex coding changes
file2read = 'Day02_sample.txt' if testing else 'Day02_01.txt'

# Translate their throws to values
rps_dict = {
    # Their Throws
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    # Our Throws
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}
wl_dict = {
    "A X": 3,  # Rock vs Rock     "draw" ,
    "B Y": 3,  # Paper vs Paper  "draw",
    "C Z": 3,  # Scissors vs Scissors Draw

    "B X": 0,  # Paper vs Rock    "win",
    "A Z": 0,  # Rock vs Scissors "loss" ,
    "C Y": 0,  # Scissors vs Paper loss

    "A Y": 6,  # Rock vs Paper    "win" ,
    "B Z": 6,  # Paper vs Scissors "loss" ,
    "C X": 6  # Scissors vs Rock  win
}
wl2_dict = {
    "A X": 0,  # Rock vs Scissors     "loss" ,
    "B X": 0,  # Paper vs Rock    "loss",
    "C X": 0,  # Scissors vs Paper  loss

    "C Y": 3,  # Scissors vs Scissors draw
    "B Y": 3,  # Paper vs Paper  draw
    "A Y": 3,  # Rock vs Rock    draw ,

    "C Z": 6,  # Scissors vs rock win
    "A Z": 6,  # Rock vs paper "win" ,
    "B Z": 6   # Paper vs scissors "win" ,

}
wl3_dict = {
    "A X": 3,  # Rock vs Scissors     "loss" ,
    "B X": 1,  # Paper vs Rock    "loss",
    "C X": 2,  # Scissors vs Paper  loss

    "C Y": 3,  # Scissors vs Scissors draw
    "B Y": 2,  # Paper vs Paper  draw
    "A Y": 1,  # Rock vs Rock    draw ,

    "C Z": 1,  # Scissors vs rock win
    "A Z": 2,  # Rock vs paper "win" ,
    "B Z": 3   # Paper vs scissors "win" ,

}
def read_file(a_file):
    score = 0
    score2 = 0
    running_total = 0
    running2_total = 0
    with open(a_file) as f:
        for line_in in f.readlines():
            throws = line_in.split()
            score = wl_dict[line_in.strip()] + rps_dict[throws[1]]
            score2 = wl2_dict[line_in.strip()] + wl3_dict[line_in.strip()]
            running_total += score
            running2_total += score2

            if stage_1:
                print(f"{line_in.strip()} --> {wl_dict[line_in.strip()]} =  {score}  --> {running_total}")
            else:
                print(f"{line_in.strip()} --> {wl2_dict[line_in.strip()]} =  {score2}  --> {running2_total}")

        print(f"Final score: {running_total}")
        print(f"Final score2: {running2_total}")

read_file(file2read)
