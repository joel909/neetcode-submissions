class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        characters_in_current_string = {}
        for right,letter in enumerate(s):
            # print("letter is : ",letter)
            if letter in characters_in_current_string and characters_in_current_string[letter]>=left:
                left = characters_in_current_string[letter]+1
                characters_in_current_string[letter] = right
            

            characters_in_current_string[letter] = right
            if right-left>=longest:
                longest = (right-left)+1

                # print("longest is")
        # if right-left:
        #     longest = right-left
            
        return longest