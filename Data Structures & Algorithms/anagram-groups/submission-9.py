class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        full_map = {}
        for index,word in enumerate(strs):
            letter_map = [0]*26
            for letter in word:
                letter_map[ord(letter)-ord("a")] += 1
            if str(letter_map) in full_map:
                full_map[str(letter_map)].append(word)
            else:
                full_map[str(letter_map)] = [word]
        mapped_list = []
        for map_item in full_map:
            mapped_list.append(full_map[map_item])
        return mapped_list

            
        