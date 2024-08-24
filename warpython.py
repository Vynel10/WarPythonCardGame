## WarPython the card game ## 

# Imports #
import random

# Creating a player class to handle playernames #
class Player:
    def __init__(self, player_name):
        self.player_name = player_name

    def __repr__(self, player_name):
        return (Player[f"player_name = {self.player_name}"])
    
class Opponent:
    def __init__(self, opponent_name):
        self.opponent_name = opponent_name

    def __repr__(self, opponent_name):
        return (Opponent[f"opponent_name = {self.opponent_name}"])
    

# Establishing Card Values and necessary variables and lists #

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = [value + ' of ' + suit for value in values for suit in suits]

card_values = {str(i): i for i in range(2, 11)}
card_values.update({"J": 11, "Q": 12, "K": 13, "A": 14})


# Creating functions for running the game #

def shuffle_deck():
    # Shuffles the deck of cards #
    deck = [value + " of " + suit for value in values for suit in suits]
    random.shuffle(deck)
    return deck

def deal_deck(deck):
    # Splits shuffled deck into half and gives each half to the player and opponent #
    return deck[:26], deck[26:]

def war_loop(player, opponent):
    # This is the main game loop for War #
    deck = shuffle_deck()
    player.deck, opponent.deck = deal_deck(deck)

    round_counter = 0
    while player.deck and opponent.deck:
        round_counter += 1
        print(f"Round {round_counter}:")
        card1 = player.deck.pop(0)
        card2 = opponent.deck.pop(0)
        print(f"{player.player_name} plays {card1}")
        print(f"{opponent.opponent_name} plays {card2}")

        card1_value = card_values[card1.split(" ")[0]]
        card2_value = card_values[card2.split(" ")[0]]

        if card1_value > card2_value:
            print(f"{player.player_name} wins this round!\n")
            player.deck.extend([card1, card2])
        elif card1_value < card2_value:
            print(f"{opponent.opponent_name} wins this round!\n")
            opponent.deck.extend([card1, card2])
        else:
            print("War!\n")
            player.deck, opponent.deck = handle_war(player, opponent)
        
        #If player or opponent runs out of cards, win condition#
        if not player.deck:
            print(f"{player.player_name} has run out of cards. {opponent.opponent_name} wins the game!")
            break
        elif not opponent.deck:
            print (f"{opponent.opponent_name} has run out of cards. {player.player_name} has won the game!")
            break

def handle_war(player, opponent):
    #This is the handler function for when war happens, where two cards tie.#
    if len(player.deck) < 4 or len(opponent.deck) < 4:
        return player.deck, opponent.deck # Not enough cards to continue war.
    
    #Players place three cards face down and one face up#
    face_down_cards1 = player.deck[:3]
    face_down_cards2 = opponent.deck[:3]
    face_up_card1 = player.deck[3]
    face_up_card2 = opponent.deck[3]

    print(f"{player.player_name} places {face_down_cards1} face down and plays {face_up_card1}.")
    print(f"{opponent.opponent_name} places {face_down_cards2} face down and plays {face_up_card2}.")
    
    #Removing cards from each player's deck#
    player.deck = player.deck[4:]
    opponent.deck = opponent.deck[4:]

    #Comparing face up cards#
    card1_value = card_values[face_up_card1.split(" ")[0]]
    card2_value = card_values[face_up_card2.split(" ")[0]]

    if card1_value > card2_value:
        print(f"{player.player_name} wins the war!\n")
        player.deck.extend(face_down_cards1 + face_down_cards2 + [face_up_card1, face_up_card2])
    elif card1_value < card2_value:
        print(f"{opponent.opponent_name} wins the war!\n")
        opponent.deck.extend(face_down_cards1 + face_down_cards2 + [face_up_card1, face_up_card2])
    else:
        print("Another war!\n")
        player.deck, opponent.deck = handle_war(player, opponent)
    
    return player.deck, opponent.deck

# Running the game #
print("Welcome to WarPython! The game where you can play the War card game right in your Python terminal!")
print("Please input your name, and press Enter.")
player = Player(input())
print("Name your opponent, and press Enter.")
opponent = Opponent(input())
print("Alright, let's go to War!")
war_loop(player, opponent)
    



