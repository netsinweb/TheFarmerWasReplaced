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

def snakeMove(moveSize):
	maxPos = moveSize - 1
	x = get_pos_x()
	y = get_pos_y()
	xEnd = maxPos
	yEnd = maxPos - maxPos * (1 - moveSize%2)
	if x == 0 and y == 0:
		move(North)
		return
	if x == xEnd and y == yEnd:
		pointMove()
		return
	if x%2 == 1:
		if y == 0:
			move(East)
			return
		move(South)
		return
	if y == maxPos:
		move(East)
		return
	move(North)
