# I tried getting 100 hays and more woods
clear()
while True:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if can_harvest():
				harvest()
			if num_items(Items.Hay) >= 100:
				plant(Entities.Bush)
			move(North)
		move(East)
