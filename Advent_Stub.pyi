

testing = False  # used for debugging messages and to pick the file
stage_1 = False  # used for more complex coding changes
file2read = 'Day02_sample.txt' if testing else 'Day02_01.txt'


def read_file(a_file):
    score = 0
    score2 = 0
    running_total = 0
    running2_total = 0
    with open(a_file) as f:
        for line_in in f.readlines():
            print(f"{line_in})


read_file(file2read)
