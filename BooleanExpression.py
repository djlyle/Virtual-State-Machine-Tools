# BooleanExpression.py
# A class of static utility methods
#
class BooleanExpression:
	
	# higher number => higher precedence
	OPERATORS = {
		"|":1,
		"&":2
	}

	@staticmethod
	def evaluateBooleanExpression(postFixTokenizedBooleanExpression):
		operandStack = []
		for token in postFixTokenizedBooleanExpression:
			if(token in BooleanExpression.OPERATORS):
				operand2 = operandStack.pop()
				operand1 = operandStack.pop()
				result = BooleanExpression.doBooleanOperation(token,operand1,operand2)
				operandStack.append(result)
			else:
				operandStack.append(token == 'True')
		return operandStack[-1]

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
			if(token in BooleanExpression.OPERATORS):
				result.append(token)
			elif(token in assertedBooleanVarsList):
				result.append('True')
			else:
				result.append('False')
		return result						

	@staticmethod
	def infixToPostfixTokenList(infixTokenizedBooleanExpressionList):
                #Converts infix boolean expression string to a postfix expression string
		stack = []
		postfix = []
		for token in infixTokenizedBooleanExpressionList:
			#If the stack is empty or contains a left parenthesis on top, push the incoming operator onto the stack.
			if(token in BooleanExpression.OPERATORS):
				if(len(stack) > 0):
					top = stack[-1]
					while(top in BooleanExpression.OPERATORS and BooleanExpression.OPERATORS[top] >= BooleanExpression.OPERATORS[token]):
						postfix.append(stack.pop())						
						if(stack):
							top = stack[-1]
						else:
							break;
				stack.append(token)
			elif(token == "(" or token == ")"):
				if(token == "("):
					stack.append(token)
				else:
					#if(token == ")")
					try:
						while(stack[-1] != "("):
							postfix.append(stack.pop())  # Adding what's in between ( ) to the postfix list
					except IndexError:
						raise ValueError("'(' not found when popping")

					stack.pop()   	 
			else:
				postfix.append(token)
						
		for token in reversed(stack):
			if token in BooleanExpression.OPERATORS.keys():
				postfix.append(token)
					
		return postfix
	
	
	#Constructor: takes an infix boolean expression string (e.g. "DOG_HAS_FLEAS & (CAT_HAS_COLLAR | CAT_HAS_WORMS)")
	def __init__(self, expressionString):
		self.expressionString = expressionString
		expressionString = expressionString.replace("("," ( ")
		expressionString = expressionString.replace(")"," ) ")
		tokenizedExpression = expressionString.split()
		self.tokenizedExpression = self.infixToPostfixTokenList(tokenizedExpression) 
				
		
	#Evaluate method returns true or false given a list of strings of boolean variable names that assert as True.
	#For example given that this BooleanExpression class was initialized as "DOG_HAS_FLEAS & (CAT_HAS_COLLAR | CAT_HAS_WORMS)"
	#if assertedBooleanVars == ["DOG_HAS_FLEAS","CAT_HAS_COLLAR"]
	#then the result of calling this method will be true
	#but if assertedBooleanVars == ["DOG_HAS_FLEAS","DOG_HAS_COLLAR"] then it will return false since
	#neither "CAT_HAS_COLLAR" or "CAT_HAS_WORMS" were in the assertedBooleanVars list
	def evaluate(self, assertedBooleanVars):
		#For each token in postFixTokenList: 
		#If it is in assertedTrueBoolVars list then replace it with 'True', 
		#otherwise replace it with 'False'
		tokenizedBooleanExpression = self.replaceAssertedBooleanVarsWithBools(self.tokenizedExpression,assertedBooleanVars) 		
		
		#Now evaluate the postfix tokenized boolean expression
		return self.evaluateBooleanExpression(tokenizedBooleanExpression)
		
		
						
