"""
Robert Hamby
December 2, 2019
Advent of Code Day 2
https://adventofcode.com/2019/day/2
"""

# Adds numbers at index pos_1 and pos_2 in array and returns
def add_pos(pos_1, pos_2, arr):
	return arr[pos_1] + arr[pos_2]

# Multiplies numbers at index pos_1 and pos_2 in array and returns
def mult_pos(pos_1, pos_2, arr):
	return arr[pos_1] * arr[pos_2]

def compute(noun, verb, RESET):
	number_arr = []
	for n in RESET:
		number_arr.append(n)
	curr_index = 0

	number_arr[1] = noun
	number_arr[2] = verb

	while(True):
		if curr_index > len(number_arr):
			break
		else:
			pos_1 = number_arr[curr_index + 1]
			pos_2 = number_arr[curr_index + 2]
			answer_pos = number_arr[curr_index + 3]
			answer = None

			if number_arr[curr_index] == 99:
				break;
			elif number_arr[curr_index] == 1:
					answer = add_pos(pos_1, pos_2, number_arr)
			elif number_arr[curr_index] == 2:
					answer = mult_pos(pos_1, pos_2, number_arr)
			else:
				print("Something went wrong.")
				break;

			number_arr[answer_pos] = answer

			curr_index += 4;

	return number_arr[0]



# Open input file and read into an array
file = "input.txt"
arr = []

with open(file) as f:
	arr = f.read().split(',')


# Convert from string to intergers
num_arr = []

for n in arr:
	num_arr.append(int(n));

RESET = tuple(num_arr)

"""
USED ONLY FOR PART 1

# Restore input to the '1202 program alarm state'
num_arr[1] = 12
num_arr[2] = 2	
"""

# Cycles through each number between 0 and 99 for 
# the noun and verb, looking for compute() to return
# OUTPUT
OUTPUT = 19690720

noun = 0
verb = 0

while(True):
	if compute(noun, verb, RESET) == OUTPUT:
		print("Found them!\n", noun, verb)
		break
	else:
		if noun == 100:
			noun = 0
			verb += 1
		else:
			noun += 1

	print(noun, " ", verb)