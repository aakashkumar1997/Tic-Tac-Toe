import os


matrix = [[0 for x in range(3)] for y in range (3)]
times = True;



def draw():											##########	DRAWS THE CURRENT TIC TAC TOE ARENA		#########
	print('\n\n\n\n')
	for i in range(3):
		for j in range(3):
			print(matrix[i][j] , end = '     ')
		print('\n\n')


def signtoggle(sign):								#########	TOGGLES THE NEXT SETP SIGN ACCORDINGLY	#########
	if(sign == 'X' or sign == 'x'):
		sign = 'O'
	else:
		sign = 'X'
	return sign		

def input_feild(target , sign):						#########	UPDATES THE TARGET POSITION ACCORDING TO PLAYER'S INPUT   ######## 
	for i in range(3):
		for j in range(3):
			if(str(matrix[i][j]) == str(target)):
				matrix[i][j] = sign
				sign = signtoggle(sign)
				return sign			


def check_if_not_won():								#########	CHECK IF GAME IS ALREADY WON OR NOT   ########
	
	notwon = True

	if(notwon):
		for i in range(3):
			token = matrix[i][0]					#########	CHECK HORIZONTAL LINES	########
			flag = True
			for j in range(3):
				if(matrix[i][j] != token and flag):
					flag = False
			if(flag):
				notwon = False
				print('Congratulations ' + str(token) + ' won the game!!!!')
				break

	if(notwon):
		for i in range(3):
			token = matrix[0][i]					#########	CHECK VERTICAL LINES	########
			flag = True
			for j in range(3):
				if(matrix[j][i] != token and flag):
					flag = False
			if(flag):
				notwon = False
				print('Congratulations ' + str(token) + ' won the game!!!!')
				break


	if(notwon):
			token = matrix[0][0]					#########	CHECK LEFT DIAGONAL	########
			flag = True
			for j in range(3):
				if(matrix[j][j] != token and flag):
					flag = False
			if(flag):
				notwon = False
				print('Congratulations ' + str(token) + ' won the game!!!!')
				

	if(notwon):
			token = matrix[0][2]					#########	CHECK RIGHT DIAGONAL	########
			flag = True
			for j in range(3):
				if(matrix[j][2 - j] != token and flag):
					flag = False
			if(flag):
				notwon = False
				print('Congratulations ' + str(token) + ' won the game!!!!')
				
	return notwon


def gameover():
	for i in range (3):
		for j in range (3):
			if(not(matrix[i][j] == 'O' or matrix[i][j] == 'X')):
				return False
	return True



########################################################	GAMES ARENA		#########################################################



for i in range(3):									#########	INITIAL TIC TAC TOE ARENA WITH FEILD NUMBER		#########
	for j in range(3):
		matrix[i][j] = 1 + j + (3 * i);

notwon = check_if_not_won();

while(notwon and (not(gameover()))):										#########	LOOPS TILL PLAYER IS NOT WON 	#########
	unused_variable = os.system('clear')
	draw();	
	if(times):
		times = False
		print('Enter the sign(X or O) with which you want to start : ' , end = '')
		sign = input()

	print('Enter the feild(1 ~ 9) in which player(' + sign + ') want to insert : ' , end = '')
	target = int(input())
	
	while(((matrix[int((target - 1) / 3)][int((target - 1) % 3)] == 'X') or (matrix[int((target - 1) / 3)][int((target - 1) % 3) ] == 'x') or (matrix[int((target - 1) / 3)][int((target - 1) % 3)] == 'O') or (matrix[int((target - 1) / 3)][int((target - 1) % 3)] == 'o') )):
		unused_variable = os.system('clear')
		draw()
		print('Feild already filled !!')
		print('Choose another feild(1 ~ 9) number : ' , end = '')
		target = int(input())

	sign  = input_feild(target , sign)
	unused_variable = os.system('clear')
	draw();
	notwon = check_if_not_won()

if(gameover()):
	unused_variable = os.system('clear')
	draw();
	print('Game Over!!!!')
	print('Nobody Won, Better Luck Next Time....')