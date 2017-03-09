# Create dataList object
import csv
with open('test.csv', 'rb') as f:
    reader = csv.reader(f)
    relationshipCsv = list(reader)

class company:
	companyCount = 0
	def __init__(self, name,children,parents):
		self.name = name
		self.children = children
		self.parents = parents
	companyCount+=1

class treeRelation:
	def __init__(self, name,relationList):
		self.name = name
		self.relationList = relationList

companyDict = {}
relationDict ={}

# stick list of list into 
for relationship in relationshipCsv:
	# check if the self company exists
	if relationship[0] not in companyDict:
		companyDict[relationship[0]] = company(relationship[0],[],[])
		# print "added" + relationship[0]
	# check if the parents exists
	if relationship[1] not in companyDict:
		companyDict[relationship[1]] = company(relationship[1],[],[])
		# print "added" + relationship[1]
	# check if the child exists
	if relationship[3] not in companyDict:
		companyDict[relationship[3]] = company(relationship[3],[],[])
		# print "added" + relationship[3]

	# update parents if parents does not exist
	if companyDict[relationship[1]] not in companyDict[relationship[0]].parents:
		companyDict[relationship[0]].parents.append(companyDict[relationship[1]])
	
	# update children if child does not exist
	if companyDict[relationship[3]] not in companyDict[relationship[0]].children:
		companyDict[relationship[0]].children.append(companyDict[relationship[3]])

# Test printing alphabet
print "my name is "+companyDict["Motorola Solutions"].name
print "I have "+ str(len(companyDict["Motorola Solutions"].parents))+" parents"

print "my parents are: "
for parents in companyDict["Motorola Solutions"].parents:
	print parents.name

print "I have "+ str(len(companyDict["Motorola Solutions"].children))+" kids"
print "my kids are: "
for kids in companyDict["Motorola Solutions"].children:
	print kids.name


def findAllKids(topLevelCo):
	##append 
	csvString = topLevelCo.name

    if not hasattr(topLevelCo, "children"):
    	return csvString

    else:
        for child in topLevelCo.children:
            match = child.findAllKids(name)
            if match:
                return match




# For each parents company

# find first child until there are no more children

# store that chain

# back up one level

# store next chain

# for each item in dictionary



# # Execute all the stuff
# allCompanies = relationshipCsv
# topLevelCompanies = findTopDogs(relationshipCsv)
# dedupedTopLevelCompanies = dedupe(topLevelCompanies)



