# Tree
# The action was written to a separate file "autoPlant" and made compatible with tree planting.
# Add logging, and changed the initial setting variables and arguments of each function according to the changes in autoMove and autoPlant.

import autoMove
import autoPlant
import logging

hayTargetNumber = 0
woodTargetNumber = 0
carrotTargetNumber = 1500
punpkinTargetNumber = 0
taregtNumber = [
	hayTargetNumber,
	woodTargetNumber,
	carrotTargetNumber,
	punpkinTargetNumber
]

hayHarvestRate = 4
woodHarvestRate = 8
carrotHarvestRate = 2
punpkinHarvestRate = 1
harvestRate = [
	hayHarvestRate,
	woodHarvestRate,
	carrotHarvestRate,
	punpkinHarvestRate
]

carrotLevel = 2
punpkinLevel = 1
entityLevel = [
	carrotLevel,
	punpkinLevel
]

def isComplete():
	return (
		num_items(Items.Hay) >= hayTargetNumber and
		num_items(Items.Wood) >= woodTargetNumber and
		num_items(Items.Carrot) >= carrotTargetNumber and
		num_items(Items.Pumpkin) >= punpkinTargetNumber
	)

def main():
	# initial
	clear()
	worldSize = [get_world_size(), get_world_size()]
	isMove = True
	autoPlant.init(worldSize, taregtNumber, harvestRate, entityLevel)
	logging.itemLog("## satrt Log")
	do_a_flip()
	change_hat(Hats.Gray_Hat)

	# main routine
	step = worldSize[0] * worldSize[1]
	while isMove and not isComplete():
		autoPlant.action()
		isMove = autoMove.loopSnake(worldSize)

	## fin
	pet_the_piggy()
	print("Complete!")
	logging.compLog()
	logging.itemLog("## end Log")

if __name__ == "__main__":
	main()
