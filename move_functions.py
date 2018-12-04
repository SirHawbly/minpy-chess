
# -----
import chess_types as c_types

# -----
def in_bounds(x, y, x_max, y_max):

	if ((0 <= x and x < x_max) and (0 <= y and y < y_max)): 
		# print('in bounds '+str(x)+" "+str(y))
		return True
	else:
		# print('out of bounds '+str(x)+" "+str(y))
		return False

# -----
def scan(arr, x,y, dx,dy, short, cap, clr):

	moves = []
	(tx,ty) = (x+dx,y+dy)

	while ( in_bounds(tx,ty, len(arr),len(arr[0])) ):	 

		pc = arr[tx][ty]
		if (pc[c_types.p] != '.'): 

			if (pc[c_types.c] == clr): 
				# print("... match clr")
				break
			elif (cap == c_types.F): 
				# print("... no cap")
				break
			else: 
				# print("... hit a piece")
				short = True

		else:
			if (cap == c_types.O): 
				# print("... cap only")
				break

		# print("adding (" + str(x)+", "+str(y) + 
		# 				")->(" + str(tx)+", "+str(ty) + ")")

		moves += [[x,y, tx,ty], ]
		(tx,ty) = (tx+dx,ty+dy)

		if (short): 
			# print("... short")
			break

	return moves

# -----
def sym_scan(arr, x,y, dx,dy, short, cap, clr):

	tx = dx
	ty = dy
	moves = []

	for i in range(0,4):
		moves += scan(arr, x,y, tx,ty, short, cap, clr)
		(tx,ty) = (ty,-tx)

	return moves

# -----
def get_moves(arr, x,y):

	# # store the piece info and a list for moves
	moves = []
	pc			= arr[x][y][0]
	clr		 = arr[x][y][1]

	# # moves are added using sym_scan and scan 
 	# # (sym_scan being a scan in all directions)
	# # using the format:
	# # scan(array, x,y, dx,dy,
	# #				stop_short, capture_type, color)

	# # Pawn Direction (wht is -1, invert for blk)
	direct			= -1 
	# # stop short can be True(T) or False(F)
	# # capture can be True(T), False(F) or Only(O)
	 		
	# # kings and queens can move all directions
	# # but kings need to stop short.
	if	 (pc == 'k' or pc == 'q'):
		moves +=			sym_scan(arr, x,y, 0, 1, 
														(pc == 'k'), c_types.T, clr)
		moves +=			sym_scan(arr, x,y, 1, 1, 
														(pc == 'k'), c_types.T, clr)

	# # bishops and rooks can move latterally, but 
	# # bishops have to stop short and cannot cap,
	# # they can also move diagonally unimpeded.
	elif (pc == 'b' or pc == 'r'):
		moves += 			sym_scan(arr, x,y, 0, 1, 
														(pc == 'b'), (pc == 'r'), clr)
		if (pc == 'b'):
			moves += 	sym_scan(arr, x,y, 1, 1,	
													c_types.F, c_types.T, clr)
		
	# # knights need to move in an L shape. they
	# # have a max of 8 possible moves.
	elif (pc == 'n'):
		moves +=			sym_scan(arr, x,y, 2,	1, 	
														c_types.T, c_types.T, clr)
		moves +=			sym_scan(arr, x,y, 2, -1, 
														c_types.T, c_types.T, clr)

	# # pawns have two moves that only can capture
	# # or move foreward by one, for blk it needs 
	# # to be inverted, dir=-1 (whts dir)
	elif (pc == 'p'):

		if (clr == c_types.BLK): direct = -direct

		moves += 					scan(arr, x,y, direct, -1, 
														c_types.T, c_types.O, clr)
		moves += 					scan(arr, x,y, direct,	1, 
														c_types.T, c_types.O, clr)
		moves += 					scan(arr, x,y, direct,	0, 
														c_types.T, c_types.F, clr)

	c_types.assert_type(c_types.MOVE_LIST, moves)
		
	return moves

# -----

