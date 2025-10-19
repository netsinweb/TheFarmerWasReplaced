def pointMove(toPointList = [0, 0]):
	toX, toY = toPointList
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

def snakeMove(sizeList, minPointList = [0, 0]):
	sizeX, sizeY = sizeList
	minX, minY = minPointList
	if sizeX < 2 or sizeY < 2:
		print("Size too small! (2 or more)")
		change_hat(Hats.Purple_Hat)
		return False
	maxX = sizeX - 1
	maxY = sizeY - 1
	# ドローンの座標はスタート地点を[0,0]とする相対値とする
	x = get_pos_x() - minX
	y = get_pos_y() - minY
	xEnd = maxX
	yEnd = maxY - maxY * (1 - sizeX%2)
	if x == 0 and y == 0:
		move(North)
		return True
	if x == xEnd and y == yEnd:
		pointMove(minPointList)
		return True
	if x%2 == 1:
		if y == 0:
			move(East)
			return True
		move(South)
		return True
	if y == maxY:
		move(East)
		return True
	move(North)
	return True

def loopSnake(sizeList, minPointList = [0, 0]):
	sizeX, sizeY = sizeList
	minX, minY = minPointList
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
	# ドローンの座標はスタート地点を[0,0]とする相対値とする
	x = get_pos_x() - minX
	y = get_pos_y() - minY
	if x == 0 and y == 0:
		move(North)
		return True
	if y == 0:
		move(West)
		return True
	if x%2 == 1:
		if y == 1 and x < maxX:
			move(East)
			return True
		move(South)
		return True
	if y == maxY:
		move(East)
		return True
	move(North)
	return True
