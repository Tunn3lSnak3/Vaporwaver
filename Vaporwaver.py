from tkinter import Tk
import time

def spaceDeleter():
	global listLength2
	try:
		for i in range(listLength):
			userInput2.remove(' ')
	except ValueError:
			listLength2 = len(userInput2)

listLength2 = 0
coolWord = ''
print('Enter the phrase/word you would like to make V A P O R W A V E D: ')
userInput1 = input()
userInput1 = userInput1.upper()
userInput2 = list(userInput1)
listLength = len(userInput2)
spaceDeleter()

for i in range(listLength2):
	coolWord = coolWord + ' ' + userInput2[i]
if coolWord == '':
	print('Congrats you did nothing. Nothing has occured.')

else:
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(coolWord)
	r.update() # now it stays on the clipboard after the window is closed
	r.destroy()
	print('You phrase/word is now V A P O R W A V E D. It now saved to your clipboard. Enjoy')
	print('This program will auto close in 10 seconds.')	
time.sleep(10)
