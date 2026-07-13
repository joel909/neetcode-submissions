class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        for letter in s :
            a[ord(letter)-ord("a")] += 1
        b = [0]*26
        for letter in t :
            b[ord(letter)-ord("a")] += 1
        if a==b:
            return True 
        return False
        