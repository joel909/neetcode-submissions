class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for item in strs:
            encoded += item+"|A|"
        return encoded


    def decode(self, s: str) -> List[str]:
        i = 0
        li = list(s)
        final_list = []
        curr_word = ""
        while True:
            if(i+2 <len(li)):
                if li[i] == "|" and li[i+1] == "A" and li[i+2] == "|":
                    final_list.append(curr_word)
                    curr_word = ""
                    del li[i]
                    del li[i]
                else:
                    curr_word += li[i]
                i = i+1
            else:
                break
        return final_list
        
