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
        round_done = False
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
            round_done = True
        elif card1_value < card2_value:
            print(f"{opponent.opponent_name} wins this round!\n")
            opponent.deck.extend([card1, card2])
            round_done = True
        else:
            print("War!\n")
            player.deck, opponent.deck = handle_war(player, opponent)
            round_done = True

        if player.deck and opponent.deck and round_done:
            print("\n""The round has concluded. Would you like to play another round? Y/N")
            user_input = input().strip().upper()
            if user_input == "Y":
                round_done = False
            elif user_input == "N":
                print("Thanks for playing!")
                break
            else:
                print("Please input a valid input.")
        
        
        #If player or opponent runs out of cards, win condition#
        if not player.deck and round_done:
            print(f"{player.player_name} has run out of cards. {opponent.opponent_name} wins the game!")
            break
        elif not opponent.deck and round_done:
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
print("\nWelcome to WarPython! The game where you can play the War card game right in your Python terminal!")
print("\nWar is a two-player card game where the objective is to win all the cards. The deck is shuffled and split evenly between the players, who simultaneously reveal the top card of their decks. The player with the higher card wins both cards and adds them to the bottom of their deck, with cards ranked from 2 (lowest) to Ace (highest). If the cards are of equal value, a \"war\" occurs: each player places three cards face down and one card face up. The player with the higher face-up card wins all the cards played during the war. If these cards are also equal, the process repeats. The game continues until one player has all the cards, winning the game.")
print("\nPlease input your name, and press Enter.")
player = Player(input())
print("Name your opponent, and press Enter.")
opponent = Opponent(input())
print("Alright, let's go to War!")
war_loop(player, opponent)
    
