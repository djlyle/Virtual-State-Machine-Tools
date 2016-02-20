# BooleanExpression.py
# A class of static utility methods
#
class BooleanExpression:
	
	# higher number => higher precedence
	OPERATORS = {
		"|":1,
		"&":2
	}
	
	#Constructor: takes an infix boolean expression string (e.g. "DOG_HAS_FLEAS & (CAT_HAS_COLLAR | CAT_HAS_WORMS)")
	def __init__(self, infixBooleanVarExpressionString):
		self.booleanVarExpressionString = infixBooleanVarExpressionString
		expressionString = BooleanExpression.infixBooleanVarExpressionString.replace("("," ( ")
		expressionString = expressionString.replace(")"," ) ")
		infixTokenizedBooleanVarExpression = expressionString.split()
		self.postfixTokenizedBooleanVarExpression = BooleanExpression.infixTokenListToPostfixTokenList(infixTokenizedBooleanVarExpression) 
				
		
	#Evaluate method returns true or false given a list of strings of boolean variable names that assert as True.
	#For example given that this BooleanExpression class was initialized as "DOG_HAS_FLEAS & (CAT_HAS_COLLAR | CAT_HAS_WORMS)"
	#if assertedTrueBoolVars == ["DOG_HAS_FLEAS","CAT_HAS_COLLAR"]
	#then the result of calling this method will be true
	#but if assertedTrueBoolVars == ["DOG_HAS_FLEAS","DOG_HAS_COLLAR"] then it will return false since
	#neither "CAT_HAS_COLLAR" or "CAT_HAS_WORMS" were in the assertedTrueBoolVars list
	def evaluate(self, assertedBooleanVarsList):
		#For each token in postFixTokenList: 
		#If it is in assertedTrueBoolVars list then replace it with 'True', 
		#otherwise replace it with 'False'
		postFixTokenizedBooleanExpression = BooleanExpression.replaceAssertedBooleanVarsWithBools(self.postfixTokenizedBooleanVarExpression) 		
		
		#Now evaluate the postfix tokenized boolean expression
		return BooleanExpression.evaluateBooleanExpression(postFixTokenizedBooleanExpression)
		
	@staticmethod
	def evaluateBooleanExpression(postFixTokenizedBooleanExpression):
		operandStack = []
		for token in postFixTokenizedBooleanExpression:
			if(token in OPERATORS):
				operand2 = operandStack.pop()
				operand1 = operandStack.pop()
				result = BooleanExpression.doBooleanOperation(token,operand1,operand2)
				operandStack.push(result)
			else:
				operandStack.push(token == 'True')
		return 

	@staticmethod
	def doBooleanOperation(op,operand1,operand2):
		if(op == "&"):
			return operand1 and operand2
		elif(op == "|"):
			return operand1 or operand2
		else:
			raise ValueError("op must be & or |")
		
	@staticmethod
	def replaceAssertedBooleanVarsWithBools(tokenizedBooleanVarExpressionList,assertedBooleanVarsList):
		result = []
		for token in tokenizedBooleanVarExpressionList:
			if(token in OPERATORS):
				result.append(token)
			elif(token in assertedBooleanVarsList):
				result.append('True')
			else:
				result.append('False')
		return result						
	
	@staticmethod
	def infixTokenListToPostfixTokenList(infixTokenizedBooleanExpressionList):
		#Converts infix boolean expression string to a postfix expression string
		stack = []
		postfix = []
		for token in infixTokenizedBooleanExpressionList:
			#If the stack is empty or contains a left parenthesis on top, push the incoming operator onto the stack.
			if(token in OPERATORS):
				if(len(stack) > 0):
					top = stack[-1]
					while(top in OPERATORS and OPERATORS[top] >= OPERATORS[token]):
						postfix.append(stack.pop())						
						if(stack):
							top = stack[-1]
						else:
							break;
				stack.append(token)
			if(c == "(" or c == ")"):
				if(c == "("):
					stack.append(token)
				else:
					#if(c == ")")
					try:
						while(stack[-1] != "("):
							postfix.append(stack.pop())  # Adding what's in between ( ) to the postfix list
					except IndexError:
						raise ValueError("'(' not found when popping")

					stack.pop()   	 
			else:
				postfix.append(token)
						
		for token in reversed(stack):
			if token in OPERATORS.keys():
				postfix.append(token)
					
		return postfix
	

						