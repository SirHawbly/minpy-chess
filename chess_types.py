
# -----
# # variables for the board  
columns = ['a', 'b', 'c', 'd', 'e']
rows		= [1, 2, 3, 4, 5, 6]

# -----
# # variables for the pieces, [type, color]
p = 0 
c = 1
pieces  			 = ['p', 'n', 'b', 'r', 'k', 'q', '.']
piece_weights  = [ 15,  5,  10,  20,  1000, 100] 

# -----
# # variables for piece color
BLK = 'Blk'
WHT = 'Wht'
NON = 'Non'

# -----
# # variables for move generation
F 	= 'False'
T 	= 'True'
O 	= 'Only'

# -----
# # variables for defining which players to use
HUMAN   = "Human"
REMOTE  = "Remote"
RANDOM  = "Random"
NEGAMAX = "Negamax"
DEPTH 	= 3

# -----
# # variables for what types are being used
PIECE 			= "Piece"
PIECE_LIST 	= "Piece_List"
COORD_LIST 	= "Coord_List"
MOVE_LIST 	= "Move_List"
BOARD 			= "Board"

# -----
def assert_type(typ, obj):

	if (not typ): 
		print("assert_type - no type provided")
		assert(False)

	# # -----
	# # a piece is a piece-type and a color.
	# # type should be in the piece list above
	# # color should be either blk, wht or non
	# # [PIECE, COL]
	if (typ == PIECE):

		# # check that the piece is two parts [type, col]
		if (len(obj) != 2):
			print("assert_type - piece contains {} ".format(len(obj)) + 
							"parts (not 2).")
			assert(False) 

		# # check that the piece's type is in the pieces list
		if (obj[0] not in pieces):
			print("assert_type - piece type not in type list " +
							"{} ({}).".format(obj[0], pieces))
			assert(False)

		# # check that the piece is in one of three colors
		if (obj[1] not in [BLK, WHT, NON]):
			print("assert_type - piece contains {} ".format(obj[1]) + 
							"not a good color.")
			assert(False)

	if (typ == PIECE_LIST):
		for pc in obj:
			try:
		 		assert_type(PIECE, pc)
			except AssertionError: 
				print("assert_type - piece in piece list {} ".format(obj) + 
								"not in piece format {} ".format(pc) + 
								"([[TYP, COL], ...]).")

	# # -----
	# # a piece list is a list of pieces and a
	# # coordinate where that piece lies in an
	# # array.
	# # [[pc, y, x], ... ]
	if (typ == COORD_LIST):

		for pc in obj:

			# # check that the piece has three parts, (typ,y,x)
			if (len(pc) != 3):
				print("assert_type - coord in piece list not correct " +
								"{} form (pc,y,x).".format(pc))
				assert(False)

			# # verify that the piece type is in the pieces array
			if (pc[0] not in pieces):
				print("assert_type - coord type not in list " + 
								"{} ({}).".format(pc[0], pieces))
				assert(False)

			# check that the y coordinate is in the acceptable range
			if (pc[1] < 0 or pc[1] > 5):
				print("assert_type - coord y not in range 0 < " + 
								"{} > 5.".format(obj[1]))
				assert(False)

			# check that the x coordinate is in the acceptable range
			if (pc[2] < 0 or pc[2] > 4):
				print("assert_type - coord x not in range 0 < " + 
								"{} > 4.".format(obj[1]))
				assert(False)

	# # -----
	# # a move list is a list of coordinates,
	# # both 0 < x < 5 and 0 < y < 6 should be 
	# # true for all xs and ys in the moves.
	# # [[y1,x1, y2,x], ...]
	if (typ == MOVE_LIST):

		for move in obj:
			y1,x1 = [move[0], move[1]]
			y2,x2 = [move[2], move[3]]

			# # check that any move in the list has four pieces, [y,x, y,x]
			if (len(move) != 4): 
				print("assert_type - move in list not in {} ".format(obj) +
								"form [[y1,x1, y2,x2], ...].")
				assert(False)

			# # check that both y variables are in between 0 and 5
			if (y1 < 0 or y1 > 5):
				print("assert_type - y1 was not in range 0 < {} > 5.".format(y1))
				assert(False)

			if (y2 < 0 or y2 > 5):
				print("assert_type - y2 was not in range 0 < {}	> 5.", y2)
				assert(False)

			# # check that both x variables are in between 0 and 4
			if (x1 < 0 or x1 > 4):
				print("assert_type - x1 was not in range 0 < {} > 4.", x1)
				assert(False)

			if (x2 < 0 or x2 > 4):
				print("assert_type - x2 was not in range 0 < {} > 4.", x2)
				assert(False)

	# # -----
	# # a board is a list of six list with 5 pieces
	# # per list, they should all follow the piece 
	# # guidelines
	# # [[PIECE, TYPE, ...], [], [], [], [], []]
	if (typ == BOARD):
		
		# # check that the board has 6 rows
		if (len(obj) != 6):
			print("assert_type - board contains {} rows (not 6).", len(obj))
			assert(False)

		# # check that any row in the board has 5 pieces inside
		for row in obj:

			if (len(row) != 5):
				print("assert_type - board contains a row with " +
								"{} pieces (not 5).".format(len(row)))
				assert(False)

			# # for all pieces in the board's rows, check they are valid
			for pc in row:
				try: 		
					assert_type(PIECE, pc)
				except AssertionError:
					print("assert_type - piece {} is an invalid ".format(pc) + 
								"piece (TYPE, COL).")
					
# -----
def assert_argument_list(arguments):

	# # given an arg list in the type [[TYPE, ARG], ...]
	# # run through all of them, asserting their assigned
	# # type.
	for arg in arguments: 

		if (len(arg) != 2):
			# # assert all arguments are paired with a type
			print("assert_argument_list - arg with incorrect form " + 
							"{} (TYPE, ARGUMENT).", arg)
			assert(False)

		# # go through all of the arguments, asserting their type
		assert_type(arg[0], arg[1])

# -----

