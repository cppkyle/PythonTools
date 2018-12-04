#!/usr/bin/python
# Kyle Bouchard (cppkyle), December 3 2018
# A small tool built for my math class
import math
import sys
def startProgram():
	choice = str(input("\n[1] Find Hypotenuse\n[2] Find Other Side\n"))

	if choice == "1":
		side1 = float(input("\nEnter length of first side: "))
		side2 = float(input("\nEnter length of second side: "))
		print("Calculating...")
		hypSquare = (side1*side1)+(side2*side2)
		hyp = math.sqrt(hypSquare)
		print("\nHypotenuse is: " + str(hyp) + "\nSquared Hypotenuse is: " + str(hypSquare))
		print("\n---------\nCopy This\n---------\n\nc^2 = a^2 + b^2\nc^2 = " + str(side1) + "^2 + " + str(side2) + "^2\nc^2 = " + str(hypSquare) + "\nc = " + str(hyp))
	
	if choice == "2":
		hyp = float(input("\nEnter length of Hypotenuse: "))
		side1 = float(input("\nEnter length of Side: "))
		if hyp < side1:
			print("Error: Hypotenuse must be greater than side!")
			startProgram()
		print("Calculating...")
		hyp2 = hyp*hyp
		side12 = side1*side1
		b2 = hyp2-side12
		side2 = math.sqrt(b2)
		print("\nOther Side is: " + str(side2) + "\nOther Side Squared is: " + str(b2))
		print("\n---------\nCopy This\n---------\n\nc^2 = a^2 + b^2\n" + str(hyp) + "^2 = a^2 + " + str(side1) + "^2\n" + str(hyp2) + " = a^2 + " + str(side12) + "\n" + str(b2) + " = a^2\n" + str(side2) + " = a")
		
	redo = str(input("\nRestart program?(Y/n)\n"))
	if (redo.lower() == "y") or (redo.lower() == "ye") or (redo.lower() == ("yes")):
		startProgram()
	else:
		sys.exit()

print(" - pyThagore -\nMade by Kyle Bouchard (cppkyle) on December 3 2018\nHave fun!")
startProgram()