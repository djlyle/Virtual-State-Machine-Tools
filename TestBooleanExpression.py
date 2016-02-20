from BooleanExpression import BooleanExpression

be1 = BooleanExpression("A & (B | C)")
assertedVars = ["A","B"]
result = be1.evaluate(assertedVars)
if(result == True):
	print "Boolean expression evaluated as true"
else:
	print "Boolean expression evaluated as false"

	
be2 = BooleanExpression("A & (B | (C & D))")
assertedVars = ["A","C","D"]
result = be2.evaluate(assertedVars)
if(result == True):
	print "Boolean expression evaluated as true"
else:
	print "Boolean expression evaluated as false"

be3 = BooleanExpression("((A | B) & (C | D))")
assertedVars = ["A","D"]
result = be3.evaluate(assertedVars)
if(result == True):
	print "Boolean expression evaluated as true"
else:
	print "Boolean expression evaluated as false"

be4 = BooleanExpression("((A | B) & (C | D))")
assertedVars = ["A","B"]
result = be4.evaluate(assertedVars)
if(result == True):
	print "Boolean expression evaluated as true"
else:
	print "Boolean expression evaluated as false"
