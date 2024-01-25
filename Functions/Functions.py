#!/bin/python3

#Programmer: Alex Thornton
#Program: Functions
#Date: 1.19.2024

def nl():
	print('\n') #New Line Function

def who_am_i(): #this is a function without parameters 
	name = "Alex" #local variable
	age = 16
	print("My name is" ,name,"and I am",age,"years old.")
	
who_am_i()
nl()
def add_one_hundred(num): #num is a Parameter
	print(num+ 100)
	
add_one_hundred(5) #5 is the Argument which inserts itself into the Parameter
nl()

add_one_hundred(0)
nl()
def add(x,y): # Add is the operator
	print(x + y)
	
add(55,102) # The numbers are the operons
nl()
