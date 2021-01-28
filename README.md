## UniMath
A collection of basic math games in Python 3:

### primes_finder

A simple, basic, slightly optimised Py3 prime numbers finder. 

### dice

Have the computer roll. 

### guess_dice

A simple game of "guess the the outcome of a dice roll".

*************************************************************

This should run on Linux, Windows and Mac systems indifferently. I wrote the clear() function for UniMath to be sure that it gives no issues on Windows, but I only tested it on Linux so far. Mac is UNIX-based so there should be no problem for a console-based application like this one.

primes_finder: when I say it's slightly optimised it means I implemented a few solutions to keep the number of calculatons a magnitude or so lower.
I did the following:

    '''
    def scanner(lLim, hLim, primes):
    	for i in range(lLim, hLim, 2): --> The answer can't be an even number, so skip two by two.
    		isPrime = True
    		j = 3 --> Because of course I start from 3 :) 
		      --> Starting from an odd number makes skipping 
		      --> by two effective by skipping even numbers.
    		top = int(i ** 0.5) --> The dividend of a non-prime 
		                    --> is found before its square root 
				    --> is reached, so I put a limit.
		for j in range(3, top, 2):
			if i % j == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(i)
	return(primes)
    '''
  
  I also wanted to add a check which made sure no number ending in 5 (skipping even numbers is already in place by now) would be evaluated, but I believe it would actually make the order of magnitude bigger for low numbers. Please let me know if you think otherwise.
  
## Dependencies
Python 3 (should run on any Posix or Windows environment)

## Running this code
Fork or clone, then `cd` into the UniMath directory and `python3 UniMath.py`
