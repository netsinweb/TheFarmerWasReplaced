hayTargetNumber = 0
woodTargetNumber = 0
carrotTargetNumber = 0
punpkinTargetNumber = 0

hayHarvestRate = 4
woodHarvestFromBushRate = 1
woodHarvestFromTreeRate = 4
carrotHarvestRate = 2
punpkinHarvestRate = 1

carrotLevel = 2
punpkinLevel = 1

hayNeedsNumber = 0
woodNeedsNumber = 0
carrotNeedsNumber = 0
punpkinNeedsNumber = 0

grassPlantedNumber = 0
bushPlantedNumber = 0
treePlantedNumber = 0
carrotPlantedNumber = 0
punpkinPlantedNumber = 0

hayHarvestNumber = 0
woodHarvestNumber = 0
carrotHarvestNumber = 0
punpkinHarvestNumber = 0

hayComp = False
woodComp = False
carrotComp = False
punpkinComp = False

def setHayTargetNumber(num):
	global hayTargetNumber
	hayTargetNumber = num

def setWoodTargetNumber(num):
	global woodTargetNumber
	woodTargetNumber = num

def setCarrotTargetNumber(num):
	global carrotTargetNumber
	carrotTargetNumber = num

def setPunpkinTargetNumber(num):
	global punpkinTargetNumber
	punpkinTargetNumber = num

def calcCost():
	global carrotNeedsNumber
	carrotNeedsNumber = (punpkinTargetNumber - num_items(Items.Pumpkin)) * punpkinLevel
	global hayNeedsNumber
	hayNeedsNumber = (carrotTargetNumber + carrotNeedsNumber - num_items(Items.Carrot)) * carrotLevel
	global woodNeedsNumber
	woodNeedsNumber = (carrotTargetNumber + carrotNeedsNumber - num_items(Items.Carrot)) * carrotLevel

def init(sizeX, sizeY):
	global grassPlantedNumber
	grassPlantedNumber = sizeX * sizeY

def action(target=""):
	def getTargetPlant(target=""):
		if target != "":
			return target
		if num_items(Items.Hay) + (grassPlantedNumber * hayHarvestRate) < (hayTargetNumber + hayNeedsNumber) and not hayComp:
			return "Hay"
		if num_items(Items.Wood) + (bushPlantedNumber * woodHarvestFromBushRate) + (treePlantedNumber * 5 * woodHarvestFromTreeRate) < (woodTargetNumber + woodNeedsNumber) and not woodComp:
			return "Wood"
		if num_items(Items.Carrot) + (carrotPlantedNumber * carrotHarvestRate) < (carrotTargetNumber + carrotNeedsNumber) and not carrotComp:
			return "Carrot"
		return ""

	def planTreeOrBush():
		if get_pos_y()%2 == (1 - 1 * get_pos_x()%2):
			plant(Entities.Tree)
			global treePlantedNumber
			treePlantedNumber += 1
			return
		plant(Entities.Bush)
		global bushPlantedNumber
		bushPlantedNumber += 1
		return

	if can_harvest():
		entityType = get_entity_type()
		if entityType == Entities.Grass and harvest():
			global hayHarvestNumber
			hayHarvestNumber += (1 * hayHarvestRate)
			if  num_items(Items.Hay) >= (hayTargetNumber + hayNeedsNumber):
				global hayComp
				hayComp = True
		if entityType == Entities.Bush and harvest():
			global woodHarvestNumber
			woodHarvestNumber += (1 * woodHarvestFromBushRate)
			if num_items(Items.Wood) >= (woodTargetNumber + woodNeedsNumber):
				global woodComp
				woodComp = True
		if entityType == Entities.Tree and harvest():
			global woodHarvestNumber
			woodHarvestNumber += (5 * woodHarvestFromTreeRate)
			if num_items(Items.Wood) >= (woodTargetNumber + woodNeedsNumber):
				global woodComp
				woodComp = True
		if entityType == Entities.Carrot and harvest():
			global carrotHarvestNumber
			carrotHarvestNumber += (1 * carrotHarvestRate)
			if num_items(Items.Carrot) >= (carrotTargetNumber + carrotNeedsNumber):
				global carrotComp
				carrotComp = True

	targetPlant = getTargetPlant(target)
	if targetPlant == "Wood":
		planTreeOrBush()
		return

	if targetPlant == "Carrot":
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		global carrotPlantedNumber
		carrotPlantedNumber += 1
		if get_water() == 0:
			use_item(Items.Water)
		return

	global grassPlantedNumber
	grassPlantedNumber += 1
	return
