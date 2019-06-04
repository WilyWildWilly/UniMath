from os import system, name 
from random import randint
  
# import sleep to show output for some time period 
from time import sleep 
  
#################################
###FUNCTIONS FOR THE MAIN MENU###
#################################  
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        
################################
###FUNCTIONS FOR PRIME_FINDER###
################################  

def lLimit(lLim):
	lLim = int(lLim)
	if lLim < 1 :
		lLim = int(input("please insert an integer greater than 0 ! "))
	if lLim % 2 == 0:
		lLim = int(lLim) + 1
	return(int(lLim))

def hLimit(hLim):
	if int(hLim) <= lLim:
		hLim = int(input("the higher range limit must be greater than the lower one! "))
	hLim = int(hLim)
	return(int(hLim))

def scanner(lLim, hLim, primes):
	for i in range(lLim, hLim, 2):
		isPrime = True
		j = 3
		top = int(i ** 0.5)
		for j in range(3, top, 2):
			if i % j == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(i)
	return(primes)

################################
###FUNCTIONS FOR DICE_GUESSER###
################################  

def guesser():
	rnd = randint(1, 6)
	gss = input("Guess the outcome of the dice roll :")
	try:
		gss = int(gss)
	except:
		msg = "You must enter an integer. '{}' is not a \nvalid guess for a dice roll!".format(gss)
	finally:
		try:
			if gss >=1 and gss <= 6:
				if gss == rnd:
					msg = "Number {} wins! The result is {} !".format(gss, rnd)
				else:
					msg = "You guessed {} but the dice gave : {}".format(gss, rnd)
			else:
				msg = "Please type an integer between 1 and 6. \n'{}' is not a valid choice.".format(gss)
		finally:
			print("The guess is", gss, "and the dice says : ", rnd)
			return(msg)



text = """

	*******************************************************
	*	Choose one of the following functions :	      *
	*                                                     *	
	*	1. Primes finder                              *	
	*	2. Roll a dice                                *	
	*	3. Guess the outcome of a dice roll	      *	
	*******************************************************			

"""

print(text)

#get a choice from the user
choices = (1, 2, 3)
usrchc = input("		Your choice : ")
try:
	usrchc = int(usrchc)
	print("congrats, input works : ", usrchc)
except:
	print("user input was : ", usrchc, " of type : ", type(usrchc))
finally:
	print(usrchc, type(usrchc))
if usrchc not in choices:
	clear()
	print("		Please select one of the options by its number!")
	print(text)
	
if int(usrchc) == 1:
	primes = []
	lLim = input("enter an integer greater than 2 as a lower limit of the range : ")
	lLim = lLimit(lLim)
	#print(lLim)
	hLim = input("now enter the higher limit of the range : ")
	hLim = hLimit(hLim)
	primes = scanner(lLim, hLim, primes)
	lenPrimes = len(primes)
	print("there are " + str(lenPrimes) + " primes in the range you selected:")
	print(primes)

if int(usrchc) == 2:
	while True :
		diceface = randint(1,6)
		print("The dice says {} !".format(diceface))
		ans = input("would you like to play again? (y/n)")
		if ans in ('y', 'Y'):
			continue
		elif ans in ('n', 'N'):
			break
		else:
			print("Answer: not correct.\nUser: rejected\nExiting...") 
		break    
	exit

if int(usrchc) == 3:
	while True :
		message = guesser()
		print(message)
		ans = input("would you like to play again? (y/n)")
		if ans in ('y', 'Y'):
			continue
		elif ans in ('n', 'N'):
			break
		else:
			print("Answer: not correct.\nUser: rejected\nExiting...") 
		break
	exit











