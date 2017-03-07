dupeList = [0,2,2,2,3,0,5,6,7,8,9,4,4,3,5,8,2]

def dedupe(initialList):
	#create a list of unique names
	resultList =[]
	for item in initialList:
		if item not in resultList:
			resultList.append(item)
			print(item)
		else:
			print("dupe, skip.")

dedupe(dupeList)