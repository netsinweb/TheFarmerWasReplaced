# Move, drone
do_a_flip()
change_hat(Hats.Gray_Hat)
while True:
	if can_harvest():
		harvest()
	move(North)
