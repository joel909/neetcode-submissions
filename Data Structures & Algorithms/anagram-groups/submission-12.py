class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        full_map = {}
        for index,word in enumerate(strs):
            letter_map = [0]*26
            hashed_letter_map = tuple()
            for letter in word:
                letter_map[ord(letter)-ord("a")] += 1
                hashed_letter_map = tuple(letter_map)
            if hashed_letter_map in full_map:
                full_map[hashed_letter_map].append(word)
            else:
                full_map[hashed_letter_map] = [word]
        mapped_list = []
        for map_item in full_map:
            mapped_list.append(full_map[map_item])
        return mapped_list

            
        