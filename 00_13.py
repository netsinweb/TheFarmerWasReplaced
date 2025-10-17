# Expanded (Level 4)
# Move function to a separate file "autoMove"

import autoMove

hayTargetNumber = 100
woodTargetNumber = 50
carrotTargetNumber = 70
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

def main():
	# initial
	clear()
	do_a_flip()
	change_hat(Hats.Purple_Hat)

	# main routine
	while not isComplete():
		action()
		autoMove.snakeMove(get_world_size())

	## fin
	pet_the_piggy()
	print("Complete!")

if __name__ == "__main__":
	main()
