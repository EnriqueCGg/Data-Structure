
class MathVerification():
    def __init__(self):
        self.verification = []
        
    def isempty(self):
        if len(self.verification) == 0:
            print('Balanced Expression')
            return True
        else:
            print('Error: Unbalanced parentheses')
    
    def verify(self, expression):
        for x in expression:
            if x == '(':
                self.verification.append(x)
            if x == ')':
                try:
                    self.verification.pop()
                except:
                    print('Error: Unbalanced parentheses \')\'')
                    return
                
        self.isempty()
        self.verification = []
                

#Test
m = MathVerification()
m.verify('(2 + 3) * (4 - (1 + 5))')
m.verify('(2 + 3 * (4 - (1 + 5))')
m.verify('(2 + 3) * 4 - (1 + 5))')
