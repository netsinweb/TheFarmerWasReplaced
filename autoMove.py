def pointMove(toX = 0, toY = 0):
	x = get_pos_x()
	y = get_pos_y()
	directionX = East
	if (toX - x) < 0:
		directionX = West
	directionY = North
	if (toY - y) < 0:
		directionY = South

	while get_pos_x() != toX:
		move(directionX)
	while get_pos_y() != toY:
		move(directionY)

def snakeMove(sizeX, sizeY, minX = 0, minY = 0):
	maxX = sizeX - 1
	maxY = sizeY - 1
	x = get_pos_x()
	y = get_pos_y()
	xEnd = maxX
	yEnd = maxY - maxY * (1 - sizeX%2)
	if x == minX and y == minY:
		move(North)
		return True
	if x == xEnd and y == yEnd:
		pointMove()
		return True
	if x%2 == 1:
		if y == minY:
			move(East)
			return True
		move(South)
		return True
	if y == maxY:
		move(East)
		return True
	move(North)
	return True

def loopSnake(sizeX, sizeY, minX = 0, minY = 0):
	if sizeX < 2 or sizeY < 2:
		print("Size too small! (2 or more)")
		change_hat(Hats.Purple_Hat)
		return False
	if (sizeX%2 == 1):
		print("X size is not an even number!")
		change_hat(Hats.Purple_Hat)
		return False
	maxX = sizeX - 1
	maxY = sizeY - 1
	x = get_pos_x()
	y = get_pos_y()
	if x == minX and y == minY:
		move(North)
		return True
	if y == minY:
		move(West)
		return True
	if x%2 == 1:
		if y == (minY + 1) and x < maxX:
			move(East)
			return True
		move(South)
		return True
	if y == maxY:
		move(East)
		return True
	move(North)
	return True
