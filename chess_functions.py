
# -----
import chess_types  		as c_types
import ai_functions 		as a_funct
import board_functions 	as b_funct
from move_functions 		import get_moves

# -----
def print_moves(moves, ver):

	if (ver == False):
		return

	# # print the header
	print("\n" + str(len(moves)) + " Moves:") 

	# # print the end of game code
	print("Enter -1 to quit")
	print("-----")

	for m,i in zip(moves, range(0,len(moves))):

		# # pad the index if not a double digit number
		if (i < 10): print("0", end='') 
		print(str(moves.index(m)) + '. ', end='') 

		# # print the first coordinate, then the second
		print("{}:{}".format(c_types.columns[m[1]],m[0]), end='') 
		print(" -> ", end='')
		print("{}:{}".format(c_types.columns[m[3]],m[2])) 

# -----
def choose_move(arr, piece_list, turn, player1, player2):

	choice	= -1
	moves		= []

	for p in piece_list:
		pc = arr[p[1]][p[2]]
		assert (pc[0] == p[0])
		moves += get_moves(arr, p[1], p[2])

	if (len(moves) == 0):
		return -1

	print_moves(moves, False)
	# choice = player(arr, turn, c_types.HUMAN, c_types.NEGAMAX, moves)
	choice = a_funct.player(arr, turn, player1, player2, moves)

	if (choice == -1): 
		return -1
	else:
		move = moves[choice]
		print("\nChose " + str(choice) + '. ', end='') 
		# # print the first coordinate, then the second
		print("{}:{}".format(c_types.columns[move[1]],move[0]), end='') 
		print(" -> ", end='')
		print("{}:{}".format(c_types.columns[move[3]],move[2])) 
		print("-----")

	return moves[choice]
				
# -----
def game_status(arr, pieces, npieces, turn, nturn, verbose):

	# # verify that the board, and two piece lists
	# # are correct and that nturn != turn
	args = []
	args += [[c_types.BOARD, arr], ]
	args += [[c_types.COORD_LIST, pieces], ]
	args += [[c_types.COORD_LIST, npieces], ]
	c_types.assert_argument_list(args)
	# # assert that both turns are not the same
	assert(nturn != turn)
		
	# # King Check
	# # Game halts when a king is taken,
	# # players should have their king 
	# # during their turn (double check).
	# # check for their king
	nking = False
	for np in npieces:
		if (np[0] == 'k'): 
			nking = True		

	if (nking == False):
		print("")	 
		if (verbose): b_funct.print_board(arr)
		print("\nchess - " + str(turn) + " killed the king!\n") 
		return False

	# # check for your king 
	king = False
	for p in pieces:
		if (p[0] == 'k'): 
			king = True 

	if (king == False):
		
		if (verbose): 
			print("\n")	
			b_funct.print_board(arr)
			print("\nchess - " + str(nturn) + " killed the king!\n") 

		assert(False == True)

	# # Pawn Promotion
	# # if you have a piece that is at the 
	# # end of the board, then we need to 
	# # replace it with a queen of that col
	if (turn == c_types.WHT): promotion = 0
	else:											promotion = 5

	for p in pieces:
		if(p[0] == 'p' and p[1] == promotion):
			arr[p[1]][p[2]][0] = 'q'

	return True

# -----

