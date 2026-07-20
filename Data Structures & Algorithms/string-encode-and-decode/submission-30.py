class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += "|"+str(len(string))+"|"+string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        index=1
        closing_index = 1
        count = 0
        final_list = []
        while index<len(s):
            curr_word=""
            count = 0
            while True:
                if s[index] == "|":
                    count = int(s[closing_index:index])
                    index += 1
                    break
                else:
                    index +=1
            new_index = index+count
            curr_word += s[index:new_index]
            index = new_index+1

            final_list.append(curr_word)
            closing_index = index
            # print(final_list)
            # print("cloasing index : "+s[index])
            
        return final_list
