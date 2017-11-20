
#https://github.com/peterbrittain/asciimatics
# https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text
import sys
import os
from randomwords import randomWord
from time import sleep
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
hangmanVisual0 = '''

            -----------
            |         |   
            |         |   
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |    
                      |
                      |   
                      | 
    ______________________
'''

hangmanVisual1 = '''

            -----------
            |         |   
            |         |   
           ...        |
          .o o.       |
          . _ .       |
           ...        |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |    
                      |
                      |   
                      | 
    ______________________
'''

hangmanVisual2 = '''

            -----------
            |         |   
            |         |   
           ...        |
          .o o.       |
          . _ .       |
           ...        |
            |         |
            |         |
            |         |
            |         |
            |         |
            |         |
                      |
                      |    
                      |
                      |   
                      | 
    ______________________
'''

hangmanVisual3 = '''

            -----------
            |         |   
            |         |   
           ...        |
          .o o.       |
          . _ .       |
           ...        |
         \  |         |
          \ |         |
           \|         |
            |         |
            |         |
            |         |
                      |
                      |    
                      |
                      |   
                      | 
    ______________________
'''

hangmanVisual4 = '''

            -----------
            |         |   
            |         |   
           ...        |
          .o o.       |
          . _ .       |
           ...        |
         \  |  /      |
          \ | /       |
           \|/        |
            |         |
            |         |
            |         |
                      |
                      |    
                      |
                      |   
                      | 
    ______________________
'''

hangmanVisual5 = '''

            -----------
            |         |   
            |         |   
           ...        |
          .o o.       |
          . _ .       |
           ...        |
         \  |  /      |
          \ | /       |
           \|/        |
            |         |
            |         |
            |         |
           /          |
          /           |    
         /            |
    ______________________
'''

hangmanVisual6 = '''

            -----------
            |         |   
            |         |   
           ...        |
          .o o.       |
          . _ .       |
           ...        |
         \  |  /      |
          \ | /       |
           \|/        |
            |         |
            |         |
            |         |
           / \        |
          /   \       |    
    ____ /_____\______|
'''

hangmanVisual7 = '''

            -----------
            |         |   
            |         |
            |         |   
           ...        |
          .x x.       |
          . _ .       |
           ...        |
         \  |  /      |
          \ | /       |
           \|/        |
            |         |
            |         |
            |         |
           / \        |
          /   \       |    
    ____ /     \ _____|
                /     
               /
              /
             / 
'''

hangmanVisualTrash = ''' 




     ___________.._______
    | .__________))______|
    | | / /      ||
    | |/ /       ||
    | | /        ||.-''.
    | |/         |/  _  \
    | |          ||  `/,|
    | |          (\\`_.'
    | |         .-`--'.
    | |        /Y . . Y\
    | |       // |   | \\
    | |      //  | . |  \\
    | |     ')   |   |   (`
    | |          ||'||
    | |          || ||
    | |          || ||
    | |          || ||
    | |         / | | \
    """"""""""|_`-' `-' |"""|
    |"|"""""""\ \       '"|"|
    | |        \ \        | |
    : :         \ \       : :  sk
    . .          `'       . .


'''
'''
   ...
  .o o.
  . _ .   
   ...
 \  |  /
  \ | /
   \|/
    |
    |
    |
   / \
  /   \
 /     \
'''

'''
   ...
  .x x.
  . _ .   
   ...
 \  |  /
  \ | /
   \|/
    |
    |
    |
   / \
  /   \
 /     \
'''
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def main():		

	os.system('printf "\033c"')
	print('''
	Hello and Welcome to 
	''')
	cprint(figlet_format('HANGMAN', font='slant'),'yellow', 'on_red', attrs=['bold'])
	print('''
Please select one of the following:

	1. PLAY
	2. Instructions
	3. Exit

	''')

	selection = input('Selection: ')
	if selection == str(1):
		os.system('printf "\033c"')		
		win,hangmanword,diffucultyValue = inputDifficulty()
		gameOver(hangmanword)
	elif selection == str(2):
		pass
	elif selection == str(3):
		os.system('printf "\033c"')
		print(bcolors.OKGREEN + 'Thanks for playing HANGMAN. Have a nice day.'+bcolors.ENDC)
		quit()
	else:
		main()



def inputDifficulty():
	print('''
How hard do you want the game to be?

'''+bcolors.OKGREEN+'''    1. Easy (Word length < 6)'''+bcolors.ENDC+'''
'''+bcolors.WARNING+'''    2. Medium (Word length 6 - 10)'''+bcolors.ENDC+'''
'''+bcolors.FAIL+'''    3. Hard (Word Length > 10)'''+bcolors.ENDC+'''

''')
	
	selection = input('Difficulty: ')
	if selection == str(1):
		win,hangmanword = playGameFunc(0,5)
		return(win,hangmanword,1)
	elif selection == str(2):
		win,hangmanword = playGameFunc(6,10)
		return(win,hangmanword,2)		
	elif selection == str(3):
		win,hangmanword= playGameFunc(11,100)
		return(win,hangmanword,3)		
	else:
		inputDifficulty()
		
		
		
		
def playGameFunc(lower,upper):
	hangmanWord = randomWord(lower,upper).title()
	rightGuessList = []
	wrongGuessList = []
	error = 0
	gamePlay = 1
	wordView = []
	for letter in hangmanWord:
		wordView.append('_')
	hangmanVisuals = [hangmanVisual0,hangmanVisual1,hangmanVisual2,hangmanVisual3,hangmanVisual4,hangmanVisual5,hangmanVisual6,hangmanVisual7]
	hangmanVisualValue = 0
	while gamePlay == 1:
		#FIND THE LETTERS AVAILABLE###
		for x in range(0,len(hangmanWord)):
			for y in range(0,len(rightGuessList)):
				if rightGuessList[y] == hangmanWord[x].upper():
					wordView[x] = hangmanWord[x]
		
		whileloop = 1
		while whileloop == 1:	
			os.system('printf "\033c"')
			print(hangmanVisuals[hangmanVisualValue])
			print('    The word is: '+bcolors.OKGREEN+' '.join(wordView)+bcolors.ENDC)
			print('   ',wrongGuessList)
			print()
			print()
			
			if '_' not in wordView:
				return(1,hangmanWord)
			if error >=7:
				return(0,hangmanWord)	
			
			
			hangmanGuess = input("What will be your guess?: ")
			if hangmanGuess.isalpha():
				whileloop = 0
				if (hangmanGuess.upper() not in wrongGuessList) and (hangmanGuess.upper() not in rightGuessList) and (len(hangmanGuess) == 1):
					if hangmanGuess.upper() in hangmanWord.upper():
						rightGuessList.append(hangmanGuess.upper())

							
					else:
						wrongGuessList.append(hangmanGuess.upper())
						hangmanVisualValue += 1
						error += 1
	
	

def gameOver(hangmanWord):	
	for x in range(1,60):
		os.system('printf "\033c"')
		print('GAME OVER')
		print(bcolors.FAIL+hangmanVisual7+bcolors.ENDC)
		print('The word was: '+hangmanWord)
		sleep(0.1)
		os.system('printf "\033c"')
		print('GAME OVER')
		sleep(0.05)	
		
		
main()		
		