hayTargetNumber = 0
woodTargetNumber = 0
carrotTargetNumber = 0
carrotLevel = 2
hayNeedsNumber = 0
woodNeedsNumber = 0
carrotNeedsNumber = 0
hayComp = False
woodComp = False
carrotComp = False

def setHayTargetNumber(num):
	global hayTargetNumber
	hayTargetNumber = num

def setWoodTargetNumber(num):
	global woodTargetNumber
	woodTargetNumber = num

def setCarrotTargetNumber(num):
	global carrotTargetNumber
	carrotTargetNumber = num

def calcCost():
	global hayNeedsNumber
	hayNeedsNumber = (carrotTargetNumber - num_items(Items.Carrot)) * carrotLevel
	global woodNeedsNumber
	woodNeedsNumber = (carrotTargetNumber - num_items(Items.Carrot)) * carrotLevel

def action(target=""):
	def getTargetPlant(target=""):
		if target != "":
			return target
		if num_items(Items.Hay) < (hayTargetNumber + hayNeedsNumber) and not hayComp:
			return "Hey"
		if num_items(Items.Wood) < (woodTargetNumber + woodNeedsNumber) and not woodComp:
			return "Wood"
		if num_items(Items.Carrot) < (carrotTargetNumber + carrotNeedsNumber) and not carrotComp:
			return "Carrot"
		return ""

	def planTreeOrBush():
		if get_pos_y()%2 == (1 - 1 * get_pos_x()%2):
			plant(Entities.Tree)
			return
		plant(Entities.Bush)

	if can_harvest():
		entityType = get_entity_type()
		if entityType == Entities.Grass and harvest() and num_items(Items.Hay) >= (hayTargetNumber + hayNeedsNumber):
			global hayComp
			hayComp = True
		if (entityType == Entities.Bush or entityType == Entities.Tree) and harvest() and num_items(Items.Wood) >= (woodTargetNumber + woodNeedsNumber):
			global woodComp
			woodComp = True
		if entityType == Entities.Carrot and harvest() and num_items(Items.Carrot) >= (carrotTargetNumber + carrotNeedsNumber):
			global carrotComp
			carrotComp = True

	targetPlant = getTargetPlant(target)
	if targetPlant == "":
		return

	if targetPlant == "Wood":
		planTreeOrBush()

	if targetPlant == "Carrot":
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		if get_water() == 0:
			use_item(Items.Water)
