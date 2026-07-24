class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_length = len(s)
        right_index , left_index = 0,s_length-1
        while left_index>right_index:
            if s[left_index].isalnum() == False:
                left_index -= 1
                continue
            if s[right_index].isalnum() == False:
                right_index += 1
                continue
            if s[left_index].lower() != s[right_index].lower():
                print("comparing ",s[left_index].lower()," and ",s[right_index].lower())
                return False
            left_index -= 1
            right_index += 1
        return True
        