#!/usr/local/bin/python3

# -----
import chess_types 			as c_types
import board_functions 	as b_funct
import chess_functions 	as c_funct
import test_suite 			as t_suite

# -----
# # global board object
array = []
	
# -----
def play_game(log):

	b_funct.create_board(array)

	# # main loop (runs for 80 moves)
	for i in range(0,80):
		ps = []
		nps = []
		moves = []

		# # set the current turn and next turn
		if (i%2 == 0):	
			turn =	c_types.WHT
			nturn = c_types.BLK
		else:						 
			turn =	c_types.BLK
			nturn = c_types.WHT

		# # pull the current ps and next ps
		ps = b_funct.get_piece_list(array, turn)
		nps = b_funct.get_piece_list(array, nturn)

		# # print the board
		print("\nTurn "+ str(i) + ": " + str(turn) + " on play")
		b_funct.print_board(array)

		b_funct.log_board(log, array, i, turn)
			
		# # while we dont have a choice
		# # loop until we get one
		m = c_funct.choose_move(array, ps, i, c_types.NEGAMAX, c_types.NEGAMAX)
		if (m == -1):

			if (i%2 == 0):	print("chess - blk", end="")
			else: 			print("chess - wht", end="")
			print(" wins, no possible moves left.\n")		 

			return 0

		# # when we get the move, we make it, 
		b_funct.move_piece(array, m)

		# # and then update the game's pieces
		# # and the game's state
		ps =	b_funct.get_piece_list(array, turn)
		nps = b_funct.get_piece_list(array, nturn)

		# # if the game has stopped, return out, 
		# # game_status handles print outs and 
		# # promotion
		if (not c_funct.game_status(array, ps, nps, turn, nturn, True)):
			b_funct.log_board(log, array, i, turn)
			print("on turn: {}\n".format(i))
			return 0

	# # end the game after 80 turns
	print("")
	b_funct.print_board(array)
	print("\nchess - no winner: turn limit reached\n")
	return 0

# -----
# Execute
# -----
def run_game():

	with open("logs/chess_log.txt", "w+") as log:
		play_game(log)
		log.close()

# -----
# # run the game while saving the log
# # then store and print the return 
# # code
rc = run_game()

print("return code: {}".format(rc))

# -----

