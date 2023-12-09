"""
Unum: a cli clone of Uno (Classic ver., 108 cards)
{license info}
"""

# Generic Imports
import random

# Global Variables
  # Player names
p1_name = ""
p2_name = ""

  # Player hands
p1_hand = []
p2_hand = []
  # Deck info
cards_in_deck = 108
card_colors = ["red", "yellow", "blue", "green"]
wild_cards_in_deck = 8
current_discard_color = ""


# Classes
class card():
  number = ""
  color = ""
  skip = False
  reverse = False
  draw_2 = False
  wild_draw_4 = False
  wild = False
  shuffle_hands_card = False

  def __init__(self, number, color, skip, reverse, draw_2, wild_draw_4, wild,
               shuffle_hands_card):
    self.number = number
    self.color = color
    self.skip = skip
    self.reverse = reverse
    self.draw_2 = draw_2
    self.wild_draw_4 = wild_draw_4
    self.wild = wild
    self.shuffle_hands_card = shuffle_hands_card


# Cards
  # Reds
red_zero = card(0, "Red", False, False, False, False, False, False)
red_one_one = card(1, "Red", False, False, False, False, False, False)
red_one_two = card(1, "Red", False, False, False, False, False, False)
red_two_one = card(2, "Red", False, False, False, False, False, False)
red_two_two = card(2, "Red", False, False, False, False, False, False)
red_three_one = card(3, "Red", False, False, False, False, False, False)
red_three_two = card(3, "Red", False, False, False, False, False, False)
red_four_one = card(4, "Red", False, False, False, False, False, False)
red_four_two = card(4, "Red", False, False, False, False, False, False)
red_five_one = card(5, "Red", False, False, False, False, False, False)
red_five_two = card(5, "Red", False, False, False, False, False, False)
red_six_one = card(6, "Red", False, False, False, False, False, False)
red_six_two = card(6, "Red", False, False, False, False, False, False)
red_seven_one = card(7, "Red", False, False, False, False, False, False)
red_seven_two = card(7, "Red", False, False, False, False, False, False)
red_eight_one = card(8, "Red", False, False, False, False, False, False)
red_eight_two = card(8, "Red", False, False, False, False, False, False)
red_nine_one = card(9, "Red", False, False, False, False, False, False)
red_nine_two = card(9, "Red", False, False, False, False, False, False)
red_skip_one = card(False, "Red", True, False, False, False, False, False)
red_skip_two = card(False, "Red", True, False, False, False, False, False)
  # Yellows
yellow_zero = card(0, "Yellow", False, False, False, False, False, False)
yellow_one_one = card(1, "Yellow", False, False, False, False, False, False)
yellow_one_two = card(1, "Yellow", False, False, False, False, False, False)
yellow_two_one = card(2, "Yellow", False, False, False, False, False, False)
yellow_two_two = card(2, "Yellow", False, False, False, False, False, False)
yellow_three_one = card(3, "Yellow", False, False, False, False, False, False)
yellow_three_two = card(3, "Yellow", False, False, False, False, False, False)
yellow_four_one = card(4, "Yellow", False, False, False, False, False, False)
yellow_four_two = card(4, "Yellow", False, False, False, False, False, False)
yellow_five_one = card(5, "Yellow", False, False, False, False, False, False)
yellow_five_two = card(5, "Yellow", False, False, False, False, False, False)
yellow_six_one = card(6, "Yellow", False, False, False, False, False, False)
yellow_six_two = card(6, "Yellow", False, False, False, False, False, False)
yellow_seven_one = card(7, "Yellow", False, False, False, False, False, False)
yellow_seven_two = card(7, "Yellow", False, False, False, False, False, False)
yellow_eight_one = card(8, "Yellow", False, False, False, False, False, False)
yellow_eight_two = card(8, "Yellow", False, False, False, False, False, False)
yellow_nine_one = card(9, "Yellow", False, False, False, False, False, False)
yellow_nine_two = card(9, "Yellow", False, False, False, False, False, False)
yellow_skip_one = card(False, "Yellow", True, False, False, False, False, False)
yellow_skip_two = card(False, "Yellow", True, False, False, False, False, False)
  # Blues
blue_zero = card(0, "Blue", False, False, False, False, False, False)
blue_one_one = card(1, "Blue", False, False, False, False, False, False)
blue_one_two = card(1, "Blue", False, False, False, False, False, False)
blue_two_one = card(2, "Blue", False, False, False, False, False, False)
blue_two_two = card(2, "Blue", False, False, False, False, False, False)
blue_three_one = card(3, "Blue", False, False, False, False, False, False)
blue_three_two = card(3, "Blue", False, False, False, False, False, False)
blue_four_one = card(4, "Blue", False, False, False, False, False, False)
blue_four_two = card(4, "Blue", False, False, False, False, False, False)
blue_five_one = card(5, "Blue", False, False, False, False, False, False)
blue_five_two = card(5, "Blue", False, False, False, False, False, False)
blue_six_one = card(6, "Blue", False, False, False, False, False, False)
blue_six_two = card(6, "Blue", False, False, False, False, False, False)
blue_seven_one = card(7, "Blue", False, False, False, False, False, False)
blue_seven_two = card(7, "Blue", False, False, False, False, False, False)
blue_eight_one = card(8, "Blue", False, False, False, False, False, False)
blue_eight_two = card(8, "Blue", False, False, False, False, False, False)
blue_nine_one = card(9, "Blue", False, False, False, False, False, False)
blue_nine_two = card(9, "Blue", False, False, False, False, False, False)
blue_skip_one = card(False, "Blue", True, False, False, False, False, False)
blue_skip_two = card(False, "Blue", True, False, False, False, False, False)
  # Greens
green_zero = card(0, "Green", False, False, False, False, False, False)
green_one_one = card(1, "Green", False, False, False, False, False, False)
green_one_two = card(1, "Green", False, False, False, False, False, False)
green_two_one = card(2, "Green", False, False, False, False, False, False)
green_two_two = card(2, "Green", False, False, False, False, False, False)
green_three_one = card(3, "Green", False, False, False, False, False, False)
green_three_two = card(3, "Green", False, False, False, False, False, False)
green_four_one = card(4, "Green", False, False, False, False, False, False)
green_four_two = card(4, "Green", False, False, False, False, False, False)
green_five_one = card(5, "Green", False, False, False, False, False, False)
green_five_two = card(5, "Green", False, False, False, False, False, False)
green_six_one = card(6, "Green", False, False, False, False, False, False)
green_six_two = card(6, "Green", False, False, False, False, False, False)
green_seven_one = card(7, "Green", False, False, False, False, False, False)
green_seven_two = card(7, "Green", False, False, False, False, False, False)
green_eight_one = card(8, "Green", False, False, False, False, False, False)
green_eight_two = card(8, "Green", False, False, False, False, False, False)
green_nine_one = card(9, "Green", False, False, False, False, False, False)
green_nine_two = card(9, "Green", False, False, False, False, False, False)
green_skip_one = card(False, "Green", True, False, False, False, False, False)
green_skip_two = card(False, "Green", True, False, False, False, False, False)
  # Wild
wild_draw_4 = card(False, "Draw 4", False, False, True, False, False, False)
wild = card(False, "Wild Card", False, False, False, False, True, False)
shuffle_hands_card = card(False, "Shuffle Hands", False, False, False, False,False, True)

# Functions
def print_logo():
  print("U   U  NN  N  U   U  M    M")
  print("U   U  N N N  U   U  MM  MM")
  print("U   U  N  NN  U   U  M MM M")
  print("UUUUU  N   N  UUUUU  M    M")


def draw_card_p1():
  global p1_hand
  color_draw = random.randint(1, 5)              #
  if color_draw == 1:
    red_card_draw = random.randint(0, 9)          #
  elif color_draw == 2:
    blue_card_draw = random.randint(0, 9)        #
    yellow_card_draw = random.randint(0, 9)
  elif color_draw == 3:                        #   FINISH THIS FUNCTION, THEN C&P INTO draw_card_p2()!!!!
    blue_card_draw = random.randint(0, 9)
  elif color_draw == 4:                        #
    green_card_draw = random.randint(0, 9)
  elif color_draw == 5:                        #
    wild_card_draw = random.randint(1, 3)
    if wild_card_draw == 1:
      p1_hand.append(wild_draw_4)              #


def drop_card():
  pass  # add code here that will drop a card from your hand, check if move is legal


def shuffle_hands():
  pass  # add code that will do the "shuffle hands" thing


def new_game():
  global p1_name
  global p2_name
  global p1_hand
  global p2_hand
  p1_name = input("What is player 1's name?")
  p2_name = input("What is player 2's name?")
  p1_hand = []
  p2_hand = []

def remake_deck():
  pass  # add code that will remake the deck if the deck is empty


# Main Code
