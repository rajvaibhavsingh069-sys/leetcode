class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        n=len(s)

        for i in range(n):
            if stack:
                last=stack[-1]
                if self.pairs(last,s[i]):
                    stack.pop()
                    continue
            stack.append(s[i])
        return not stack

    def pairs(self,last,current):
        if last=="("and current ==")"or last=="{"and current=="}"or last=="["and current=="]":
            return True 
        return False