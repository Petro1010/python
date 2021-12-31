#BFS Solution:
def validString(s):
        
        stack = []
        
        for i in s:
            if i == "(":
                stack.append("(")
            
            if i == ")":
                if len(stack) == 0:   #if nothing to pop parenthesis are wrong
                    return False
                stack.pop()
        
        return len(stack) == 0


def removeInvalidParentheses(s):
	solutions = set()   #no dups in solution
	minLen = None   #length of the minimal solution

	strings = [s]
	checkedStrings = [s]

	while len(strings):  #while we still have strings to check
		currString = strings.pop(0) #queue FIFO
		if validString(currString):   
			if minLen == None:
				minLen = len(currString)
			else:
				if len(currString) < minLen:  #if it has length less than minimal solution, we have all minimal solutions due to nature of BFS
					break

			solutions.add(currString)

		for i in range(len(currString)):
			if currString[i] not in (")", "("):  #do not remove a character
				continue
			nextStr = currString[:i] + currString[i + 1:]   #string without a specific character, all of length currString - 1
			if nextStr not in checkedStrings:  #if its not been checked, check it
				strings.append(nextStr)
				checkedStrings.append(nextStr)

	return list(solutions)

print(removeInvalidParentheses("()())()"))



#Recursive solution:
class Solution:
    def removeInvalidParentheses(self, s):
        solutions = []
            
        self.removeInvalidParRec(s, solutions, 0)
        #solutions now filled with valid options, so pick out non dups and minimal changes
        
        finalSol = [solutions[0]]
        
        for i in solutions:
            if i in finalSol:    #if its a dup dont include
                continue
                
            else:
                finalSol.append(i)
            
        
        return finalSol
    
    def removeInvalidParRec(self, s, solutions, ind):
        #print(s)
        if self.validString(s):  #valid string so add it to solutions
            if len(solutions) > 0 and len(s) < len(solutions[0]):  #get a solution that is not minimal
                return
            solutions.append(s)
            
        if ind >= len(s):  #if the index is past the string length then we have exhausted all options
            return
            
        if s[ind] not in ["(", ")"]:
            self.removeInvalidParRec(s, solutions, ind + 1)  #keep the letter at ind...
        
        else:
            self.removeInvalidParRec(s, solutions, ind + 1)  #keep the bracket at ind...
            self.removeInvalidParRec(s[:ind] + s[ind + 1:], solutions, ind)  #remove the bracket at ind...
        
        
        
    
    def validString(self, s):
        
        stack = []
        
        for i in s:
            if i == "(":
                stack.append("(")
            
            if i == ")":
                if len(stack) == 0:   #if nothing to pop parenthesis are wrong
                    return False
                stack.pop()
        
        return len(stack) == 0