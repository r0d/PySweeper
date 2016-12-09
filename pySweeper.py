#*********************************************#
# Name: Nicolas Rodriguez  
# Date: 21 NOV 16
#*********************************************#

import msvcrt
import random 
import math
import os

bombLine = random.randint(0,19)
bombChar = random.randint(0,39)
line = []

#*****************************************************************#
#FUNCTION NAME      : createBoard
#FUNCTION INPUT(s)  : none
#FUNCTIONS IT CALLS : none
#WHAT IT RETURNS    : nothing, it adds 20 items of 40 dots to the varaible list
#HOW TO CALL IT     :
#>>> createBoard()
#>>> 
#*****************************************************************#
def createBoard():
  for x in range(1,21):
    line.append(list("........................................"))

#*****************************************************************#
#FUNCTION NAME      : showBoard
#FUNCTION INPUT(s)  : charNumber, lineNumber
#FUNCTIONS IT CALLS : print(), math.sqrt()
#WHAT IT RETURNS    : nothing, prints out the variable list with each item as its own row, calculates distacne to bomb, and prints out formatting
#HOW TO CALL IT     :
#>>> showBoard(charNumber, lineNumber)
#>>> 
#*****************************************************************#

def showBoard(charNumber, lineNumber):
	os.system('cls')
	print('Welcome to PySweeper 1.0! Use WASD to move around the board! Press q to quit.')
	print('_________________________________________________________')
	for x in range(0,20):
		currentRow = line[x]
		allRows = ''
		for y in range(0,40):
			allRows += currentRow[y]
		print(allRows)
	bombDistance = int(math.sqrt(((bombChar-charNumber)**2)+((bombLine-lineNumber)**2)))
	print("Distance to bomb: " + str(bombDistance))
	print('_________________________________________________________')

#*****************************************************************#
#FUNCTION NAME      : bombByte
#FUNCTION INPUT(s)  : none
#FUNCTIONS IT CALLS : print()
#WHAT IT RETURNS    : prints out a bomb when the user loses
#HOW TO CALL IT     :
#>>> bombByte()
#>>> 
#*****************************************************************#

def bombByte():
	os.system('cls')
	print(".................\|/...................")                         
	print("...............`--+--'.................")                        
	print("................./|\...................")                          
	print("................' | '..................")                                                    
	print("..................|....................")                           
	print("..............,--'#`--.................")                       
	print("..............|#######|................")                       
	print("..........._.-'#######`-._.............")                    
	print("........,-'###############`-...........")                 
	print("......,'#####################`,........")               
	print("...../#########################\.......")              
	print("....|###########################|......")             
	print("...|#############################|.....")            
	print("...|#############################|.....")       
	print("...|#############################|.....")        
	print("...|#############################|.....")       
	print("....|###########################|......")             
	print(".....\#########################/.......")              
	print("......`.#####################,'........")               
	print("........`._###############_,'..........")                 
	print("...........`--..#####..--'.............")
	print("BOOM! You hit a bomb, you lose!")
	print("GAME OVER")

#*****************************************************************#
#FUNCTION NAME      : winByte
#FUNCTION INPUT(s)  : none
#FUNCTIONS IT CALLS : print()
#WHAT IT RETURNS    : prints out an american flag when the user wins
#HOW TO CALL IT     :
#>>> bombByte()
#>>> 
#*****************************************************************#
def winByte():
	os.system('cls')
	print("|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("| * * * * * * * * *  OOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("| * * * * * * * * *  OOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("| * * * * * * * * *  OOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|")
	print("|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|")
	print('')
	print('YOU WIN!!!!!!!!!!!!!')
	print('You are now qualified to branch EOD!')
	print("'Merica, fuck yeah!")

#*****************************************************************#
#FUNCTION NAME      : editBoard
#FUNCTION INPUT(s)  : none
#FUNCTIONS IT CALLS : msvcrt.getwch(), math.sqrt(), print()
#WHAT IT RETURNS    : nothing, it displays the new board after making a change based on the key the user presses
#HOW TO CALL IT     :
#>>> editBoard()
#>>> 
#*****************************************************************#   
    
def editBoard():
	total = 0
	x = 0
	lineNumber = 0
	charNumber = 0
	while x != 1:
		char = msvcrt.getwch()
		if char == 's':
			lineNumber += 1
			if lineNumber == bombLine and charNumber == bombChar:
				bombByte()
				break
			elif lineNumber < 0 or lineNumber > 19:
				lineNumber -=1
			else:  
				currentLine = line[lineNumber]
				if currentLine[charNumber] == '#':
					currentLine[charNumber] = '.'
					total -=1
				else:
					currentLine[charNumber] = '#'
					total +=1
			if total != 799:
				showBoard(charNumber, lineNumber)
			else:
				showBoard(charNumber, lineNumber)
				winByte()
				break
		elif char == 'w':
			lineNumber -= 1
			if lineNumber == bombLine and charNumber == bombChar:
				bombByte()
				break
			elif lineNumber < 0 or lineNumber > 19:
				lineNumber +=1
			else:  
				currentLine = line[lineNumber]
				if currentLine[charNumber] == '#':
					currentLine[charNumber] = '.'
					total -=1
				else:
					currentLine[charNumber] = '#'
					total +=1
			if total != 799:
				showBoard(charNumber, lineNumber)
			else:
				showBoard(charNumber, lineNumber)
				winByte()
				break
		elif char == 'a':
			charNumber -= 1
			if lineNumber == bombLine and charNumber == bombChar:
				bombByte()
				break
			elif charNumber < 0 or charNumber > 39:
				charNumber += 1
			else:  
				currentLine = line[lineNumber]
				if currentLine[charNumber] == '#':
					currentLine[charNumber] = '.'
					total -=1
				else:
					currentLine[charNumber] = '#'
					total +=1
			if total != 799:
				showBoard(charNumber, lineNumber)
			else:
				showBoard(charNumber, lineNumber)
				winByte()
				break
				x += 1
		elif char == 'd':
			charNumber += 1
			if lineNumber == bombLine and charNumber == bombChar:
				bombByte()
				break    
			elif charNumber < 0 or charNumber > 39:
				charNumber -= 1
			else:  
				currentLine = line[lineNumber]
				if currentLine[charNumber] == '#':
					currentLine[charNumber] = '.'
					total -=1
				else:
					currentLine[charNumber] = '#'
					total +=1
			if total != 799:
				showBoard(charNumber, lineNumber)
			else:
				showBoard(charNumber, lineNumber)
				winByte()
				break
		elif char == 'q':
			x += 1
		else:
			print("Not a vaild character, try again!")
   
createBoard()
showBoard(0, 0)
editBoard()


   