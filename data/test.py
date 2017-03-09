# currentNb = 0
# nextNb = 1
# for i in xrange(1,10):
# 	sumNb = currentNb + nextNb
# 	print sumNb
# 	currentNb = nextNb
# 	nextNb = sumNb

def traverseTree (startingNode)
	if not hasattr(startingNode, "children")
		print startingNode
		return
	else
	 traverseTree(startingNode.children[0])


# as long as there is a first child, grab first child, grab first child, etc.
# go up one level, grab next child
# grab first child, grab first child, etc.
# go up one level, grab next child