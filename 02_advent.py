"""
Robert Hamby
December 2, 2019
Advent of Code Day 2
https://adventofcode.com/2019/day/2
"""

def add_pos(pos_1, pos_2, arr):
	return arr[pos_1] + arr[pos_2]

def mult_pos(pos_1, pos_2, arr):
	return arr[pos_1] * arr[pos_2]


# Open input file and read into an array
file = "input.txt"
arr = []

with open(file) as f:
	arr = f.read().split(',')


# Convert from string to intergers
num_arr = []

for n in arr:
	num_arr.append(int(n));

# Restore input to the '1202 program alarm state'
num_arr[1] = 12
num_arr[2] = 2	

# Holds the current index
curr_index = 0

while(True):
	if curr_index > len(num_arr):
		break
	else:
		pos_1 = num_arr[curr_index + 1]
		pos_2 = num_arr[curr_index + 2]
		answer_pos = num_arr[curr_index + 3]
		answer = None

		if num_arr[curr_index] == 99:
			break;
		elif num_arr[curr_index] == 1:
				answer = add_pos(pos_1, pos_2, num_arr)
		elif num_arr[curr_index] == 2:
				answer = mult_pos(pos_1, pos_2, num_arr)
		else:
			print("Something went wrong.")
			break;

		num_arr[answer_pos] = answer

		curr_index += 4;


print(num_arr)

