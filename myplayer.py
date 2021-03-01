import random
import sys
import copy
sys.path.append('..')
from common import board


class BoardNode:
	def __init__(self, y, x, parent = None):
		self.y = y
		self.x = x
		self.parent = parent
		self.value = 0
		self.children = []

def make_move(the_board, color):
    """
    Returns a random move from the list of possible ones
    :return: (int, int)
    """
    color = board.Board.WHITE if color == 'white' else board.Board.BLACK
    legal_moves = the_board.legal_moves(color)
    minimax_decision(the_board, 'W', 0)
    return random.choice(legal_moves) if len(legal_moves) > 0 else (-1, -1)

def minimax_decision(the_board, color, depth):
    print('STARTED MAKING TREE')
    our_board = copy.deepcopy(the_board)
    finalValue = max_value(our_board, color, depth)		

def max_value(the_board, color, depth):
	if depth > 3:
	    print('STOPED MAX VALUE')
	    return 0 # TODO: FUNCAO UTILIDADE
	currentValue = -100000
	for element in the_board.legal_moves(color):
		newBoard = copy.deepcopy(the_board)
		print("Max. Altura atual: ", depth)
		newBoard.process_move(element, color)
		newBoard.print_board()
		currentValue = max(currentValue, min_value(newBoard, 'B', depth + 1))
	
	return currentValue		

def min_value(the_board, color, depth):
	if depth > 3:
	    print('STOPED MIN VALUE')
	    return 0 # TODO: FUNCAO UTILIDADE
	currentValue = 100000
	for element in the_board.legal_moves(color):
		newBoard = copy.deepcopy(the_board)
		print("Min. Altura atual: ", depth)
		newBoard.process_move(element, color)
		newBoard.print_board()
		currentValue = min(currentValue, max_value(newBoard, 'W', depth + 1))
	
	return currentValue

if __name__ == '__main__':
    b = board.from_file(sys.argv[1])
    f = open('move.txt', 'w')
    f.write('%d,%d' % make_move(b, sys.argv[2]))
    f.close()


