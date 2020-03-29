# Starter Code
# Simulation game of traveling out west in 1800's

import random

welcome_text = """
Welcome to the Oregon Trail! The year is 1850 and Americans are
headed out West to populate the frontier. Your goal is to travel
by wagon train from Independence, MO to Oregon (2000 miles). You start on March 1st, and your goal is to reach Oregon by December 31st.
The trail is arduous. Each day costs you food and health. You
can hunt and rest, but you have to get there before winter!
"""

help_text = """
Each turn you can take one of 3 actions:

  travel - moves you randomly between 30-60 miles and takes
           3-7 days (random).
  rest   - increases health 1 level (up to 5 maximum) and takes
           2-5 days (random).
  hunt   - adds 100 lbs of food and takes 2-5 days (random).

When prompted for an action, you can also enter one of these
commands without using up your turn:

  status - lists food, health, distance traveled, and day.
  help   - lists all the commands.
  quit   - will end the game.
  
You can also use these shortcuts for commands:

  't', 'r', 'h', 's', '?', 'q'
  
"""

good_luck_text = "Good luck, and see you in Oregon!"

# Model -- global variables that collectivel represent the state
# of the game
miles_traveled = 0
food_remaining = 500
health_level = 5
month = 3
day = 1
sicknesses_suffered_this_month = 0
player_name = None
first_sick_day = 1
second_sick_day = 2

# Constants -- parameters that define the rules of the game,
# but which don't change. An 'travel' action can take the player 
# between 30-60 miles, and take 3-7 days. Use the Random function with the min and max values below to determine what happens per turn/action taken. Notice the syntax on constants vs global variables- the lowercase versus all caps.   
MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7

# More constants! A 'rest' action increases health 1 level (up to 5 maximum that a player can have) and takes 2-5 days (random).
MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5

# More constants! A 'hunt' action adds 100 lbs of food and takes 2-5 days (random).
FOOD_PER_HUNT = 100
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5

# Constants to help you with gameplay. 
FOOD_EATEN_PER_DAY = 5
MILES_BETWEEN_MO_AND_OREGON = 2000
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]

NAME_OF_MONTH = [
    'fake', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December'
]

# Converts are numeric date into a string.
# input: m - a month in the range 1-12
# input: d - a day in the range 1-31
# output: a string like "December 24".
# Note: this function does not enforce calendar rules. It's happy to output
# impossible strings like "June 95" or "February 31".
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def date_as_string(m, d):
	# Enter your code here 
  	return 1
  
# Prints out how many miles are left. Player starts at 2000 and you should be updating how far they have traveled using 'miles_traveled' as gameplay continues.
# input: nothing
# output: a number that indicates how many miles are remaining. If there are no miles remaining, the game ends as the player has won!
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def miles_remaining():
	# Enter your code here
  	return 1

# Returns the number of days in the month (28, 30, or 31).
# input: an integer from 1 to 12. 1=January, 2=February, etc.
# output: the number of days in the month. If the input is not in
#   the required range, returns 0.
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def days_in_month(m):
	# Enter your code here
  	return 1
   
# Determines which (random) days of the month the player is going to get sick. 
# The expectation is that at the start of each new month, you want to run this function, and figure out two days during which a player is going to get sick. 
# You are going to need to call randint (1, DAYS_IN_MONTH) twice and make sure the second number is not the same as the first. You will also need to figure out the DAYS_IN_MONTH and generate
# the random integer between 1 and that. 
# Update first_sick_day and second_sick_day with the 2 random numbers generated.   
# input: nothing
# output: nothing

def sick_day_generator():
  	# Enter your code here
	return 1

# This function will tell you if sickness occurs on any given day. Whenever the user passes the days given by first_sick_day or second_sick_day, a sickness has occured. 
# This can happen during travel, rest, hunting etc. Make sure you update sicknesses_suffered_this_month by 1 if a sick day has passed. 
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def random_sickness_occurs():
	# Enter your code here
  	return 1

# This function should update the health of a player. If a random sickness occurs, health goes down by the same that you gain when you rest. 
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def handle_sickness():
	# Enter your code here
  	return 1

# A player's gotta eat every day. A player consumers FOOD_EATEN_PER_DAY every day. Remember, some actions take multiple days, so FOOD_EATEN_PER_DAY should be multiplied by that amount of days. 
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def consume_food():
	# Enter your code here
  	return 1

# Causes a certain number of days to elapse. The days pass one at a time, and each
# day brings with it a random chance of sickness. The sickness rules are quirky: player
# is guaranteed to fall ill a certain number of times each month, so illness
# needs to keep track of month changes. You will need to deal with month changes when the day becomes greater than days this month. 
# 
#
# input: num_days - an integer number of days that elapse.
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def add_day(num_days):
	# Enter your code here
  	return 1

# This is a handler for if a player selects 'travel' as an action. Think about what happens when 'travel' is selected and what other functions need to be called from this handler.
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def handle_travel():
	# Enter your code here
 	 return 1

# This is a handler for if a player selects 'rest' as an action. Think about what happens when 'rest' is selected and what other functions need to be called from this handler.
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def handle_rest():
	# Enter your code here
	return 1

# This is a handler for if a player selects 'hunt' as an action. Think about what happens when 'hunt' is selected and what other functions need to be called from this handler.
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def handle_hunt():
	# Enter your code here
	return 1

# This is a handler for if a player selects 'status' as an action. The player wants info and we're gonna give it to them! This function should print food, health, distance traveled, and day.
def handle_status():
	# Enter your code here
  	return 1

# This is handler for if a player selects 'help' as an action. Good thing we defined help_text at the start of this program...
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def handle_help():
	# Enter your code here
  	return 1

# This is a handler for if a player selects 'quit' as an action. This ends the game. Note that adding the word 'global' in front of a variable makes the variable global and usable outside of the context of the function.  

def handle_quit():
	global playing
	playing = False

# Sometimes players might enter gibberish or actions that we have not defined in our game. This is a handler to ask for another response if that is the case. 
def handle_invalid_input(response):
	print("'{0}' is not a valid command. Try again.".format(response))

# Ways a game can end are: player selects 'quit' (you should have handled this above in handle_quit()), or player's health_level gets to 0, or miles_traveled gets to 2000, or the player has been traveling past 12/31.
# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def game_is_over():
	# Enter your code here
  	return 1

# To help the code run while you update the code for the various functions, we added 'return 1'. Do not forget to edit this as you write this function.
def player_wins():
	# Enter your code here
  	return 1

# This is the main gameplay code. If you want, you can define and create a new select_action function to help with this part. We won't take marks off for no select_action being defined (even though it says to in the rubric).
print(welcome_text + help_text + good_luck_text)
player_name = input("\nWhat is your name, player?")

playing = True
handle_status()

while playing:
	print()
	action = input("Choose an action, {0} -->".format(player_name))
	if action == "travel" or action == "t":
		handle_travel()
	elif action == "rest" or action == "r":
		handle_rest()
	elif action == "hunt" or action == "h":
		handle_hunt()
	elif action == "quit" or action == "q":
		handle_quit()
	elif action == "help" or action == "?":
		handle_help()
	elif action == "status" or action == "s":
		handle_status()
	else:
		handle_invalid_input(action)

	if game_is_over():
		playing = False

if player_wins():
	print("\n\nCongratulations you made it to Oregon alive!")
	handle_status()
else:
	print("\n\nAlas! You lose.")
	handle_status()
