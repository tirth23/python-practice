#evaluation of postfix expression
class Evaluate:
    def __init__(self):
        self.stack = []

    def isDigit(self, digit):
        if ord(digit) >= 48 and ord(digit) <= 57:
            return 1
        else:
            return 0

    def evaluatepostfix(self, exp):
        for i in range(len(exp)):
            if self.isDigit(exp[i]):
                self.stack.append(int(exp[i]))
            elif exp[i] == " ":
                pass
            else:
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                op = self.perform(exp[i], op1, op2)
                self.stack.append(op)
        
        return self.stack.pop()
    
    def perform(self, operator, op1, op2):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        elif operator == '/':
            return op1 / op2
        else:
            return '!'

if __name__ == "__main__":
    
    exp = input("Enter postfix expression to evaluate : ")
    ev = Evaluate()
    print(ev.evaluatepostfix(exp))