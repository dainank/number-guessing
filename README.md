# Number Guessing Game
A very simple guessing game in Python, one of the many exercises from the book [`python-workout`](https://www.manning.com/books/python-workout) by *Reuven M. Lerner*. Exercises will quickly get more complex than this!

## Requirements
- a void function `guessing_game` with no parameters
- choose random number between 0 and 100
- user guesses number with hints on error
- once number is guessed, application exits, otherwise it loops again

## Missing Ideas
> Some additional things I could've done in the implementation.

1. Add a prompt for the user, to personlize the experience:
```py
name = input('Enter your name: ')
print(f'Hello, {name}!')
```

2. Don't try user input with the `while = true`:
```py
# Walrus Operator
while s := input('Enter thoughts:'):
   print(f'Your thoughts are: {s}')
```

## Key Concepts:
|   Concept   	|                             What is it?                            	|                             Example                            	|               To learn more               	|
|:-----------:	|:------------------------------------------------------------------:	|:--------------------------------------------------------------:	|:-----------------------------------------:	|
| random      	| Module for generating random numbers and selecting random elements 	| `number = random.randint(1, 100)`                                	| http://mng.bz/Z2wj                        	|
| Comparisons 	| Operators for comparing values                                     	| `x < y`                                                          	| http://mng.bz/oPJj                        	|
| f-strings   	| Strings into which expressions can be interpolated                 	| `f'It is currently {datetime.datetime .now()}' `                 	| http://mng.bz/1z6Z & http://mng.bz/PAm2 	|
| for loops   	| Iterates over the elements of an iterable                          	| `for i in range(10): print(i*i)`                                 	| http://mng.bz/Jymp                        	|
| input       	| Prompts the user to enter a string, and returns a string           	| `input('Enter your name: ')`                                    	| http://mng.bz/wB27                        	|
| enumerate   	| Helps us to number elements of iterables                           	| `for index, item in enumerate('abc'): print(f'{index}: {item}')` 	| http://mng.bz/qM1K                        	|
| reversed    	| Returns an iterator with the reversed elements of an iterable      	| `r = reversed('abcd')`                                           	| http://mng.bz/7XYx                        	|