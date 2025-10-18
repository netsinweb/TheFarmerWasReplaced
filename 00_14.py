# Tree
# The action was written to a separate file "autoPlant" and made compatible with tree planting.

import autoMove
import autoPlant

hayTargetNumber = 0
woodTargetNumber = 0
carrotTargetNumber = 1000

def isComplete():
	return (
		num_items(Items.Hay) >= hayTargetNumber and
		num_items(Items.Wood) >= woodTargetNumber and
		num_items(Items.Carrot) >= carrotTargetNumber
	)

def main():
	# initial
	clear()
	worldSize = get_world_size()
	isMove = True
	autoPlant.setHayTargetNumber(hayTargetNumber)
	autoPlant.setWoodTargetNumber(woodTargetNumber)
	autoPlant.setCarrotTargetNumber(carrotTargetNumber)
	autoPlant.calcCost()
	do_a_flip()
	change_hat(Hats.Green_Hat)

	# main routine
	while isMove and not isComplete():
		autoPlant.action()
		isMove = autoMove.loopSnake(worldSize, worldSize)

	## fin
	pet_the_piggy()
	print("Complete!")

if __name__ == "__main__":
	main()
