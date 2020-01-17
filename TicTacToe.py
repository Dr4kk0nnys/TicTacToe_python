from random import randint

field = [None] * 9 # Initializing a 9 length array

def CreateField(): # Adds a empty space to every single item of the array
	for i in range(len(field)):
		field[i] = " "

def FakeField(): # It creates a fake field, for developing purposes
	players = ["X", "O"]
	for i in range(len(field)):
		field[i] = players[random.randint(0, 1)]

def ShowField(): # It shows the entire field formated, note that the field doesn't look at all like this, because it's an empty array
	index = 0
	print("-" * 16) # Aesthetic purposes
	for i in range(3):
		board = ""
		for j in range(3):
			board += field[index] + " | "
			index += 1
		print(board)
	print("-" * 16) # Aesthetic purposes

def CheckMove(position):
	if(field[position] == " "): return True
	else: 
		print("\nInvalid Play\n")
		return False

def CheckGame(player): # It checks for the entire game status, for both playes ( it uses a lot of math and logic )
	win = 0
	index = 0
	for i in range(3): # Horizontal [ 0, 1, 2 ], [ 3, 4, 5 ], [ 6, 7, 8 ]
		win = 0
		for j in range(3):
			if(field[index] == player):
				win += 1
			if(win >= 3):
				return False
			index += 1

	index = 0
	restart_index = 1
	for i in range(3): # Vertical [ 0, 3, 6 ], [ 1, 4, 7 ], [ 2, 5, 8 ]
		win = 0
		for j in range(3):
			if(field[index] == player):
				win += 1
			if(win >= 3):
				return False
			index += 3
		index = restart_index
		restart_index += 1

	if(field[0] == player and field[4] == player and field[8] == player): return False # Crossed Line
	if(field[2] == player and field[4] == player and field[6] == player): return False # Crossed Line

def CheckDraw():
	for i in range(len(field)):
		if(field[i] == " "): return
	return False

def ChoosePlayer(number):
	if(number % 2 == 0): return "X"
	else: return "O"

def Play():
	player_time = 0
	players = ["X", "O"]
	while(True):
		movement = int(input("[ 1 ~ 9 ]: ")) -1 # The -1 thing makes it possible to play with a [ 1 ~ 9 ] length, instead of playing [ 0 ~ 8 ]
		if(CheckMove(movement)):
			field[movement] = ChoosePlayer(player_time)
			ShowField()
			if(CheckGame(ChoosePlayer(player_time)) == False):
				print(ChoosePlayer(player_time) + " player Won!!!")
				break
		if(CheckDraw() == False):
			print("No one won!!!")
			break
		player_time += 1

CreateField()
Play()

