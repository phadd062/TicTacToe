#! /usr/bin/python

def display(row1, row2, row3):
	'''
	DOCSTRING: This function shows the rows
	INPUT: row1, row2, row3
	OUTPUT: N/A
	'''
	print(row1)
	print(row2)
	print(row3)

def user_choice():
	'''
	DOCSTRING: This function validates user input
	INPUT: N/A
	OUTPUT: N/A
	'''
	while True:
		choice = input("Please enter a number (0-10): ")
		if(choice.isdigit()):
			choice = int(choice)
			for i in range(0, 11):
				if i == choice:
					return choice		
		print("Try again!")

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

display(row1, row2, row3)

print(user_choice())
