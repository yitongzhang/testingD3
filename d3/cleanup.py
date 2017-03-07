# Create dataList object
import csv
with open('parseplz.csv', 'rb') as f:
    reader = csv.reader(f)
    relationshipCsv = list(reader)

class company:
	companyCount = 0
	def __init__(self, name,children):
		self.name = name
		# self.parent = parent
		# self.parentId = parentId
		self.children = children
		# self.industry = industry
		# self.revenue = revenue
		# self.founder = founder
		# self.logo = logo
	companyCount+=1


companyDict = {}


# stick list of list into 
for relationship in relationshipCsv:
	# check if the self company exists
	if relationship[0] not in companyDict:
		companyDict[relationship[0]] = company(relationship[0],[])
		# print "added" + relationship[0]
	# check if the parent exists
	if relationship[1] not in companyDict:
		companyDict[relationship[1]] = company(relationship[1],[])
		# print "added" + relationship[1]
	# check if the child exists
	if relationship[3] not in companyDict:
		companyDict[relationship[3]] = company(relationship[3],[])
		# print "added" + relationship[3]

	# update parent if parent does not exist
	if not hasattr(companyDict[relationship[0]],"parent"):
		companyDict[relationship[0]].parent = companyDict[relationship[1]]
	
	# update children if child does not exist
	if companyDict[relationship[3]] not in companyDict[relationship[0]].children:
		companyDict[relationship[0]].children.append(companyDict[relationship[3]])

# Testing printing stuff
print "my name is "+companyDict["Google"].name
print "my parent is "+companyDict["Google"].parent.name
print "I have "+ str(len(companyDict["Google"].children))+" kids"
print "my kids are: "
for kids in companyDict["Google"].children:
	print kids.name


# #creates a list of top level companies
# def findTopDogs(initialList):
# 	resultList =[]
# 	for item in initialList:
# 		if item[1] =="":
# 			resultList.append(item) 
# 	return resultList

# # Merge lists so that there is only 1 for each top level company
# def dedupe(initialList):
# 	#create a list of unique names
# 	resultList =[]
# 	for item in initialList:
# 		if item[0] not in resultList:
# 			resultList.append(item[0])
# 			print(item[0])
# 	return resultList


# # Execute all the stuff
# allCompanies = relationshipCsv
# topLevelCompanies = findTopDogs(relationshipCsv)
# dedupedTopLevelCompanies = dedupe(topLevelCompanies)



