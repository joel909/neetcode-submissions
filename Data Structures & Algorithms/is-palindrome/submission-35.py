class Solution:
    def isPalindrome(self, s: str) -> bool:
        right_end = ""
        left_end = ""
        right_index = 0
        left_index = 1
        for i in range(0,(int(len(s)/2))):
            right_end = s[right_index]
            left_end = s[(len(s))-left_index]
            while right_end.isalnum() != True and right_index+1<=len(s)-1:
                right_index += 1
                right_end = s[right_index]
            while left_end.isalnum() != True and left_index+1<=len(s) :
                left_index += 1
                left_end = s[(len(s))-left_index]
            if right_end.lower() != left_end.lower()  and right_end.isalnum() == True and right_end.isalnum() == True:
                return False
            right_index += 1
            left_index += 1
        return True