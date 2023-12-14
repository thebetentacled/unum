"""
Unum: a cli clone of Uno
{license info}
"""

# Generic Imports
import random

# Global Variables
p1_name = ""
p2_name = ""
deck = []
discard = []
discard_color = "r"
prev_card = ""

# Player hands
p1_hand = []
p2_hand = []


# Functions
def shuffle_hands():
  global p1_hand, p2_hand
  temp_hand = []
  temp_hand.extend(p1_hand)
  temp_hand.extend(p2_hand)
  random.shuffle(temp_hand)
  th_length = len(temp_hand)
  th_middle = th_length // 2
  p1_hand = temp_hand[:th_middle]
  p2_hand = temp_hand[th_middle:]


def remake_deck():
  global deck, discard
  deck.extend(discard)
  random.shuffle(deck)


def make_deck():
  global deck
  deck = []
  for n in range(1, 15):
    for c in "rby":
      deck.append(str(n) + " " + c)
  deck.append("S r")
  deck.append("S b")
  deck.append("S y")
  random.shuffle(deck)


def start_game():
  global p1_hand, p2_hand, p1_name, p2_name, deck, discard, discard_color
  discard = []
  dc_options = ["r", "b", "y"]
  discard_color = dc_options[random.randint(0, 2)]
  make_deck()
  repeat = 7
  while repeat > 1:
    draw_card_p1()
    draw_card_p2()
    repeat = repeat - 1
  p1_name = input("What is Player 1's name? \n  -> ")
  p2_name = input("What is Player 2's name? \n  -> ")
  turns()


def turns():
  global p1_hand, p2_hand, p1_name, p2_name

  def p1_turn():
    print(" ***P1 Turn*** ")
    print("What would you like to do? (See Hand, Draw, or Drop")
    print("(Make sure you type the option EXACTLY as it is shown here.)")
    p1_turn_in = input("  -> ")
    if p1_turn_in == "See Hand":
      print(p1_hand)
      p1_turn()
    elif p1_turn_in == "Draw":
      draw_card_p1()
      print("You drew [" + p1_hand[-1] + "]")
      p1_turn()
    elif p1_turn_in == "Drop":
      drop_card_p1()
      p2_turn()
    else:
      print("Invalid.")
      p1_turn()

  def p2_turn():
    print(" ***P2 Turn*** ")
    print("What would you like to do? (See Hand, Draw, or Drop)")
    print("(Make sure you type the option EXACTLY as it is shown here.)")
    p2_turn_in = input("  -> ")
    if p2_turn_in == "See Hand":
      print(p2_hand)
      p2_turn()
    elif p2_turn_in == "Draw":
      draw_card_p2()
      p2_turn()
    elif p2_turn_in == "Drop":
      drop_card_p2()
      p1_turn()
    else:
      print("Invalid.")

  p1_turn()


def print_logo():
  print("U   U  NN  N  U   U  M    M   |‾‾‾‾‾|")
  print("U   U  N N N  U   U  MM  MM   | 14r |")
  print("U   U  N  NN  U   U  M MM M   |     |")
  print("UUUUU  N   N  UUUUU  M    M   |_____|")


def draw_card_p1():
  global deck, p1_hand
  p1_hand.append(deck[0])
  deck.remove(deck[0])


def draw_card_p2():
  global deck, p2_hand
  p2_hand.append(deck[0])
  deck.remove(deck[0])


def drop_card_p1():
  global discard_color, discard, p1_hand, prev_card
  pc_info = prev_card.split(" ", 1)
  card_to_drop = ""
  print("The last card that was dropped was: " + str(prev_card))
  print("The current discard color is [" + discard_color + "]")
  print("Drop what card?" + "(", p1_hand, ")")
  print("(Make sure you type the card EXACTLY as it is shown here.)")
  card_to_drop = input("  -> ")
  ctd_info = card_to_drop.split(" ", 1)
  if str(card_to_drop) not in p1_hand and not "Draw":
    print("Invalid. Select a card from your hand!")
  elif str(ctd_info[-1]) is not str(discard_color) and str(ctd_info[0]) is not str(pc_info[0]):
    print("This card doesn't match the discard color. Draw a card?")
    print("(Any answer besides \"y\" will be considered \"n\")")
    dc_draw_input = input("  -> ")
    if dc_draw_input == "y":
      draw_card_p1()
      drop_card_p1()
    else:
      drop_card_p1()
  else:
    if card_to_drop in ["S r", "S b", "S y"]:
      discard.append(str(card_to_drop))
      p1_hand.remove(str(card_to_drop))
      shuffle_hands()
      shuffle_hands()
      prev_card = card_to_drop
    elif ctd_info[0] == pc_info[0]:
      discard_color = ctd_info[1]
      discard.append(str(card_to_drop))
      p1_hand.remove(str(card_to_drop))
      prev_card = card_to_drop
    else:
      discard.append(str(card_to_drop))
      p1_hand.remove(str(card_to_drop))
      prev_card = card_to_drop

def drop_card_p2():
  global discard_color, discard, p2_hand, prev_card
  pc_info = prev_card.split(" ", 1)
  card_to_drop = ""
  print("The last card that was dropped was: " + str(prev_card))
  print("The current discard color is [" + discard_color + "]")
  print("Drop what card?" + "(", p2_hand, ")")
  print("(Make sure you type the card EXACTLY as it is shown here.)")
  print("If you have no card that matches the discard color, answer with \"Draw\"")
  card_to_drop = input("  -> ")
  ctd_info = card_to_drop.split(" ", 1)
  if str(card_to_drop) not in p2_hand and not "Draw":
    print("Invalid. Select a card from your hand!")
  elif str(ctd_info[-1]) is not str(discard_color) and str(ctd_info[0]) is not str(pc_info[0]):
    print("This card doesn't match the discard color. Draw a card?")
    print("(Any answer besides \"y\" will be considered \"n\")")
    dc_draw_input = input("  -> ")
    if dc_draw_input == "y":
      draw_card_p2()
      drop_card_p2()
    else:
      drop_card_p2()
  else:
    if card_to_drop in ["S r", "S b", "S y"]:
      discard.append(str(card_to_drop))
      p2_hand.remove(str(card_to_drop))
      prev_card = card_to_drop
      shuffle_hands()
    elif ctd_info[0] == pc_info[0]:
      discard_color = ctd_info[1]
      discard.append(str(card_to_drop))
      p2_hand.remove(str(card_to_drop))
      prev_card = card_to_drop
    else:
      discard.append(str(card_to_drop))
      p2_hand.remove(str(card_to_drop))
      prev_card = card_to_drop

# Main Code
start_game()
