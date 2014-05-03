#!/usr/bin/env python
import time

def displayStoryone():
    print("you are in a land full of demons. In front of you")
    print("there are two weapons in a chest,") 
    print("one is a sword good for close range")
    print("the next is a bow good for long range")
    print()

def chooseWeapon():
    weapon = ""
    while weapon != "Bow" and weapon != "Sword":
        print("which do you choose? Bow or Sword?")
        weapon = input()

        return weapon
        
def checkWeapon(chooseWeapon):
	print("You open the chest..")
	time.sleep(2)
	print("you have chosen...")
	time.sleep(2)
	print(chooseWeapon)

def displayStorytwo():
	print()
	print("You go forth with your weapon")
	print("passing many lands, lakes and rivers")
	print("you come across an abandon marketplace")
	print("and you see that there are vases in front with a note")
	print("the note reads that one vase has a demon")
	print("while another one has a map to treasure")
	print()
	
def chooseVase():
    vase = ""
    while vase != "Blue" and vase != "Red":
        print("which do you choose? Blue or Red?")
        vase = input()

        return vase

def checkVase(chooseVase):
	print("using your weapon you smash one of the vase")
	time.sleep(2)
	print("within the vase...")
	time.sleep(2)
	print()
	
	badVase = "Red"
	
	if chooseVase == str(badVase):
		print("A Demon hopes out and kills you")
		print()
		print("Game Over. Do you wish to play again? ")
	else:
		print("Inside there is a map that shows you to a cave")

	def displayStorythree():
		print("you follow the maps path")
		print("traveling through the land ")
displayStoryone()

weaponNumber = chooseWeapon()

checkWeapon(weaponNumber)

displayStorytwo()

vaseNumber = chooseVase()

checkVase(vaseNumber)

displayStorythree()
