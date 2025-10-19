# カボチャの植栽、育成、収穫関連
# 栽培サイズの指定


import autoMove

def isHarvest(growthNum, size):
	return growthNum == size ** 2

def doPlant(size, point=[0, 0]):
	for i in range(size ** 2):
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		autoMove.snakeMove([size, size], point)

def checkHarvest(size, point=[0, 0]):
		growthNum = 0
		for i in range(size ** 2):
			if not can_harvest():
				plant(Entities.Pumpkin)
			else:
				growthNum += 1
			autoMove.snakeMove([size, size], point)
		return isHarvest(growthNum, size)

def autoAction(size, point=[0, 0]):
	doPlant(size, point)
	while True:
		if checkHarvest(size, point):
			harvest()
			break
