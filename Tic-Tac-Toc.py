"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.

NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    '''
    To compute a single trials
    '''
    
    while True:
        empty_squares = board.get_empty_squares()
        square = random.choice(empty_squares)
        board.move(square[0],square[1],player)
        
        if board.check_win() == None :
            player = provided.switch_player(player)
        else :
            break
            
def mc_update_scores(scores, board, player):
    '''
    To update score grid
    '''
    winner = board.check_win()
    
    if winner == provided.DRAW :
        calculate(scores, board, player, 0, 0)
    
    elif winner == player :
        calculate(scores, board, player, SCORE_CURRENT, -SCORE_OTHER)
        
    else :    
        calculate(scores, board, player, -SCORE_CURRENT, SCORE_OTHER)
        
                    
def calculate(scores, board, player, score_current, score_other):
    '''
        To calculate score
    '''
    
    
    dim = board.get_dim()
    
    for dummy_i in range(dim) :
            for dummy_j in range(dim):
                if board.square(dummy_i,dummy_j) == player :
                    scores[dummy_i][dummy_j] +=  score_current
                elif board.square(dummy_i,dummy_j) == provided.switch_player(player) :    
                    scores[dummy_i][dummy_j] +=  score_other
                else :
                    scores[dummy_i][dummy_j] += 0
                    
                    
                    
def get_best_move(board, scores):
    '''
    To get a best move
    '''
    
    empty_squares = board.get_empty_squares()
    high_score = -10000
    lst =[]
    
    for pos in empty_squares :
        if scores[pos[0]][pos[1]] > high_score :
            high_score = scores[pos[0]][pos[1]]
    for pos in empty_squares:
        if scores[pos[0]][pos[1]] == high_score:
            lst.append(pos)
            
    return random.choice(lst)

def mc_move(board, player, trials):
    '''
    To perfom monte carlo
    '''
    
    
    dim = board.get_dim()
    scores = [[ 0 for dummy_j in range(dim)] for dummy_i in range(dim)]
    count = 0 
    while count < (trials):
        new_board = board.clone()
        mc_trial(new_board, player)
        mc_update_scores(scores, new_board, player)
        count += 1
    return get_best_move(board, scores)     
        
    
    

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS,False)
