
# -----
import chess_types as c_types

# -----
def get_pawns(clr):

	return [['p',clr,], ['p',clr,], ['p',clr,], ['p',clr,], ['p',clr,],]

# -----
def get_other(clr):

	return [['r',clr,], ['n',clr,], ['b',clr,], ['q',clr,], ['k',clr,],]

# -----
def get_space(clr):

	return [['.',clr,], ['.',clr,], ['.',clr,], ['.',clr,], ['.',clr,],]

# -----
def create_board(arr):

	arr += [get_other(c_types.BLK)]
	arr += [get_pawns(c_types.BLK)]
	arr += [get_space(c_types.NON)]
	arr += [get_space(c_types.NON)]
	arr += [get_pawns(c_types.WHT)]
	arr += [get_other(c_types.WHT)]

# -----
def print_board(arr):

	for i in range(0, len(arr)-1): 
		print("  {}".format(c_types.columns[i]), end = '')

	i = 0
	for row in arr:

		print( ('\n'+str(i)) ,end=' ')

		i += 1
		for pc in row:

			if (pc[c_types.c] == c_types.BLK):
				print("{}  ".format(pc[c_types.p].lower()), end='')
			else:
				print("{}  ".format(pc[c_types.p].upper()), end='')

	print('')

# -----
# # given a move, place the piece
# # at the starting position at 
# # the ending position and put
# # a blank piece on the starting
def move_piece(arr, m):

	if (len(m) != 4): assert(False)

	arr[m[2]][m[3]] = arr[m[0]][m[1]]
	arr[m[0]][m[1]]   = ['.', c_types.NON,]

# -----
def get_piece_list(arr, clr):

	pieces = []

	for row,i in zip(arr, range(0, len(arr))):
		for pc,j in zip(row, range(0, len(row))):
			if (pc[c_types.c] == clr):
				pieces += [[pc[c_types.p], i, j], ]

	return pieces

# -----
# # given a log file, print out the board who's
# # move, and the amount of turns left
def log_board(log, arr, i, turn): 

	# # log the board state
	log.write("\n{} - {}\n".format(i,turn))

	for i in range(0, len(arr)-1): 
		log.write("  {}".format(c_types.columns[i]))

	i = 0
	for row in arr:

		i = i+1
		log.write("\n{} ".format(i))

		for pc in row:
			if (pc[c_types.c] == c_types.BLK):
				log.write("{}  ".format(pc[0][0].lower()))
			else:
				log.write("{}  ".format(pc[0][0].upper()))

# -----
# # given a frame string, parse it into
# # its 3 parts, turn, turn count, and 
# # board and return all in list of lists.
# # frame ["20 B", "kPq..", ... ]
# # [i,turn,arr] = load_board(frame)
def load_board(frame_string):

	i = 0
	turn = c_types.NON
	arr = []

	for line in frame_string:

		# # the first line in the board is the turn
		# # count and the coor.
		if (line == frame_string[0]):

			# # strip the color, its the last character
			col = line[-1]
			if (col == 'W'): 	turn = c_types.WHT
			else:							turn = c_types.BLK

			# # if line[1] isnt a space, we need to bump
			# # line[0] up a magnitude and add line[1]
			i = int(line[0])
			if (line[1] != ' '): 
				i *= 10
				i += int(line[1])

		else :

			pcs = []
			assert(len(line) == 5)

			for p in line:

				if (p == '.'):				pcs += [['.', 			c_types.NON]]
				elif (p.isupper()): 	pcs += [[p.lower(), c_types.WHT]]
				else:					 				pcs += [[p.lower(), c_types.BLK]]

			arr += [pcs,]

	return [i,turn,arr]

# -----
def board_value(arr, col, ncol):

	pcs = []
	npcs = []
	value = 0

	for row in arr:
		for pc in row:
			if (pc[1] == col):
				pcs += [pc]
			elif (pc[1] == ncol):
				npcs += [pc]

	for pc in pcs:
		value += c_types.piece_weights[c_types.pieces.index(pc[0])]
	for npc in npcs:
		value -= c_types.piece_weights[c_types.pieces.index(npc[0])]

	return value

# -----

