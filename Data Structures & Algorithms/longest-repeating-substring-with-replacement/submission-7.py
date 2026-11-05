class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        largest_character = s[0]
        letter_count = {}
        largest = 0
        for right,item in enumerate(s):
            # print("hi")
            if item not in letter_count:
                if letter_count == {}:
                    largest_character = item
                    letter_count[item] = 1
                    continue
                else:
                    letter_count[item] = 1
            else:
                if letter_count[item]+1>letter_count[largest_character]:
                    largest_character = item
                    # print("Updated argest charachter to : ",largest_character)
                letter_count[item] +=1

            others = (right-(left+letter_count[largest_character])+1)
            # print("Others is : ",others)
            if others>k:
                # print("Fuck you : ",s)
                letter_count[s[left]] -= 1
                left += 1
                if letter_count[s[left]] == 0:
                    letter_count.pop(s[left])
                largest_character = ""
                largest_character_count = 0
                for key in letter_count:
                    if letter_count[key]> largest_character_count:
                        largest_character = key
                        largest_character_count = letter_count[key]                    
                
            if largest<=right-left:   
                largest = (right-left)+1
                # print("FAHH")
            if largest ==0 and right==(len(s)-1):
                # print("FAHH")
                return (right-left)+1
                
        # print("here")
        if len(s)==1 and k==0:
            return 1
        return largest
        