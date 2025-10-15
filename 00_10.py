# Almost the same as 00_09
#I watered the carrots and added more bush blocks.
clear()
do_a_flip()
change_hat(Hats.Purple_Hat)
while num_items(Items.Hay)<=200 or num_items(Items.Wood)<=50 or num_items(Items.Carrot)<=40:
	for x in range(get_world_size()):
		for y in range(get_world_size()-1):
			if can_harvest():
				harvest()
			if get_pos_x()==0:
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)
				if get_water()==0:
					use_item(Items.Water)
			if (get_pos_x()>=2 and get_pos_y()<=1) or get_pos_x()==1:
				plant(Entities.Bush)
			if (get_pos_x()%2==0):
				move(North)
			if (get_pos_x()%2==1):
				move(South)
		if can_harvest():
			harvest()
		if get_pos_x()==0:
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Carrot)
		if get_pos_x()>=1 and get_pos_y()<=1:
			plant(Entities.Bush)
		move(East)
	move(North)
pet_the_piggy()
print("Fin!")
