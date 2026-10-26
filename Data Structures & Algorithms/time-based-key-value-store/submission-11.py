class TimeMap:

    def __init__(self):
        self.key_value = dict()
        self.key_index = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_value:
            self.key_value[key].append(value)
            self.key_index[key].append(timestamp)
        else:
            self.key_value[key] = [value]
            self.key_index[key] = [timestamp]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_value:
            return ""
        values = self.key_value[key]
        index = self.binary_search(key,timestamp)
        if index=="":
            return ""
        # print("hii")
        # print(values[index])
        return values[index]
    
    def binary_search(self,key,timestamp):
        array = self.key_index[key]
        left = 0
        right = len(array)-1
        if array[0] > timestamp:
            return ""
        while right>=left:
            mid_point = ((left+right)//2)
            # print("array is : ",array[left:right+1])
            if timestamp>array[mid_point]:
                left = mid_point+1
                if left>=len(array):
                    return len(array)-1
                if array[left]>timestamp:
                    return mid_point    
            elif timestamp<array[mid_point]:
                right = mid_point-1
                if array[right]<timestamp:
                     return right
            else:
                return mid_point
        return mid_point
        
