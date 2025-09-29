#What is the expected number of cards you need to draw from a 52-card deck before you see the first ace?
#https://openquant.co/questions/race-to-ace





import random

def first_ace():
    deck = list(range(1, 14)) * 4 # deck of cards
    random.shuffle(deck)
    
    counter = 0
    for card in deck:
        counter += 1
        if card == 1:  # if ace
            return counter


num_simulations = 100_000 # no. of simulations
total_cards = 0

for i in range(num_simulations):
    total_cards += first_ace()

average_cards = total_cards / num_simulations




print("Average cards drawn = ", average_cards )

