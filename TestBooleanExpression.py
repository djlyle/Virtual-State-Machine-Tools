from BooleanExpression import BooleanExpression

be1 = BooleanExpression("A & (B | C)")
assertedVars = ["A","B"]
result = be1.evaluate(assertedVars)
if(result == True):
	print "Boolean expression evaluated as true"
else:
	print "Boolean expression evaluated as false"

	
