from copy import deepcopy
'''
import math

def numcat(a,b):
    return int(math.pow(10,(int(math.log(b,10)) + 1)) * a + b)
'''
class State(object):
    """
        Represents a state in the solution of the boggle
        Attributes:
           board: an NxN matrix reprsenting the state of the board's letters
           moves: the sequence of letters visited so far
    """
    def __init__(self, board, moves):
        self.board = board
        self.moves = moves
        self.n = len(board)
        
    def neighbors(self, letter, prefix_dict):
        
        """
            Generate a new state by checking a position's surrounding letters 
            to check if it is a word in the prefix dictionary
        
            Input: a letter position in the board
        """
        
        row = letter / self.n
        #print row 
        col = letter % self.n
        #print col
        new_boards = deepcopy(self.board)
        new_moves = deepcopy(self.moves)
                                                    #add these as the neighbors
           
        original_letter = letter
        letter = new_boards[row][col]
        '''
        if letter + new_boards[row][col + 1] in prefix_dict:
            print letter + new_boards[row][col + 1]
        '''
        
        if row > 0:
            if letter + new_boards[row - 1][col] in prefix_dict:
                new_moves.append(row - 1, col)
            if col > 0:
                if letter + new_boards[row - 1][col - 1] in prefix_dict:
                    new_moves.append(row - 1, col - 1)
            if col < self.n - 1:
                new_boards[row - 1][col + 1]  
            '''
            if letter + new_boards[row - 1][col] in prefix_dict:
                temp = numcat(row - 1, col) - (row * 6)
                new_moves.append(temp)
            if col > 0:
                if letter + new_boards[row - 1][col - 1] in prefix_dict:
                    temp = numcat(row - 1, col - 1) - (row * 6)
                    new_moves.append(temp)
            if col < self.n - 1:
                new_boards[row - 1][col + 1]    
            '''
        if row < self.n - 1:
            new_boards[row + 1][col]
        if col > 0:
            new_boards[row][col - 1]
            if row < self.n - 1:
                new_boards[row + 1][col - 1]
        if col < self.n - 1:
            new_boards[row][col + 1] 
            if row < self.n - 1:
                new_boards[row + 1][col + 1]
            
        return State(new_boards, new_moves)

def already_visited(state, visited):
    if hash(state.board) in visited:
        return True
    else:
        return False
        



def hash(board):
    sum = 0
    
    for i in range(len(board) * len(board)):
        row = i / len(board)
        col = i % len(board)
        
        sum += 2 ** i * board[row][col]
    return sum
    
def add_to_visited(state, visited):
    h = hash(state.board)
    visited[h] = True


def load_words(filename='words.txt'):
    with open(filename) as f:
        word_list = {}
        for word in f:
            word_list[word.strip()] = True
    return word_list 

def prefix_generator(word_dict):
    
    prefix_dict = {}
    for word in word_dict:
        letter = ''
        if letter not in prefix_dict:
            prefix_dict[letter] = True
        for i in range(len(word) - 1):
            letter += word[i]
            if letter not in prefix_dict:
                prefix_dict[letter] = True
    return prefix_dict

def print_grid(grid):
	"""
	Simple utility method for displaying the grid
	"""
	for r in grid:
		print r

def solve(board):
    moves = []
    
    state = State(board, moves)
    '''
    coordinates = []
    x, y = 0, 0
    while x < len(board):
        while y < len(board):
            coordinates.append((x, y))
            y += 1
        x += 1 
    '''
    word_dict = load_words()
    prefix_dict = prefix_generator(word_dict)
    
    # The queue of frontier states
    queue = []
    queue.append(state)
    
    # Dictionary of previously expanded states
    visited = {}
    
    print_grid(board)
    #print len(board)
    
    '''
    for word in sorted(prefix_dict):
        print word
    '''
    
    
    
    while len(queue) > 0:
        state = queue.pop(0)
        
        # Do the letters formed by the coordinates of state correspond to a word
        # if so, print it
        # Expand the current state by considering all possible flips
        for i in range(len(board) * len(board)):
            new_state = state.neighbors(i, prefix_dict)
            '''
            if not already_visited(new_state, visited):
                add_to_visited(new_state, visited)
                queue.append(new_state)
            '''
        # for all the neighbors of the last coordinate
        #    is that neighbor a valid addition to the prefix represented by this state
        #    test if the neighbor is on the grid
        #    test if you have previously visited the neighbor
        #    test if the prefix inclduing the neighbor is a valid prefix of any word
        
        #    If the neighbor is a valid addition
        #      copy the state to make a new state
        #      add the new coordinate to the end of the list
        #      insert the new state into the queue
        
        '''
        def neighbors((x, y)):
            for nx in range(max(0, x-1), min(x+2, ncols)):
                for ny in range(max(0, y-1), min(y+2, nrows)):
                    yield (nx, ny)
                    
        
        
        '''
        
        
if __name__ == '__main__':
    board = [
                 ['u', 'n', 't', 'h'],
	             ['g', 'a', 'e', 's'],
	             ['s', 'r', 't', 'r'],
	             ['h', 'm', 'i', 'a']
	        ]
    solve(board)