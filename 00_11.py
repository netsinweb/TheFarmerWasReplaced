# Now that I have the functions, I've put together some movements and actions.
# isComplete() is the target harvest number setting
# action() is for performing actions such as harvesting, planting, and watering.
#snakeMove() is a function that moves the drone along a snake-like course.

def isComplete():
	return (
		num_items(Items.Hay) >= 200 and
		num_items(Items.Wood) >= 50 and
		num_items(Items.Carrot) >= 55
	)

def action():
	if can_harvest():
		harvest()
	if get_pos_x() == 0:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		if get_water() == 0:
			use_item(Items.Water)
	if (get_pos_x() >= 2 and get_pos_y() <= 1) or get_pos_x()== 1:
		plant(Entities.Bush)

def snakeMove(moveSize):
	maxPos = moveSize - 1
	x = get_pos_x()
	y = get_pos_y()
	if x == 0 and y == 0:
		move(North)
		return
	if x == maxPos and y == maxPos:
		move(North)
		move(East)
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
