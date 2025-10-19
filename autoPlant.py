# 目標値(Target Number)とコスト(Needs Number)から目標収穫数を設定。
# 植栽した数(Planted Number)と1ブロックあたりの収穫単位(Harvest Unit)と収穫率(Harvest Rate)から予想収穫量を計算。
# 目標収穫数と予想収穫量から、植栽や収穫の判断(何を植えるか? 収穫は行うのか?)をさせてみた。
# 干し草、木材、人参、カボチャの順で植栽・収穫しようとします
#
# ~~人参の収穫で気付いたが、1ブロックからの収穫数がランダム。~~
# ~~とは言え、おそらく「植栽数 * 収穫単位(人参は土地1ブロックにつき1個) * 収穫率」が最低値と思われる。~~
# ~~予想よりも多く収穫できる分には困らないからこのまま進めてみる。~~
# ちゃんとログに書き出して確認したらランダムじゃないし、想定した計算であってる...落ち着け自分...

hayTargetNumber = 0
woodTargetNumber = 0
carrotTargetNumber = 0
pumpkinTargetNumber = 0

hayHarvestRate = 1
woodHarvestRate = 1
carrotHarvestRate = 1
pumpkinHarvestRate = 1

carrotLevel = 1
pumpkinLevel = 1

# 収穫単位(土地1ブロックあたりの収穫数)
hayHarvestUnit = 1
woodHarvestFromBushUnit = 1
woodHarvestFromTreeUnit = 5
carrotHarvestUnit = 1
pumpkinHarvestUnit = 1

hayNeedsNumber = 0
woodNeedsNumber = 0
carrotNeedsNumber = 0
pumpkinNeedsNumber = 0

grassPlantedNumber = 0
bushPlantedNumber = 0
treePlantedNumber = 0
carrotPlantedNumber = 0
pumpkinPlantedNumber = 0

# 収穫量 ~~(予定値:人参などは収穫単位がランダムのため実測値ではない)~~
hayHarvestNumber = 0
woodHarvestNumber = 0
carrotHarvestNumber = 0
pumpkinHarvestNumber = 0

hayComp = False
woodComp = False
carrotComp = False
pumpkinComp = False

def setTaregetNumber(numList):
	global hayTargetNumber
	global woodTargetNumber
	global carrotTargetNumber
	global pumpkinTargetNumber
	(
		hayTargetNumber,
		woodTargetNumber,
		carrotTargetNumber,
		pumpkinTargetNumber
	) = numList

def setHarvestRate(numList):
	global hayHarvestRate
	global woodHarvestRate
	global carrotHarvestRate
	global pumpkinHarvestRate
	(
		hayHarvestRate,
		woodHarvestRate,
		carrotHarvestRate,
		pumpkinHarvestRate
	) = numList

def setEntityLevel(numList):
	global carrotLevel
	global pumpkinLevel
	(
		carrotLevel,
		pumpkinLevel
	) = numList

# get_costが解放されればいらなくなるね
# いや、やっぱり残りそうかな...
def calcCost():
	global carrotNeedsNumber
	carrotNeedsNumber = (pumpkinTargetNumber - num_items(Items.Pumpkin)) / pumpkinHarvestRate * pumpkinLevel
	global hayNeedsNumber
	hayNeedsNumber = (carrotTargetNumber + carrotNeedsNumber - num_items(Items.Carrot)) / carrotHarvestRate * carrotLevel
	global woodNeedsNumber
	woodNeedsNumber = (carrotTargetNumber + carrotNeedsNumber - num_items(Items.Carrot)) / carrotHarvestRate * carrotLevel

def init(sizeList, targetNumList, harvestRateList, entityLevelList):
	sizeX, sizeY = sizeList
	global grassPlantedNumber
	grassPlantedNumber = sizeX * sizeY
	setTaregetNumber(targetNumList)
	setHarvestRate(harvestRateList)
	setEntityLevel(entityLevelList)
	calcCost()

def getHayHarvestBasic():
	return hayHarvestUnit * hayHarvestRate

def getWoodHarvestFromBushBasic():
	return woodHarvestFromBushUnit * woodHarvestRate

def getWoodHarvestFromTreeBasic():
	return woodHarvestFromTreeUnit * woodHarvestRate

def getCarrotHarvestBasic():
	return carrotHarvestUnit * carrotHarvestRate

def getPumpkinHarvestBasic():
	return pumpkinHarvestUnit * pumpkinHarvestRate

def getHayExpectationNum():
	return num_items(Items.Hay) + (grassPlantedNumber * getHayHarvestBasic())

def getWoodExpectationNum():
	return num_items(Items.Wood) + (bushPlantedNumber * getWoodHarvestFromBushBasic()) + (treePlantedNumber * getWoodHarvestFromTreeBasic())

def getCarrotExpectationNum():
	return num_items(Items.Carrot) + (carrotPlantedNumber * getCarrotHarvestBasic())

def getPumpkinExpectationNum():
	return num_items(Items.Pumpkin) + (pumpkinPlantedNumber * getPumpkinHarvestBasic())

def isHayComp():
	return num_items(Items.Hay) >= (hayTargetNumber + hayNeedsNumber) or hayComp

def isWoodComp():
	return num_items(Items.Wood) >= (woodTargetNumber + woodNeedsNumber) or woodComp

def isCarrotComp():
	return num_items(Items.Carrot) >= (carrotTargetNumber + carrotNeedsNumber) or carrotComp

def isPumpkinComp():
	return num_items(Items.Pumpkin) >= (pumpkinTargetNumber + pumpkinNeedsNumber) or pumpkinComp

def action(target=""):
	def getTargetPlant(target=""):
		if target != "":
			return target
		if getHayExpectationNum() < (hayTargetNumber + hayNeedsNumber) and not hayComp:
			quick_print("")
			quick_print("getTargetPlant: Hay")
			quick_print("items:",num_items(Items.Hay))
			quick_print("grassPlantedNumber:", grassPlantedNumber)
			quick_print("hayTargetNumber:", hayTargetNumber)
			quick_print("hayNeedsNumber:", hayNeedsNumber)
			change_hat(Hats.Brown_Hat)
			return "Hay"
		if getWoodExpectationNum() < (woodTargetNumber + woodNeedsNumber) and not woodComp:
			quick_print("")
			quick_print("getTargetPlant: Wood")
			quick_print("items:",num_items(Items.Wood))
			quick_print("bushPlantedNumber:", bushPlantedNumber)
			quick_print("treePlantedNumber:", bushPlantedNumber)
			quick_print("woodTargetNumber:", woodTargetNumber)
			quick_print("woodNeedsNumber:", woodNeedsNumber)
			change_hat(Hats.Green_Hat)
			return "Wood"
		if getCarrotExpectationNum() < (carrotTargetNumber + carrotNeedsNumber) and not carrotComp:
			quick_print("")
			quick_print("getTargetPlant: Carrot")
			quick_print("items:",num_items(Items.Carrot))
			quick_print("carrotPlantedNumber:", carrotPlantedNumber)
			quick_print("carrotTargetNumber:", carrotTargetNumber)
			quick_print("carrotNeedsNumber:", carrotNeedsNumber)
			change_hat(Hats.Carrot_Hat)
			return "Carrot"
		if getPumpkinExpectationNum() < (pumpkinTargetNumber + pumpkinNeedsNumber) and not pumpkinComp:
			quick_print("")
			quick_print("getTargetPlant: Pumpkin")
			quick_print("items:",num_items(Items.Pumpkin))
			quick_print("pumpkinPlantedNumber:", pumpkinPlantedNumber)
			quick_print("pumpkinTargetNumber:", pumpkinTargetNumber)
			quick_print("pumpkinNeedsNumber:", pumpkinNeedsNumber)
			change_hat(Hats.Brown_Hat)
			return "Pumpkin"
		quick_print("")
		quick_print("hayComp:",hayComp)
		quick_print("woodComp:",woodComp)
		quick_print("carrotComp:",carrotComp)
		change_hat(Hats.Gray_Hat)
		return ""

	def planTreeOrBush():
		if get_pos_y()%2 == (1 - 1 * get_pos_x()%2):
			if plant(Entities.Tree):
				global treePlantedNumber
				treePlantedNumber += 1
			return
		if plant(Entities.Bush):
			global bushPlantedNumber
			bushPlantedNumber += 1
		return

	if can_harvest():
		entityType = get_entity_type()
		if not hayComp and entityType == Entities.Grass and harvest():
			global grassPlantedNumber
			grassPlantedNumber -= 1
			global hayHarvestNumber
			hayHarvestNumber += getHayHarvestBasic()
			global hayComp
			hayComp = isHayComp()
		if not woodComp and entityType == Entities.Bush and harvest():
			global bushPlantedNumber
			bushPlantedNumber -= 1
			global woodHarvestNumber
			woodHarvestNumber += getWoodHarvestFromBushBasic()
			global woodComp
			woodComp = isWoodComp()
		if not woodComp and entityType == Entities.Tree and harvest():
			global treePlantedNumber
			treePlantedNumber -= 1
			global woodHarvestNumber
			woodHarvestNumber += getWoodHarvestFromTreeBasic()
			global woodComp
			woodComp = isWoodComp()
		if not carrotComp and entityType == Entities.Carrot and harvest():
			global carrotPlantedNumber
			carrotPlantedNumber -= 1
			global carrotHarvestNumber
			carrotHarvestNumber += getCarrotHarvestBasic()
			global carrotComp
			carrotComp = isCarrotComp()
		if not pumpkinComp and entityType == Entities.Pumpkin and harvest():
			global pumpkinPlantedNumber
			pumpkinPlantedNumber -= 1
			global pumpkinHarvestNumber
			pumpkinHarvestNumber += getPumpkinHarvestBasic()
			global pumpkinComp
			pumpkinComp = isPumpkinComp()
			
	targetPlant = getTargetPlant(target)
	if targetPlant == "Wood":
		planTreeOrBush()
		return

	if targetPlant == "Carrot":
		if get_ground_type() != Grounds.Soil:
			till()
		if plant(Entities.Carrot):
			global carrotPlantedNumber
			carrotPlantedNumber += 1
		if get_water() == 0:
			use_item(Items.Water)
		return

	if targetPlant == "Pumpkin":
		if get_ground_type() != Grounds.Soil:
			till()
		if plant(Entities.Pumpkin):
			global pumpkinPlantedNumber
			pumpkinPlantedNumber += 1
		if get_water() == 0:
			use_item(Items.Water)
		return
		
	if get_ground_type() == Grounds.Grassland:
		global grassPlantedNumber
		grassPlantedNumber += 1
	return
