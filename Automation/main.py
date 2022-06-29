# Let's Automate Some Stuff
import pyautogui
pyautogui.screenshot('c:\\screenshot_example.png')



def main_menu(): 
  print('''What would you like to automate?: 
  
  1. 3CX
  2. ???
  3. ???''')
  choice = input('\nEnter Number Here: ')
  if choice == '1':
   print('\nTotally tublular!')
   # DEX 1 - this 'my_name()' would have be calling twice once below and once in game_start_conf(). Moved to game_start_conf() only
   #my_name()
   #game_start_conf()
  while choice == '2':
   print('\nNo options available. Check back later.')
   print()
   #main_menu()
  if choice == '3':
   print('\nThis will eventually be sys exit. Check back later.')
   print()
   main_menu()

