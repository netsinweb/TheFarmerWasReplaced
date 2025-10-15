# Try harvesting with bush, grass, and bush for each row.
# And plant the bushes as soon as you harvest them.
clear()
while True:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if can_harvest():
				harvest()
			if x%2 == 0:
				plant(Entities.Bush)
			move(North)
		move(East)
