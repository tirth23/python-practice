class BalancedParenthesis:

    def __init__(self):
        self.stack = []

    def arepair(self, opening, closing):
        if opening == '(' and closing == ')':
            return 1
        elif opening == '{' and closing == '}':
            return 1
        elif opening == '[' and closing == ']':
            return 1
        else:
            return 0

    def arebalance(self, exp):
        for i in range(len(exp)):
            if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
                self.stack.append(exp[i])
            elif exp[i] == ')' or exp[i] == '}' or exp[i] == ']':
                if len(self.stack) == 0 or not(self.arepair(self.stack[-1], exp[i])):     #check stack[top] equal to exp[i]
                    return 0
                else:
                    self.stack.pop()
        if len(self.stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    
    bp = BalancedParenthesis()
    exp = input("Enter expression : ")
    if bp.arebalance(exp):
        print("Balanced.")
    else:
        print("Imbalanced.")