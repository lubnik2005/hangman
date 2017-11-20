
# https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text
import sys
import os
from randomwords import randomWord
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
                      |   
                      | 
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
         /     \      |
                      |   
                      | 
    ______________________
'''

hangmanVisual7 = '''

            -----------
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
         /     \      |
                      |   
                      | 
    ______________________
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
Hello and Welcome to '''+bcolors.BOLD + '''HANGMAN''' + bcolors.ENDC+'''
Please select one of the following:

	1. PLAY
	2. Instructions
	3. Exit

	''')

	selection = input('Selection: ')
	if selection == str(1):
		os.system('printf "\033c"')		
		inputDifficulty()
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

    1. Easy (Word length < 6)
    2. Medium (Word length 6 - 10)
    3. Hard (Word Length > 10)
	''')
	
	selection = input('Difficulty: ')
	if selection == str(1):
		playGameFunc(0,5)
	elif selection == str(2):
		playGameFunc(6,10)
	elif selection == str(3):
		playGameFunc(11,100)
	else:
		inputDifficulty()
		

def playGameFunc(lower,upper):
	hangmanWord = randomWord(lower,upper)
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
				if rightGuessList[y].lower() == hangmanWord[x].lower():
					wordView[x] = hangmanWord[x]
			
		
		os.system('printf "\033c"')
		print(hangmanVisuals[hangmanVisualValue])
		print('    The word is: '+' '.join(wordView))
		print('   ',wrongGuessList)
		print()
		print()
		hangmanGuess = input("What will be your guess?: ")

		if hangmanGuess.isalpha and hangmanGuess not in wrongGuessList and hangmanGuess not in rightGuessList:
			if hangmanGuess in hangmanWord:
				rightGuessList.append(hangmanGuess.upper())
			else:
				wrongGuessList.append(hangmanGuess.upper())
				hangmanVisualValue += 1
				error += 1
			############################################################################ BEING DUMB #################################		
			for x in range(0,len(hangmanWord)):
				for y in range(0,len(rightGuessList)):
					if rightGuessList[y].lower() == hangmanWord[x].lower():
						wordView[x] = hangmanWord[x]
			os.system('printf "\033c"')
			print(hangmanVisuals[hangmanVisualValue])
			print('    The word is: '+' '.join(wordView))
			print('   ',wrongGuessList)
			print()
			print()
			print("What is your guess?: "+ str(hangmanGuess))
			if hangmanGuess in hangmanWord:
				input('YES, YOU GOT IT!!')
				rightGuessList.append(hangmanGuess)
			else:
				input("NOO! HELP THE HANGMAN SO HE DOESN't DIE!!")

			
			############################################################################ BEING DUMB #################################		


		if error == 7:
			input('So sorry, you lost!! The word was: ' + bcolors.WARNING+hangmanWord.title()+bcolors.ENDC)		
		if '_' not in wordView:
			input('YOU WIN!!!!')
		main()	


	

main()


