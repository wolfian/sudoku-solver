from tabulate import tabulate
import os, time, copy

def fill_values(): # adding pre defined values in sudoku
	temp_su = []
	for i in range(9):
		print(f"Enter elements of row {i+1} separated by space (type 0 is case of empty places)")
		while True:
			try:
				current_row = list(map(int, input("> ").split()))
				if len(current_row) == 9:
					temp_su.append(current_row)
					break
				else:
					raise Exception
			except:
				print("Invalid row input encountered!")

	return temp_su


def display_sudoku(su): # display sudoku as a 9x9 grid
	
	# replacing 0s with '-' wo make it visually appealing
	temp = copy.deepcopy(su)

	for i in range(9):
		for j in range(9):
			if temp[i][j] == 0:
				temp[i][j] = '-'

	print(title)
	print(f'\n{tabulate(temp, tablefmt="grid")}')


def check_validity(pos, val, su):
	# check row
	for i in range(len(su[0])):
		if su[pos[0]][i] == val and pos[1] != i:
			return False
	#check column
	for i in range(len(su)):
		if su[i][pos[1]] == val and pos[0] != i:
			return False

	#check 3x3 boxes
	for i in range((pos[0]//3)*3, (pos[0]//3)*3 + 3):
		for j in range((pos[1]//3) * 3, (pos[1]//3)*3 + 3):
			if su[i][j] == val and (i,j) != pos:
				return False

	return True


def check_empty(su):
	for i in range(9):
		for j in range(9):
			if su[i][j] == 0:
				return (i, j)
	return None


def solve(su):
	os.system('clear')
	display_sudoku(su)
	# time.sleep(0.25) # makes the algorith in action visible, but slows down execution

	pos = check_empty(su) # returns empty location available in the form of a tuple
	if not pos:
		return True
	else:
		r, c = pos
		
	for value in range(1, 10):
		if check_validity((r, c), value, su):
			su[r][c] = value

			if solve(su):
				return True

			su[r][c] = 0

	return False


# program starts here
title = ''' ___  _ _    ___  ___  ___  ___  _ __ ___  ___ 
/ __>| | |  |  _>| . \| . ||  _>| / /| __>| . \ 
\__ \| ' |  | <__|   /|   || <__|  \ | _> |   /
<___/`___'  `___/|_\_\|_|_|`___/|_\_\|___>|_\_\ '''

sudoku = [
    		[0, 0, 0, 0, 0, 0, 0, 0, 0],
   			[0, 0, 0, 0, 0, 0, 0, 0, 0],
   			[0, 0, 0, 0, 0, 0, 0, 0, 0],
   			[0, 0, 0, 0, 0, 0, 0, 0, 0],
   			[0, 0, 0, 0, 0, 0, 0, 0, 0],
   			[0, 0, 0, 0, 0, 0, 0, 0, 0],
   			[0, 0, 0, 0, 0, 0, 0, 0, 0],
   			[0, 0, 0, 0, 0, 0, 0, 0, 0],
   			[0, 0, 0, 0, 0, 0, 0, 0, 0]
		]

os.system('clear')
display_sudoku(sudoku)
print("\nLet's add pre defined values first!")
input("Press enter/return key to continue ...")

while True: # loop to add predefined values
	os.system('clear')
	display_sudoku(sudoku)

	try:
		opt = int(input("\n1. Fill pre-defined values    2. Solve sudoku\n"))
		if opt == 1:
			sudoku = fill_values()
		if opt == 2:
			break
	except Exception as err:
		print("\nInvalid input encountered!")
		print("Details:", err)
		time.sleep(1)
		continue

start_time = time.time() # calculating time taken to solve the sudoku
solve(sudoku)
end_time = time.time() - start_time

os.system('clear')
display_sudoku(sudoku)
print(f"\nFinished! (took {abs(end_time):.2f} seconds)")
