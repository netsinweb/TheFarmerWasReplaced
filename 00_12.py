# Expanded (Level 3)
# Next, I want to improve the usability of action().
# Automatically calculate the required cost based on the target number of harvested items (hay, wood, carrots).
# Then, grow and harvest the items in order.

hayTargetNumber = 200
woodTargetNumber = 50
carrotTargetNumber = 80
hayNeedsNumber = carrotTargetNumber * 1
woodNeedsNumber = carrotTargetNumber * 1
carrotNeedsNumber = 0
hayComp = False
woodComp = False
carrotComp = False

def isComplete():
	return (
		num_items(Items.Hay) >= hayTargetNumber and
		num_items(Items.Wood) >= woodTargetNumber and
		num_items(Items.Carrot) >= carrotTargetNumber
	)

def getTargetPlant():
	if num_items(Items.Hay) < (hayTargetNumber + hayNeedsNumber) and not hayComp:
		return "Hey"
	if num_items(Items.Wood) < (woodTargetNumber + woodNeedsNumber) and not woodComp:
		return "Wood"
	if num_items(Items.Carrot) < (carrotTargetNumber + carrotNeedsNumber) and not carrotComp:
		return "Carrot"
	return ""

def action():
	if can_harvest():
		entityType = get_entity_type()
		if entityType == Entities.Grass and harvest() and num_items(Items.Hay) >= (hayTargetNumber + hayNeedsNumber):
			global hayComp
			hayComp = True
		if entityType == Entities.Bush and harvest() and num_items(Items.Wood) >= (woodTargetNumber + woodNeedsNumber):
			global woodComp
			woodComp = True
		if entityType == Entities.Carrot and harvest() and num_items(Items.Carrot) >= (carrotTargetNumber + carrotNeedsNumber):
			global carrotComp
			carrotComp = True

	targetPlant = getTargetPlant()
	if targetPlant == "":
		return

	if targetPlant == "Wood":
		plant(Entities.Bush)

	if targetPlant == "Carrot":
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		if get_water() == 0:
			use_item(Items.Water)

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

# initial
clear()
do_a_flip()
change_hat(Hats.Purple_Hat)

# main routine
while not isComplete():
	action()
	snakeMove(get_world_size())

## fin
pet_the_piggy()
print("Complete!")
