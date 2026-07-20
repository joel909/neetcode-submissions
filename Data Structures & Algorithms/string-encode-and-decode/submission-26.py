class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            if len(string)<10:
                encoded_string += "!#"+str(len(string))+string
            elif len(string)>=10 and len(string)<100:
                encoded_string += "!!"+str(len(string))+string
            else:
                encoded_string += "!+"+str(len(string))+string
        return encoded_string
            

    def decode(self, s: str) -> List[str]:
        index = 0
        final_list = []
        if len(s) < 2:
            return []
        if s[1] == "!":
            count=int(s[2:4])
            index += 1
        elif s[1] == "+":
            count = int(s[2:5])
            index += 2
        else:
            count = int(s[2])
        index += 3
        while index <= len(s):
            # print("first count : ",count)
            curr_item = ""
            for i in range(0,count):
                curr_item += s[index+i]
            final_list.append(curr_item)
            # print(final_list)
            if index+count+2>=len(s):
                break
            # print("next count",s[index+count+2])
            min_addition = index+count+2
            if s[min_addition-1]  == "!":
                count = int(s[min_addition:min_addition+2])
                min_addition +=1
                # print("new count is more than 10",s[min_addition:min_addition+2])
            elif s[min_addition-1] == "+":
                count = int(s[min_addition:min_addition+3])
                min_addition +=2
                # print("new count is more than 100",s[min_addition:min_addition+2])
            else:
                count = int(s[min_addition])
                
            index = min_addition+1
            
            
            curr_item = ""
            # print(final_list)
            # if index+2>=len(s) and count != 0:
            #     # print("breaking")
            #     break
        return final_list


