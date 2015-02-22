#!/usr/bin/env python
import time
import sys

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
		print("Game Over. Do you wish to play again?")
		sys.exit(0)
	else:
		print("Inside there is a map that shows you to a cave")
		print()

def displayStorythree():
	print("you follow the map's path")
	print("traveling through the land")
	print("you then come to a fork in the road")
	print("one path leads left the other leads right")
	print()

def choosePath():
	path = ""
	while path != "LEFT" and path != "RIGHT":
		print("Which path do you choose LEFT or RIGHT")
		path = input()

		return path

def checkPath(choosePath):
	print("after choosing your path")
	time.sleep(2)
	print("you run to the path that you have chosen")
	time.sleep(2)
	print()

	badPath = "RIGHT"

	if choosePath == str(badPath):
		print("You run right into a demon mouth")
		print()
		print("Game Over. Do you wish to play again?")
		sys.exit(0)
	else:
		print()
		print("you have reached a clearing!!")	
		print()


def displayStoryfour():
	print("After the path finishes")
	print("you see two caves")
	print("one covered in gold")
	print("the other covered in silver")
	print()

def chooseCave():
	cave = ""
	while cave != "Gold" and cave != "Silver":
		print("Which cave do you choose Gold or Silver")
		path = input()

		return cave

def checkCave(chooseCave):
	print("you journey into the cave")
	time.sleep(2)
	print("there is a demon in here!!")
	time.sleep(2)
	print("it comes forward")
	time.sleep(2)
	print()

	badCave = "Gold"

	if chooseCave == str(badCave):
		print("the demon swallows you whole")
		print()
		print("Game Over. Do you wish to play again?")
		sys.exit(0)
	else:
		print()
		print("CONGRATS YOU GET ALL OF THE TREASURE")
		print()

displayStoryone()

weaponNumber = chooseWeapon()

checkWeapon(weaponNumber)

displayStorytwo()

vaseNumber = chooseVase()

checkVase(vaseNumber)

displayStorythree()

pathNumber = choosePath()

checkPath(pathNumber)

displayStoryfour()

caveNumber = chooseCave()

checkCave(caveNumber)
