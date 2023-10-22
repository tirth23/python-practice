class Postfix:
    def __init__(self):
        self.stack = []

    def isoperand(self, op):
        if (ord(op) >= 65 and ord(op) <= 90) or (ord(op) >= 97 and ord(op) <= 122) or (ord(op) >= 48 and ord(op) <= 57):
            return 1
        else:
            return 0

    def isoperator(self, oper):
        if oper == '+' or oper == '-' or oper == '*' or oper == '/' or oper == '$' or oper == '^':
            return 1
        else:
            return 0

    def getoperatorweight(self, op):
        weight = -1
        if op == '+' or op == '-':
            weight = 1
        elif op == '*' or op == '/':
            weight = 2
        elif op == '$' or op == '^':
            weight = 3
        return weight

    def isrightassociative(self, op):
        #only $ or ^ has right associativity
        if op == '$' or op == '^':       
            return 1
        else:
            return 0

    def hashigherprecedence(self, op1, op2):
        op1weight = self.getoperatorweight(op1)
        op2weight = self.getoperatorweight(op2)

        if op1weight == op2weight:
            if self.isrightassociative(op1):
                return 0
            else:
                return 1

        if op1weight > op2weight:
            return 1
        else:
            return 0

    def infixtopostfix(self, exp):
        postfix = ""
        for i in range(len(exp)):
            if exp[i] == " ":
                continue
            
            elif self.isoperator(exp[i]):
                while len(self.stack) != 0 and self.stack[-1] != '(' and self.hashigherprecedence(self.stack[-1], exp[i]):
                    postfix = postfix + self.stack[-1]
                    self.stack.pop()
                self.stack.append(exp[i])
            
            elif self.isoperand(exp[i]):
                postfix = postfix + exp[i]
            
            elif exp[i] == '(':
                self.stack.append(exp[i])
            
            elif exp[i] == ')':
                while len(self.stack) != 0 and self.stack[-1] != '(':
                    postfix = postfix + self.stack[-1]
                    self.stack.pop()
                self.stack.pop()
                
        while len(self.stack) != 0:
            postfix = postfix + self.stack[-1]
            self.stack.pop()
        return postfix

if __name__ == "__main__":
    
    pf = Postfix()
    exp = input("Enter infix expression to convert it to postfix : ")
    print(pf.infixtopostfix(exp))