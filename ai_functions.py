
# -----
import chess_types 			as c_types
import board_functions 	as b_funct
import chess_functions 	as c_funct
import move_functions 	as m_funct
from random 						import randrange
from copy 							import deepcopy

# -----
# # go through all of the moves, making them,
# # and trying to find the value of them, if
# # that value is the worst for out opponent, 
# # we will choose that one
def negamax(arr, turn, cols, pieces, moves, depth):

	# # figure out the next color for next turn
	[col, ncol] = cols
	[ps, nps] = pieces
	[mvs, nmvs] = moves

	# # return values of this function
	best_score = -100000
	best_move = []

	# # if we have no moves, we will need to 
	# # return that we lose this turn
	if (len(mvs) == 0):
		return [best_score, best_move]
	if (turn == 80):
		return [0, best_move]

	# # if we have reached the end of the 
	# # depth, we can return out with the
	# # boards current state
	if (depth <= 0):
		temp = b_funct.board_value(arr, col[0], col[1]) + len(mvs)-len(nmvs) * 10
		return [temp, []]

	# # check if we have no king if not,
	# # return that we have lost 
	king = False
	for p in ps:
		if (p[0] == 'k'): king = True
	if (king == False): return [best_score, best_move]	

	for m in mvs:

		# # copy the board and make the current
		# # selected move
		board = deepcopy(arr)
		b_funct.move_piece(board, m)
		
		# # switch the colors, and find all the 
		# # pieces for the next turn
		next_ps  = b_funct.get_piece_list(board, ncol)
		next_nps = b_funct.get_piece_list(board, col)
		next_pieces = [next_ps, next_nps]

		# # populate the next turns moves
		# # (the colors are swapped)
		next_mvs, next_nmvs = [], []
		for p in next_ps: 	next_mvs += m_funct.get_moves(board, p[1], p[2])
		for np in next_nps: next_nmvs += m_funct.get_moves(board, p[1], p[2])
		next_moves = [next_mvs, next_nmvs]

		# # pull the best move via negamax
		# # should be of form:
		# # [score_val, move]
		t = negamax(board, turn+1, [ncol,col], next_pieces, next_moves, depth-1)
		# # we will need to negate the score
		# # as that was from our opponent
		curr_score, curr_move = -t[0], t[1]
		# print("negamax - best score/move {} {}".format(curr_score,curr_move))

		# # if we capped a piece, more pts
		if (len(ps) > len(next_nps)): curr_score += 100

		# # if we have a move that is better
		# # for us than our best move, then
		# # we save that move/score
		if (curr_score >= best_score):
			best_score = curr_score
			best_move = m		

		# print(m)

	# print("negamax - best score/move {} {}".format(best_score, best_move))
	return [best_score, best_move]

# -----
# # pull info from the command line
# # in a acceptable index.
def human_player(moves):

	choice = -1

	while (choice == -1):

		try: choice = int(input(': '))
		except ValueError: choice = False

		if (choice == -1): return -1

		if (choice < 0 or choice >= len(moves)):
			choice = -1
			print_moves(moves, False)
		
	return choice

# -----
# # choose a move using a random index
def random_player(moves):
	
	title = "random_payer - "

	i = randrange(0, len(moves))
	print(title+"chose {}.".format(i))

	return i
 
# -----
# # choose a move using negamax you
# # do need to provide a depth > 0
# # (board, 70, [[0,0, 1,2], [...]], 6)
def negamax_player(arr, turn, moves, depth):

	if (depth == 0): 
		print("negamax_player - depth of 0 provided")
		assert(False)

	# # get the colors for current/next player
	if (turn%2 == 0): cols = [c_types.WHT, c_types.BLK]
	else: 						cols = [c_types.BLK, c_types.WHT]

	# # store the piece for the current player
	# # and the other player
	ps = b_funct.get_piece_list(arr, cols[0])
	nps = b_funct.get_piece_list(arr, cols[1])
	pieces = [ps, nps]

	# # get all moves for both piece sets
	mvs, nmvs = [], []
	for p in ps: mvs += m_funct.get_moves(arr, p[1], p[2])
	for np in nps: nmvs += m_funct.get_moves(arr, np[1], np[2])
	moves = [mvs, nmvs]

	# # return the index of the best move
	nega_move = negamax(arr, turn, cols, pieces, moves, depth)

	# # print and return the best move
	print("negamax_player - chose {}".format(nega_move))
	return moves[0].index(nega_move[1])

# -----
# # 
def player(arr, turn, wht_move, blk_move, moves):

	choice = -1
	function = ""

	if (turn%2 == 0): function = wht_move
	else:							function = blk_move

	# # get choice via command line
	if	 (function == c_types.HUMAN):		choice = human_player(moves)
	# # get choice via random index
	elif (function == c_types.RANDOM):	choice = random_player(moves)
	# # get choice via minichess server
	elif (function == c_types.REMOTE):	choice = random_player(moves)
	# # get choice via negamax logic
	elif (function == c_types.NEGAMAX):

		if (turn%2 == 0): depth = c_types.DEPTH		# # wht
		else: depth = c_types.DEPTH								# # blk

		choice = negamax_player(arr, turn, moves, depth)
		
	return choice


# -----

