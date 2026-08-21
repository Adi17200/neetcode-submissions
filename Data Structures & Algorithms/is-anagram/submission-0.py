class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i = sorted(s)
        j = sorted(t)
        if i == j:
            return True
        return False
        