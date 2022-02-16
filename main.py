#team B23
#Import libraries 
from datetime import datetime
import calendar
import math

#Get info about current time
currentTime = datetime.now()

#Get day of the week
weekDayNumber = datetime.today().weekday()

#Convert to English
weekDay = calendar.day_name[weekDayNumber]

#print menu messages
print('    Welcome to the task selection menu!\n')

#use f-strings to add time
print(f"    Today's date: {weekDay} {currentTime.day}/{currentTime.month}/{currentTime.year}")

#Convert to standard time
standardTime = currentTime.strftime("%I:%M %p")


print(f'    Program start time: {standardTime}')

#Print menu box
print(
'''    --------------------------------------------
    | 1.  Military to standard time converter  |
    | 2.  Pythagorean theorem calculator       |
    | 3.  Parentheses balancer                 |
    | 4.  Square checker                       |
    | 5.  Secret function                      |
    | 6.  Leap year checker                    |
    | 7.  Monoalphabetic substitution          |
    | 8.  Number weaver                        |
    | 9.  Secret word counter                  |
    | 10. Descriptive statistics               |
    | 11. Hex-to-RGB converter                 |
    | 12. Primality tester                     |
    | 13. Typing test                          |
    --------------------------------------------
''')

try:
	# Ask for task number, and tries to make it an integer
	numberStr = input('Choose a task to run by entering the corresponding number!\n')
	number = int(numberStr)
except:
	#If there is an error, shut down
	print('please enter a valid task number!')
	exit()

#Importing tasks

def military_to_std_time_converter():
	print("This task will convert a military timestamp to a standard 12 hour timestamp.")
	print("Please enter a military timestamp formatted as HH:MM!")
	#try to convert
	try:
		mil_time = input()
		std_time = datetime.strptime(mil_time, "%H:%M")
		std_time = std_time.strftime("%I:%M %p")
		print(std_time)
	except:
		# if unsucessful, shut down
		print('Please enter a military timestamp formatted as HH:MM!')


def parentheses_balancer():
	print('This task will check whether or not a string with parentheses is balanced based on whether or not every open parenthesis is closed correctly.')
	inputStr = input('Please enter a string of length < 128 with parentheses! Additional non-parentheses characters are permitted.\n')
	openParentheses = inputStr.count('(')
	closeParentheses = inputStr.count(')')
	if openParentheses == closeParentheses:
		print('All parentheses are balanced in the input string')
	else:
		print('All parentheses are not balanced in the input string')




if number == 1:
	military_to_std_time_converter()
elif number == 2:
	pass
elif number == 3:
	parentheses_balancer()
else: 
	# If no tasks with the number are found give warning
	print('Please select a valid task!')

#exit after task is finished
exit()