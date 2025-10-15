# I want to plant bush on one block
# and harvest grass on two blocks
clear()
do_a_flip()
change_hat(Hats.Brown_Hat)
while True:
	plant(Entities.Bush)
	if can_harvest():
		harvest()
	move(North)
	if can_harvest():
		harvest()
	move(North)
	if can_harvest():
		harvest()
	move(North)
