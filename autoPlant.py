# 目標値(Target Number)とコスト(Needs Number)から目標収穫数を設定。
# 植栽した数(Planted Number)と1ブロックあたりの収穫単位(Harvest Unit)と収穫率(Harvest Rate)から予想収穫量を計算。
# 目標収穫数と予想収穫量から、植栽や収穫の判断(何を植えるか? 収穫は行うのか?)をさせてみた。
# 干し草、木材、人参、カボチャの順で植栽・収穫しようとします
#
# ~~人参の収穫で気付いたが、1ブロックからの収穫数がランダム。~~
# ~~とは言え、おそらく「植栽数 * 収穫単位(人参は土地1ブロックにつき1個) * 収穫率」が最低値と思われる。~~
# ~~予想よりも多く収穫できる分には困らないからこのまま進めてみる。~~
# ちゃんとログに書き出して確認したらランダムじゃないし、想定した計算であってる...落ち着け自分...

import config

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

def getExpectedPumpkinUnit(pumpkinPlantSize = 1):
	if pumpkinPlantSize > 6:
		return (pumpkinPlantSize ** 2) * 6 * config.HarvestRatePumpkin
	return pumpkinPlantSize ** 3 * config.HarvestRatePumpkin

# 目標値と所持数から必要な植栽数を算出

def getPumpkinPlantFromTargetNum(pumpkinPlantSize = 1):
	goal = config.TargetNumberPumpkin + getPumpkinNeeds() - num_items(Items.Pumpkin)
	if goal <= 0:
		return 0
	unit = getExpectedPumpkinUnit(pumpkinPlantSize)
	roundUp = 0
	if goal % unit > 0:
		roundUp = 1
	return (goal // unit + roundUp) * (pumpkinPlantSize ** 2)

def getCarrotPlantFromTargetNum(pumpkinPlantSize = 1):
	goal = config.TargetNumberCarrot + getCarrotNeeds(pumpkinPlantSize) - num_items(Items.Carrot)
	if goal <= 0:
		return 0
	unit = config.HarvestUnitCarrot * config.HarvestRateCarrot
	roundUp = 0
	if goal % unit > 0:
		roundUp = 1
	return goal // unit + roundUp

# 木材の植栽数だけリスト[Bush数, Tree数]で返すよ
def getWoodPlantFromTargetNum(pumpkinPlantSize = 1):
	def distributeUnit(num):
		if num <= bushUnit:
			return [1, 0]
		if num <= treeUnit:
			return [0, 1]
	goal = config.TargetNumberWood + getWoodNeeds(pumpkinPlantSize) - num_items(Items.Wood)
	if goal <= 0:
		return [0, 0]
	bushUnit = config.HarvestWoodFromBushUnit * config.HarvestRateWood
	treeUnit = config.HarvestWoodFromTreeUnit * config.HarvestRateWood
	unit = bushUnit + treeUnit
	if goal <= treeUnit:
		return distributeUnit(goal)
	plantNum = goal // unit
	distribution = distributeUnit(goal % unit)
	return [plantNum + distribution[0], plantNum + distribution[1]]

def getHayPlantFromTargetNum(pumpkinPlantSize = 1):
	goal = config.TargetNumberHay + getHayNeeds(pumpkinPlantSize) - num_items(Items.Hay)
	if goal <= 0:
		return 0
	unit = config.HarvestUnitHay + config.HarvestRateHay
	roundUp = 0
	if goal % unit > 0:
		roundUp = 1
	return goal // unit + roundUp

# 必要な植栽数からコストを算出

def getPumpkinNeeds():
	return 0

def getCarrotNeeds(pumpkinPlantSize = 1):
	pumpkin = getPumpkinPlantFromTargetNum(pumpkinPlantSize) * config.EntityLevelPumpkin
	# ヒマワリの計算は未実装
	sunflower = 0
	return pumpkin + sunflower

def getWoodNeeds(pumpkinPlantSize = 1):
	carrot = getCarrotPlantFromTargetNum(pumpkinPlantSize) * config.EntityLevelCarrot
	return carrot

def getHayNeeds(pumpkinPlantSize = 1):
	carrot = getCarrotPlantFromTargetNum(pumpkinPlantSize) * config.EntityLevelCarrot
	return carrot


# get_costが解放されればいらなくなるね
# いや、やっぱり残りそうかな...
def calcCost(pumpkinPlantSize = 1):
	global carrotNeedsNumber
	carrotNeedsNumber = getCarrotNeeds(pumpkinPlantSize)
	global hayNeedsNumber
	hayNeedsNumber = getHayNeeds(pumpkinPlantSize)
	global woodNeedsNumber
	woodNeedsNumber = getWoodNeeds(pumpkinPlantSize)

# 設定値をconfig.pyに分離することでinitは不要になるかも
def init(sizeList):
	sizeX, sizeY = sizeList
	global grassPlantedNumber
	grassPlantedNumber = sizeX * sizeY
	calcCost()

def getHayHarvestBasic():
	return config.HarvestUnitHay * config.HarvestRateHay

def getWoodHarvestFromBushBasic():
	return config.HarvestWoodFromBushUnit * config.HarvestRateWood

def getWoodHarvestFromTreeBasic():
	return config.HarvestWoodFromTreeUnit * config.HarvestRateWood

def getCarrotHarvestBasic():
	return config.HarvestUnitCarrot * config.HarvestRateCarrot

def getPumpkinHarvestBasic():
	return config.HarvestUnitPumpkin * config.HarvestRatePumpkin

def getHayExpectationNum():
	return num_items(Items.Hay) + (grassPlantedNumber * getHayHarvestBasic())

def getWoodExpectationNum():
	return num_items(Items.Wood) + (bushPlantedNumber * getWoodHarvestFromBushBasic()) + (treePlantedNumber * getWoodHarvestFromTreeBasic())

def getCarrotExpectationNum():
	return num_items(Items.Carrot) + (carrotPlantedNumber * getCarrotHarvestBasic())

def getPumpkinExpectationNum():
	return num_items(Items.Pumpkin) + (pumpkinPlantedNumber * getPumpkinHarvestBasic())

def isHayComp():
	return num_items(Items.Hay) >= (config.TargetNumberHay + hayNeedsNumber) or hayComp

def isWoodComp():
	return num_items(Items.Wood) >= (config.TargetNumberWood + woodNeedsNumber) or woodComp

def isCarrotComp():
	return num_items(Items.Carrot) >= (config.TargetNumberCarrot + carrotNeedsNumber) or carrotComp

def isPumpkinComp():
	return num_items(Items.Pumpkin) >= (config.TargetNumberPumpkin + pumpkinNeedsNumber) or pumpkinComp

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
		if getWoodExpectationNum() < (config.TargetNumberWood + woodNeedsNumber) and not woodComp:
			quick_print("")
			quick_print("getTargetPlant: Wood")
			quick_print("items:",num_items(Items.Wood))
			quick_print("bushPlantedNumber:", bushPlantedNumber)
			quick_print("treePlantedNumber:", bushPlantedNumber)
			quick_print("woodTargetNumber:", config.TargetNumberWood)
			quick_print("woodNeedsNumber:", woodNeedsNumber)
			change_hat(Hats.Green_Hat)
			return "Wood"
		if getCarrotExpectationNum() < (config.TargetNumberCarrot + carrotNeedsNumber) and not carrotComp:
			quick_print("")
			quick_print("getTargetPlant: Carrot")
			quick_print("items:",num_items(Items.Carrot))
			quick_print("carrotPlantedNumber:", carrotPlantedNumber)
			quick_print("carrotTargetNumber:", config.TargetNumberCarrot)
			quick_print("carrotNeedsNumber:", carrotNeedsNumber)
			change_hat(Hats.Carrot_Hat)
			return "Carrot"
		if getPumpkinExpectationNum() < (config.TargetNumberPumpkin + pumpkinNeedsNumber) and not pumpkinComp:
			quick_print("")
			quick_print("getTargetPlant: Pumpkin")
			quick_print("items:",num_items(Items.Pumpkin))
			quick_print("pumpkinPlantedNumber:", pumpkinPlantedNumber)
			quick_print("pumpkinTargetNumber:", config.TargetNumberPumpkin)
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
