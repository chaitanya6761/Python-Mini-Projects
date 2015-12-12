# Mini-project #6 - Blackjack
# codeSkluptor link : http://www.codeskulptor.org/#user40_VCTO8mDaRGFhptd_0.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit 

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        if in_play and (pos[0]==30 and pos[1]==395):
            canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

        else :
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    
    def __init__(self):
        # create Hand object
        
        self.lstOfCards=[]
                
    def __str__(self):
        # return a string representation of a hand
        
        var = 'Hand contains '
        
        for card in self.lstOfCards :
            var += (card.get_suit() + card.get_rank()) + ' '
            
        return var    
        
    def add_card(self, card):
        # add a card object to a hand
        
        self.lstOfCards.append(card)
        
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        
        total=0
        flag=0
        
        for card in self.lstOfCards :
            total = total + VALUES[card.get_rank()]
            if card.get_rank() == 'A' :
                flag+=1
        
        if flag == 0:
            return total
            
        else:
            if total + 10 <= 21 :
                return total + 10
            else :
                return total
                 
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        
        for card in self.lstOfCards :
            
            card.draw(canvas,pos)
            pos[0] += 80
            
#define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.lstOfCards = []
        
        for suit in SUITS :
            
            for rank in RANKS :
                
                self.lstOfCards.append(Card(suit,rank))
        
        

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        
        return random.shuffle(self.lstOfCards)

    def deal_card(self):
        # deal a card object from the deck
        
        return random.choice(self.lstOfCards)
    
    def __str__(self):
        # return a string representing the deck

        var = ''
        for card in self.lstOfCards :
            var += card.get_suit()+card.get_rank() + ' '
        return var    



deckOfCards = Deck()
player_hand = Hand()
dealer_hand = Hand()
    
#define event handlers for buttons
def deal():
    global outcome, in_play ,deckOfCards ,player_hand ,dealer_hand,score
    deckOfCards = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    deckOfCards.shuffle()
    
    if in_play :
        score -= 1
        outcome = 'Player has busted. Dealer won.'
        
    else :
        outcome = 'New Game Started  Hit or Stand'
    
    # your code goes here
    
    for i in range(2):
        player_hand.add_card(deckOfCards.deal_card())
        dealer_hand.add_card(deckOfCards.deal_card())
    
    
    in_play = True

def hit():
    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
    
    global outcome ,in_play ,score ,player_hand
    
    if in_play :
        player_hand.add_card(deckOfCards.deal_card())
        
        if player_hand.get_value() > 21 :
            outcome = 'Player has busted and Dealer won the Hand'
            in_play=False
            score -= 1
            
        else :
            outcome = 'Hit or Stand'
    
    else:
        outcome='Game Over'
    
    
    
def stand():
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    
    global dealer_hand ,in_play ,score ,outcome
    
    if in_play == False :
        outcome = 'Game Over'
        
    else : 
        
        flag = 0
    
        while True :
        
            if dealer_hand.get_value() > 17:
                flag = 1
                break
            else :
                dealer_hand.add_card(deckOfCards.deal_card())
        
        in_play=False
        if flag == 1 :
            
            if dealer_hand.get_value() > 21 :
                
                outcome = 'Dealer has busted and Player won the Hand'
                score += 1
                
            else :
                
                if player_hand.get_value() > dealer_hand.get_value() :
                    score += 1
                    outcome = 'Player won the Hand'
                    
                elif player_hand.get_value() <= dealer_hand.get_value() :
                    score -= 1
                    outcome = 'Player lost the Hand'
                    

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_text('Blackjack', (250, 40), 30, 'yellow')
    canvas.draw_text(outcome,(30,100),20,'white')
    temp = "score: " +  str(score)
    canvas.draw_text(temp,(450,100),20,'white')
    canvas.draw_text("Player's Hand:",(30,150),20,'white')
    canvas.draw_text("Dealer's Hand:",(30,375),20,'white')
    
    player_hand.draw(canvas,[30,170])
    dealer_hand.draw(canvas,[30,395])
    
    
    
    
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

