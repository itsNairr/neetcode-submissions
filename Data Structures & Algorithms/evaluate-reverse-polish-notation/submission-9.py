class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return None
        if len(tokens) == 1:
            return tokens[0]
        stack = []
        sett = {'+','-','*','/'}
        n1 = None
        for tok in tokens:
            print(stack)
            if tok in sett:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if tok == '+':
                    n1 += n2
                elif tok == '-':
                    n1 -= n2
                elif tok == '*':
                    n1 = n1 * n2
                else:
                    n1 = int(n1 / n2)
                stack.append(n1)
                continue
            stack.append(tok)
        return n1


        