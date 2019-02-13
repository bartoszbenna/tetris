import sys
import colorama
import msvcrt
import os
import random
import time

colorama.init()


class Element:
	def __init__(self, position):
		self.position = position


class CurrentElement(list):
	def __init__(self):
		list.__init__(self)
		self.type = random.randint(1, 7)
		self.state = 1


numberofrows = 15
numberofcolumns = 15

table = [" "] * numberofcolumns * numberofrows

for i in range(numberofcolumns):
	table.append(colorama.Fore.WHITE + "*")

score = 0
level = 1
rowsdeleted = 0


def createElement():
	currentElement = CurrentElement()

	if currentElement.type == 1:
		currentElement.append(Element(3))
		currentElement.append(Element(4))
		currentElement.append(Element(5))
		currentElement.append(Element(6))

	elif currentElement.type == 2:
		currentElement.append(Element(3))
		currentElement.append(Element(4))
		currentElement.append(Element(5))
		currentElement.append(Element(5 + numberofcolumns))

	elif currentElement.type == 3:
		currentElement.append(Element(3))
		currentElement.append(Element(4))
		currentElement.append(Element(5))
		currentElement.append(Element(3 + numberofcolumns))

	elif currentElement.type == 4:
		currentElement.append(Element(3))
		currentElement.append(Element(4))
		currentElement.append(Element(3 + numberofcolumns))
		currentElement.append(Element(4 + numberofcolumns))

	elif currentElement.type == 5:
		currentElement.append(Element(3))
		currentElement.append(Element(4))
		currentElement.append(Element(2 + numberofcolumns))
		currentElement.append(Element(3 + numberofcolumns))

	elif currentElement.type == 6:
		currentElement.append(Element(3))
		currentElement.append(Element(4))
		currentElement.append(Element(5))
		currentElement.append(Element(4 + numberofcolumns))

	elif currentElement.type == 7:
		currentElement.append(Element(3))
		currentElement.append(Element(4))
		currentElement.append(Element(4 + numberofcolumns))
		currentElement.append(Element(5 + numberofcolumns))
	return currentElement


currentElement = createElement()


def play(currentElement, right=False, left=False, rotate=False, moveDown=False):
	global score
	global level
	global rowsdeleted
	if right:
		move = True
		for square in currentElement:
			if (square.position + 1) % numberofcolumns == 0 or table[square.position + 1] != " ":
				move = False
		if move:
			for square in currentElement:
				square.position += 1
	if left:
		move = True
		for square in currentElement:
			if square.position % numberofcolumns == 0 or table[square.position - 1] != " ":
				move = False
		if move:
			for square in currentElement:
				square.position -= 1
	if rotate:
		if currentElement.type == 1:
			if currentElement.state == 1:
				if table[currentElement[0].position - (2 * numberofcolumns) + 2] == " " and table[
					currentElement[1].position - numberofcolumns + 1] == " " and table[
					currentElement[3].position + numberofcolumns - 1] == " ":
					currentElement[0].position += (-(2 * numberofcolumns) + 2)
					currentElement[1].position += (-numberofcolumns + 1)
					currentElement[3].position += (numberofcolumns - 1)
					currentElement.state = 2
			elif currentElement.state == 2:
				if table[currentElement[0].position + (2 * numberofcolumns) - 2] == " " and table[
					currentElement[1].position + numberofcolumns - 1] == " " and table[
					currentElement[3].position - numberofcolumns + 1] == " ":
					if (currentElement[0].position + 1) % numberofcolumns == 0:
						for square in currentElement:
							square.position -= 1
					elif currentElement[0].position % numberofcolumns == 0:
						for square in currentElement:
							square.position += 2
					currentElement[0].position += (2 * numberofcolumns) - 2
					currentElement[1].position += numberofcolumns - 1
					currentElement[3].position += (-numberofcolumns + 1)
					currentElement.state = 1
		if currentElement.type == 2:
			if currentElement.state == 1:
				if table[currentElement[0].position - numberofcolumns + 1] == " " and table[
					currentElement[2].position + numberofcolumns - 1] == " " and table[
					currentElement[3].position - 2] == " ":
					currentElement[0].position += (-numberofcolumns + 1)
					currentElement[2].position += (numberofcolumns - 1)
					currentElement[3].position += (-2)
					currentElement.state = 2
			elif currentElement.state == 2:
				if table[currentElement[0].position + numberofcolumns + 1] == " " and table[
					currentElement[2].position - numberofcolumns - 1] == " " and table[
					currentElement[3].position - 2 * numberofcolumns] == " ":
					if (currentElement[0].position + 1) % numberofcolumns == 0:
						for square in currentElement:
							square.position -= 1
					currentElement[0].position += (numberofcolumns + 1)
					currentElement[2].position += (-numberofcolumns - 1)
					currentElement[3].position += (-2 * numberofcolumns)
					currentElement.state = 3
			elif currentElement.state == 3:
				if table[currentElement[0].position + numberofcolumns - 1] == " " and table[
					currentElement[2].position - numberofcolumns + 1] == " " and table[
					currentElement[3].position + 2] == " ":
					currentElement[0].position += (numberofcolumns - 1)
					currentElement[2].position += (-numberofcolumns + 1)
					currentElement[3].position += 2
					currentElement.state = 4
			elif currentElement.state == 4:
				if table[currentElement[0].position - numberofcolumns - 1] == " " and table[
					currentElement[2].position + numberofcolumns + 1] == " " and table[
					currentElement[3].position + 2 * numberofcolumns] == " ":
					if currentElement[2].position % numberofcolumns == 0:
						for square in currentElement:
							square.position += 1
					currentElement[0].position += (-numberofcolumns - 1)
					currentElement[2].position += (numberofcolumns + 1)
					currentElement[3].position += (2 * numberofcolumns)
					currentElement.state = 1
		if currentElement.type == 3:
			if currentElement.state == 1:
				if table[currentElement[0].position - numberofcolumns + 1] == " " and table[
					currentElement[2].position + numberofcolumns - 1] == " " and table[
					currentElement[3].position - 2 * numberofcolumns] == " ":
					currentElement[0].position += (-numberofcolumns + 1)
					currentElement[2].position += (numberofcolumns - 1)
					currentElement[3].position += (-2 * numberofcolumns)
					currentElement.state = 2
			elif currentElement.state == 2:
				if table[currentElement[0].position + numberofcolumns + 1] == " " and table[
					currentElement[2].position - numberofcolumns - 1] == " " and table[
					currentElement[3].position + 2] == " ":
					if (currentElement[0].position + 1) % numberofcolumns == 0:
						for square in currentElement:
							square.position -= 1
					currentElement[0].position += (numberofcolumns + 1)
					currentElement[2].position += (-numberofcolumns - 1)
					currentElement[3].position += 2
					currentElement.state = 3
			elif currentElement.state == 3:
				if table[currentElement[0].position + numberofcolumns - 1] == " " and table[
					currentElement[2].position - numberofcolumns + 1] == " " and table[
					currentElement[3].position + 2 * numberofcolumns] == " ":
					currentElement[0].position += (numberofcolumns - 1)
					currentElement[2].position += (-numberofcolumns + 1)
					currentElement[3].position += (2 * numberofcolumns)
					currentElement.state = 4
			elif currentElement.state == 4:
				if table[currentElement[0].position - numberofcolumns - 1] == " " and table[
					currentElement[2].position + numberofcolumns + 1] == " " and table[
					currentElement[3].position - 2] == " ":
					if currentElement[2].position % numberofcolumns == 0:
						for square in currentElement:
							square.position += 1
					currentElement[0].position += (-numberofcolumns - 1)
					currentElement[2].position += (numberofcolumns + 1)
					currentElement[3].position += (-2)
					currentElement.state = 1
		if currentElement.type == 5:
			if currentElement.state == 1:
				if table[currentElement[0].position + numberofcolumns + 1] == " " and table[
					currentElement[1].position + 2 * numberofcolumns] == " " and table[
					currentElement[2].position - numberofcolumns + 1] == " ":
					currentElement[0].position += (numberofcolumns + 1)
					currentElement[1].position += (2 * numberofcolumns)
					currentElement[2].position += (-numberofcolumns + 1)
					currentElement.state = 2
			elif currentElement.state == 2:
				if table[currentElement[0].position + numberofcolumns - 1] == " " and table[
					currentElement[1].position - 2] == " " and table[
					currentElement[2].position + numberofcolumns + 1] == " ":
					if currentElement[2].position % numberofcolumns == 0:
						for square in currentElement:
							square.position += 1
					currentElement[0].position += (numberofcolumns - 1)
					currentElement[1].position += (-2)
					currentElement[2].position += (numberofcolumns + 1)
					currentElement.state = 3
			elif currentElement.state == 3:
				if table[currentElement[0].position - numberofcolumns - 1] == " " and table[
					currentElement[1].position - 2 * numberofcolumns] == " " and table[
					currentElement[2].position + numberofcolumns - 1] == " ":
					currentElement[0].position += (-numberofcolumns - 1)
					currentElement[1].position += (-2 * numberofcolumns)
					currentElement[2].position += (numberofcolumns - 1)
					currentElement.state = 4
			elif currentElement.state == 4:
				if table[currentElement[0].position - numberofcolumns + 1] == " " and table[
					currentElement[1].position + 2] == " " and table[
					currentElement[2].position - numberofcolumns - 1] == " ":
					if (currentElement[3].position + 1) % numberofcolumns == 0:
						for square in currentElement:
							square.position -= 1
					currentElement[0].position += (-numberofcolumns + 1)
					currentElement[1].position += 2
					currentElement[2].position += (-numberofcolumns - 1)
					currentElement.state = 1
		if currentElement.type == 6:
			if currentElement.state == 1:
				if table[currentElement[0].position - numberofcolumns + 1] == " " and table[
					currentElement[2].position + numberofcolumns - 1] == " " and table[
					currentElement[3].position - numberofcolumns - 1] == " ":
					currentElement[0].position += (-numberofcolumns + 1)
					currentElement[2].position += (numberofcolumns - 1)
					currentElement[3].position += (-numberofcolumns - 1)
					currentElement.state = 2
			elif currentElement.state == 2:
				if table[currentElement[0].position + numberofcolumns + 1] == " " and table[
					currentElement[2].position - numberofcolumns - 1] == " " and table[
					currentElement[3].position - numberofcolumns + 1] == " ":
					if (currentElement[0].position + 1) % numberofcolumns == 0:
						for square in currentElement:
							square.position -= 1
					currentElement[0].position += (numberofcolumns + 1)
					currentElement[2].position += (-numberofcolumns - 1)
					currentElement[3].position += (-numberofcolumns + 1)
					currentElement.state = 3
			elif currentElement.state == 3:
				if table[currentElement[0].position + numberofcolumns - 1] == " " and table[
					currentElement[2].position - numberofcolumns + 1] == " " and table[
					currentElement[3].position + numberofcolumns + 1] == " ":
					currentElement[0].position += (numberofcolumns - 1)
					currentElement[2].position += (-numberofcolumns + 1)
					currentElement[3].position += (numberofcolumns + 1)
					currentElement.state = 4
			elif currentElement.state == 4:
				if table[currentElement[0].position - numberofcolumns - 1] == " " and table[
					currentElement[2].position + numberofcolumns + 1] == " " and table[
					currentElement[3].position + numberofcolumns - 1] == " ":
					if currentElement[2].position % numberofcolumns == 0:
						for square in currentElement:
							square.position += 1
					currentElement[0].position += (-numberofcolumns - 1)
					currentElement[2].position += (numberofcolumns + 1)
					currentElement[3].position += (numberofcolumns - 1)
					currentElement.state = 1
		if currentElement.type == 7:
			if currentElement.state == 1:
				if table[currentElement[0].position + 2] == " " and table[
					currentElement[1].position + numberofcolumns + 1] == " " and table[
					currentElement[3].position + numberofcolumns - 1] == " ":
					currentElement[0].position += 2
					currentElement[1].position += (numberofcolumns + 1)
					currentElement[3].position += (numberofcolumns - 1)
					currentElement.state = 2
			elif currentElement.state == 2:
				if table[currentElement[0].position + 2 * numberofcolumns] == " " and table[
					currentElement[1].position + numberofcolumns - 1] == " " and table[
					currentElement[3].position - numberofcolumns - 1] == " ":
					if currentElement[2].position % numberofcolumns == 0:
						for square in currentElement:
							square.position += 1
					currentElement[0].position += (2 * numberofcolumns)
					currentElement[1].position += (numberofcolumns - 1)
					currentElement[3].position += (-numberofcolumns - 1)
					currentElement.state = 3
			elif currentElement.state == 3:
				if table[currentElement[0].position - 1] == " " and table[
					currentElement[1].position - numberofcolumns - 1] == " " and table[
					currentElement[3].position - numberofcolumns + 1] == " ":
					currentElement[0].position += (-2)
					currentElement[1].position += (-numberofcolumns - 1)
					currentElement[3].position += (-numberofcolumns + 1)
					currentElement.state = 4
			elif currentElement.state == 4:
				if table[currentElement[0].position - 2 * numberofcolumns] == " " and table[
					currentElement[1].position - numberofcolumns + 1] == " " and table[
					currentElement[3].position + numberofcolumns + 1] == " ":
					if (currentElement[3].position + 1) % numberofcolumns == 0:
						for square in currentElement:
							square.position -= 1
					currentElement[0].position += (-2 * numberofcolumns)
					currentElement[1].position += (-numberofcolumns + 1)
					currentElement[3].position += (numberofcolumns + 1)
					currentElement.state = 1

	os.system("cls")
	for i in range(len(table)):
		ending = ""
		if i != 0 and (i + 1) % numberofcolumns == 0:  # koniec linii
			ending = "\n"

		isOccupied = False
		for square in currentElement:
			if square.position == i:
				isOccupied = True
		if isOccupied:
			if currentElement.type == 1:
				print(colorama.Fore.CYAN + u"\u25A0", end=ending)
			if currentElement.type == 2:
				print(colorama.Fore.BLUE + u"\u25A0", end=ending)
			if currentElement.type == 3:
				print(colorama.Fore.LIGHTYELLOW_EX + u"\u25A0", end=ending)
			if currentElement.type == 4:
				print(colorama.Fore.YELLOW + u"\u25A0", end=ending)
			if currentElement.type == 5:
				print(colorama.Fore.GREEN + u"\u25A0", end=ending)
			if currentElement.type == 6:
				print(colorama.Fore.MAGENTA + u"\u25A0", end=ending)
			if currentElement.type == 7:
				print(colorama.Fore.RED + u"\u25A0", end=ending)
		else:
			# print(" ", end="")
			print(table[i], end=ending)

	print(repr('Score:').center(numberofcolumns))
	print(repr(score).center(numberofcolumns))

	print("\n" + repr('Level:').center(numberofcolumns))
	print(repr(level).center(numberofcolumns))

	saveState = False
	for square in currentElement:
		if square.position + numberofcolumns > len(table) - 1:
			saveState = True
		elif table[square.position + numberofcolumns] != " ":
			saveState = True

	if saveState is False and moveDown is True:
		for square in currentElement:
			square.position += numberofcolumns

	if saveState is True:
		for square in currentElement:
			if currentElement.type == 1:
				table[square.position] = colorama.Fore.CYAN + u"\u25A0"
			if currentElement.type == 2:
				table[square.position] = colorama.Fore.BLUE + u"\u25A0"
			if currentElement.type == 3:
				table[square.position] = colorama.Fore.LIGHTYELLOW_EX + u"\u25A0"
			if currentElement.type == 4:
				table[square.position] = colorama.Fore.YELLOW + u"\u25A0"
			if currentElement.type == 5:
				table[square.position] = colorama.Fore.GREEN + u"\u25A0"
			if currentElement.type == 6:
				table[square.position] = colorama.Fore.MAGENTA + u"\u25A0"
			if currentElement.type == 7:
				table[square.position] = colorama.Fore.RED + u"\u25A0"

		row = 0
		rowstodelete = []
		for a in range(numberofrows):
			spaces = False
			for i in range(numberofcolumns):
				if table[row * numberofcolumns + i] == " ":
					spaces = True
			if not spaces:
				rowstodelete.append(row)
			row += 1

		for row in rowstodelete:
			for i in range(numberofcolumns):
				del table[row * numberofcolumns]
			for i in range(numberofcolumns):
				table.insert(0, " ")
		if len(rowstodelete) == 1:
			score += 40
		elif len(rowstodelete) == 2:
			score += 100
		elif len(rowstodelete) == 3:
			score += 300
		elif len(rowstodelete) == 4:
			score += 1200
		elif len(rowstodelete) > 4:
			score += len(rowstodelete) * 300

		rowsdeleted += len(rowstodelete)

		if rowsdeleted >= 10:
			if level < 11:
				level += 1
				rowsdeleted = 0

		return True


# game logic

print(" " * 13, end="")
print(
	colorama.Fore.CYAN + "T" + colorama.Fore.BLUE + "E" + colorama.Fore.LIGHTYELLOW_EX + "T" + colorama.Fore.YELLOW + "R" + colorama.Fore.GREEN + "I" + colorama.Fore.RED + "S")
print("\n" + " " * 12, end="")
print(colorama.Fore.WHITE + "Controls" + "\n")
print("Left arrow key - move left")
print("Right arrow key - move right")
print("Up arrow key - rotate clockwise")
print("Down arrow key - soft drop")
print("Space - hard drop")
print("\n" + "Press ENTER to start the game...")
while True:
	if msvcrt.getch() == b'\r':
		while True:
			move_length = 0.5 - (level - 1) * 0.05

			end_of_move = time.time() + move_length
			while time.time() <= end_of_move:
				while time.time() <= end_of_move:
					if msvcrt.kbhit():
						key = msvcrt.getch()
						if key == b'\xe0':
							d = msvcrt.getch()
							if d == b'H':
								if play(currentElement, rotate=True):
									break
							elif d == b'K':
								if play(currentElement, left=True):
									break
							elif d == b'M':
								if play(currentElement, right=True):
									break
							elif d == b'P':
								score += 1
								if play(currentElement, moveDown=True):
									break
						elif key == b' ':
							while True:
								score += 2
								if play(currentElement, moveDown=True):
									break

				# only executed when new element is created
				if play(currentElement):
					currentElement = createElement()
					isLost = False
					for element in currentElement:
						if table[element.position] is not " ":
							isLost = True
					if isLost:
						print(colorama.Fore.WHITE + "\n\n" + "You lost!")
						time.sleep(15)
						sys.exit(1)
			# ran out of time
			play(currentElement, moveDown=True)
