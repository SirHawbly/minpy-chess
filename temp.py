# -----
# # go through all of the moves, making them,
# # and trying to find the value of them, if
# # that value is the worst for out opponent, 
# # we will choose that one
def negamax(arr, turn, cols, pieces, moves, depth):

	# # figure out the next color for next turn
	[col,ncol] = cols
	[ps,nps] = pieces
	[mvs,nmvs] = moves

	# # if we have 0 moves to make this turn, we lose
	if (len(mvs) == 0):
		# print("negamax - no moves, returning {}".format(best_score))
		best_move  = []
		best_score = -1000000
		return [best_score, best_move]

	# # default value, any/all moves are better
	best_move, board = moves[0], deepcopy(arr)
	b_funct.move_piece(board, best_move)
	best_score = b_funct.board_value(board, col, ncol)

	# # if depth is 0, we need to return the 
	# # current board's value
	if (depth == 0):	
		best_score = b_funct.board_value(arr, col, ncol) + len(moves)*10
		best_move = []
		# print("negamax - depth == 0, returning {}".format(curr_score))
		return [best_score, best_move]

	# # I guess we can return a score of 0 here, if 
	# # that is better than any other move, i guess
	# # we can take the tie.
	if (turn == 80):
		curr_score = 0
		curr_move = []
		return [curr_score,curr_move]

	for m in moves:

		# # copy the board, so that we can mod it
		# # and make the current move on it
		board = deepcopy(arr)
		# print("negamax - {}".format(m))
		b_funct.move_piece(board, m)
	
		# # if we are in a game state that has ended we
		# # can return the game state
		nps = b_funct.get_piece_list(board, ncol)
		print("col{},ncol{}\nnps{}".format(col,ncol,nps))
		nval = False
		for np in nps: 
			if (nps[0] == 'k'): 
				nval = True
		if (nval == False):
			print("their king is dead")
			curr_score = b_funct.board_value(board, col, ncol)
			curr_move = m
			print("negamax - {}:{}".format(curr_score, curr_move))
			return [curr_score,curr_move]

		# # populate the possible moves from new pieces
		nmoves = []
		for np in nps:
			pc = arr[np[1]][np[2]]
			assert (pc[0] == np[0])
			nmoves += get_moves(arr, np[1], np[2])

		# # get the value of the board given that move
		curr_score = -negamax(board, turn+1, ncol, nmoves, depth-1)[0]
		curr_move = m
		# print("negamax - {} -> {}".format(curr_move, curr_score))

		# # if we have found a better move, set best move
		if (curr_score >= best_score):
			# string = "{}:{} >= {}:{}".format(
				# curr_score,curr_move, best_score,best_move)
			# print("negamax - new best " + string)
			best_move = curr_move
			best_score = curr_score

	# # if at the top level, print out the
	# # best move, and tis score	
	# if (depth == c_types.DEPTH):	
		# print("negamax - best move {}:{}".format(best_score, best_move))

	return [best_score, best_move]

# -----
