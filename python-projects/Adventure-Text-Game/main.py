# This program is a text based adventure game

# Decko's Tip: You just need to figure out which variables you want to set as global (accessible throughout the runtime of the game) and define them underneath player_name. So like you may have 'player_role' as another global variable for instance.


# Main menu options
def main_menu(): 
  print('''Welcome to another text adventure game!
  \nEnter the number for where you want to go:
  1. Start
  2. Options
  3. Exit''')
  choice = input('\nEnter Number Here: ')
  if choice == '1':
   print('\nTotally tublular!')
   # DEX 1 - this 'my_name()' would have be calling twice once below and once in game_start_conf(). Moved to game_start_conf() only
   #my_name()
   game_start_conf()
  while choice == '2':
   print('\nNo options available. Check back later.')
   print()
   main_menu()
  if choice == '3':
   print('\nThis will eventually be sys exit. Check back later.')
   print()
   main_menu()

# this is the global player_name variable that is waiting to be set
player_name = ''

def my_name():
  return input('\nTell me adventurer, what is your name?: ').capitalize()
  #DEX was missing parenthesis () on capitalize function
  
# Game start confirmation screen
def game_start_conf(): 
  # DEX 2 - setting player_name variable to return value of my_name() input
  player_name = my_name()

  # DEX 3 - when referring to player name from here on in if/else statements use 'player_name'
  name_conf = input('\nHello ' + player_name + ', it\'s nice to meet you. Are you ready to embark on an adventure? ').capitalize()
  if name_conf == 'Yes':
   game_start()
  elif name_conf == 'No':
   print('\nThat\'s a shame, perhaps next time. Returning to Main Menu.')
   main_menu()
  else:
    print('\nPlease type "Yes" or "No".')

def game_start():
 print('\nWe haven\'t coded this far yet, returning to main menu.')
 print('')
 main_menu()

# Step One
main_menu()
# Step Two

#Step Three