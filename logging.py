import config
import autoPlant

def itemLog(message = ""):
	quick_print("")
	quick_print(message)
	quick_print("The number of items")
	quick_print("  - hay    :", num_items(Items.Hay))
	quick_print("  - wood   :", num_items(Items.Wood))
	quick_print("  - carrot :", num_items(Items.Carrot))
	quick_print("  - pumpkin:", num_items(Items.Pumpkin))

def wantPlant(message = ""):
	quick_print(
		"[Want plant]",
		message,
		"Hay:", autoPlant.getHayPlantFromTargetNum(config.PumpkinPlantSize),
		"Wood:", autoPlant.getWoodPlantFromTargetNum(config.PumpkinPlantSize),
		"Carrot:", autoPlant.getCarrotPlantFromTargetNum(config.PumpkinPlantSize), 
		"Pumpkin:", autoPlant.getPumpkinPlantFromTargetNum(config.PumpkinPlantSize)
	)

def map(message = ""):
	quick_print("")
	quick_print(message)
	for x in range(get_world_size()):
		quick_print(config.map[x])

def compLog():
	quick_print("")
	quick_print("## complete Log")
	quick_print("Target Number")
	quick_print("  - hay    :", config.TargetNumberHay)
	quick_print("  - wood   :", config.TargetNumberWood)
	quick_print("  - carrot :", config.TargetNumberCarrot)
	quick_print("  - pumpkin:", config.TargetNumberPumpkin)
	quick_print("Planted Number")
	quick_print("  - grass :", autoPlant.grassPlantedNumber)
	quick_print("  - bush  :", autoPlant.bushPlantedNumber)
	quick_print("  - tree  :", autoPlant.treePlantedNumber)
	quick_print("  - carrot:", autoPlant.carrotPlantedNumber)
	quick_print("  - pumpkin", autoPlant.pumpkinPlantedNumber)
	quick_print("Harvest Number")
	quick_print("  - hay    :", autoPlant.hayHarvestNumber)
	quick_print("  - wood   :", autoPlant.woodHarvestNumber)
	quick_print("  - carrot :", autoPlant.carrotHarvestNumber)
	quick_print("  - pumpkin:", autoPlant.pumpkinHarvestNumber)
