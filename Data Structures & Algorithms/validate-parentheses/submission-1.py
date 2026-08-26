class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cTop = {")" : "(", "]" : "[", "}": "{"}

        for c in s:
            if c in cTop:
                if stack and stack[-1] == cTop[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False