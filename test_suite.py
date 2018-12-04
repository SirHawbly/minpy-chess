
# -----
import chess_types 			as c_types
import board_functions 	as b_funct
import chess_functions 	as c_funct

# -----
verbose = True

# -----
def vprint(string, verbose):

	if(verbose): print(string)

# -----
# # a function to read in a frame file given a 
# # title, this includes, the turn, turn count,
# # and the piece layout.
# # "20 W", "...QK", ".PP.P", ...
def read_frame_file(name):

	arr = []	

	# # read in 7 lines, stripping out the '\n'
	with open(name, "r") as f:
		for i in range(0,7):
			arr += [f.readline().replace("\n", ""), ]

	# # return the frame array
	return arr

# -----
# # given a list of pieces, and list of pieces
# # that should be there, remove pieces from 
# # both lists, until either throws and error,
# # or both are empty (they where the same).
def assertPieces(pieceList, givenPieces, ver):

	title = "assertPieces - " 
	first = "checking {} == {}".format(pieceList, givenPieces)

	vprint(title + first, ver)

	# # if both lists dont have the same length,
	# # print error, assert false.
	if (len(pieceList) != len(givenPieces)):
		second = "lists have different length."
		vprint(title + second, ver)
		assert(False)

	while(pieceList):

		# # try to remove pieces from both Piece Lists
		# # if any fail, print error, assert false. 
		# # pieces should be [piece-type, y, x]
		pc = pieceList.pop(0)

		try: givenPieces.remove(pc)
		except ValueError: 	
			third = "remove {} from {} failed.".format(pc, givenPieces)
			vprint(title + third, ver)
			assert(False) 

	return True

# -----
# # given a list of moves, and a list of moves
# # that should be there, remove moves from both 
# # lists until either a list throws an error, or
# # or one is still around, or they are empty.
def assertMoves(moveList, givenMoves, ver):

	title = "assertMoves - " 
	first = "checking {} == {}".format(moveList, givenMoves)
	vprint(title + first, ver)

	if (len(moveList) != len(givenMoves)):
		second = ("lists differnt length {} ".format(len(moveList)) + 
								"and {}.".format(len(givenMoves)))
		vprint(title + second, ver)
		assert(False)

	while(moveList):

		# # try to remove moves from both Move Lists
		# # if any fail, print error, assert false.
		# # moves should be [y1,x1, y2,x2]
		mv = moveList.pop(0)

		try: givenMoves.remove(mv)
		except ValueError: 	 
			third = "remove {} from {} failed.".format(pc, givenPieces)
			vprint(title + third, ver)
			assert(False)
	
		return True

# -----
# # read in an empty board with just a king
# # and assert there are 8 moves to make 
def test_one(ver):

	print("Test 1 ...")

	arr = []
	frame = [ "20 B",
						".....",
						".....",
						"..k..",
						".....",
						".....",
						"....." ]
	i = False
	turn = False
	moves = []

	[i,turn,arr] = b_funct.load_board(frame)
	vprint("\ni: {}, turn: {}".format(i, turn), ver)
	for row in arr: vprint("arr: {}".format(row), ver)

	ps = b_funct.get_piece_list(arr, turn)
	vprint("\npieces {}\n".format(ps), ver)

	for p in ps:
		moves += c_funct.get_moves(arr, p[1], p[2])
	vprint("\nmoves: {}\n".format(moves), ver)

	assert (len(moves) == 8)

	print("Test 1: Passes")

# -----
# # read in an empty board with just a king
# # and assert there are 8 moves to make 
def test_two(ver):

	print("Test 2 ...")

	frame = [ "21 B",
						".....",
						"..Pp.",
						"..pP.",
						".....",
						".....",
						"....." ]

	i = 0
	turn = False
	arr = []
	ps = []
	nps = []
	moves = []
	nmoves = []

	[i,turn,arr] = b_funct.load_board(frame)

	if(turn == c_types.BLK): 	nturn = c_types.WHT
	else: 										nturn = c_types.BLK
	
	vprint("\ni: {}, turn: {}".format(i, turn), ver)

	# for row in arr: vprint("arr: {}".format(row), ver)
	b_funct.print_board(arr)

	ps = b_funct.get_piece_list(arr, turn)
	nps = b_funct.get_piece_list(arr, nturn)

	for p in ps:
		moves += c_funct.get_moves(arr, p[1], p[2])
	for p in nps:
		nmoves += c_funct.get_moves(arr, p[1], p[2])

	# # these should be true, if not, i
	# # will assert(False)
	# assert (len(moves) == len(nmoves))
	givenPs = [['p', 1, 3], ['p', 2, 2]]	
	givenNps = [['p', 1, 2], ['p', 2, 3]]
	vprint("\npieces {}\nnpieces {}\n".format(ps,nps), ver)
	vprint("Given pcs: {}\nGiven npcs: {}\n".format(givenPs, givenNps), ver)

	assertPieces(ps, givenPs, ver)
	assertPieces(nps, givenNps, ver)
	
	givenMvs = [[2, 2, 3, 2]]
	givenNmvs = [[1, 2, 0, 2]]
	vprint("\nmoves: {}\nnmoves: {}\n".format(moves, nmoves), ver)
	vprint("Given moves: {}\n".format(givenMvs) + 
					"Given nmoves: {}\n".format(givenNmvs), ver)

	assertMoves(moves, givenMvs, ver)
	assertMoves(nmoves, givenNmvs, ver)

	print("Test 2: Passes")

# -----
# # given the moves, pieces, and a frame,
# # check that chess functions are able to
# # find all of them correctly.
def test(frame, givenPs, givenNps, givenMvs, givenNmvs, ver):

	# # load the board, turn count, and turn
	[i,turn,arr] = b_funct.load_board(frame)

	# # set the other turn type
	if(turn == c_types.BLK): 	nturn = c_types.WHT
	else: 										nturn = c_types.BLK

	# # print out info pulled from the frame
	vprint("\ni: {}, turn: {}".format(i, turn), ver)
	b_funct.print_board(arr)

	# # pull the pieces from the board
	ps = b_funct.get_piece_list(arr, turn)
	nps = b_funct.get_piece_list(arr, nturn)
	vprint("\npieces {}\nnpieces {}\n".format(ps,nps), ver)
	
	# # set up move lists
	moves = []
	nmoves = []

	# # pull both sides possible moves
	for p in ps:
		moves += c_funct.get_moves(arr, p[1], p[2])
	for p in nps:
		nmoves += c_funct.get_moves(arr, p[1], p[2])
	vprint("moves: {}\nnmoves: {}\n".format(moves,nmoves), ver)

	# # assert pieces for both sides
	assertPieces(ps, givenPs, ver)
	assertPieces(nps, givenNps, ver)
	
	# # assert moves for both sides
	assertMoves(moves, givenMvs, ver)
	assertMoves(nmoves, givenNmvs, ver)

	return True

# -----
# # given a frame file, a tuple with pieces and 
# # a tuple of moves, assert that all are found 
# # using the python functions.
# # ('file', [ps, nps], [mv, nmv], verbose)
def run_test(frame_file, pieces, moves, ver):
	
	frame = read_frame_file(frame_file)

	givenPs = pieces[0]
	givenNps = pieces[1]

	givenMvs = moves[0]
	givenNmvs = moves[1]

	test(frame, givenPs, givenNps, givenMvs, givenNmvs, ver)

	return True

# -----
# # run the board tests, to make sure pieces and
# # moves are being found/stored.
def board_tests():

	print("Running Tests: ")

	# # run all board tests, providing
	# # whether or not to use prints

	# # test a given frame
	test_one(False)
	test_two(False)

	# # test reading in a frame
	print("Test 3 ...")
	ps = [['k',0,0], ['r',1,0], ['p',1,1], ['p',2,0]]
	nps = [['k',0,2], ['p',1,2], ['p',2,1], ['p',3,0]]
	mv = [[0,0, 0,1]]
	nmv = [[2,1, 1,0], [0,2, 0,1], [0,2, 0,3], [0,2, 1,3], [0,2, 1,1]]
	run_test("movetests/king-vs-king.in", [ps,nps], [mv,nmv], False)
	print("Test 3: Passes")

	print("All Tests Passed.")

# -----
board_tests()

# -----

